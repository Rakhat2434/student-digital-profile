/* Offline Figma plugin. Changes only a newly created page. */
figma.showUI(__html__, { width: 480, height: 520 });
let running = false;
let completedPage = null;
const rgb = hex => ({ r: parseInt(hex.slice(1, 3), 16) / 255, g: parseInt(hex.slice(3, 5), 16) / 255, b: parseInt(hex.slice(5, 7), 16) / 255 });
const status = (text, done = false) => figma.ui.postMessage({ type: 'status', text, done });

figma.ui.onmessage = async message => {
  if (message.type === 'close') { figma.closePlugin(); return; }
  if (message.type !== 'build' || running) return;
  if (completedPage) { await figma.setCurrentPageAsync(completedPage); status('Already built. Select a starting frame and press Present.', true); return; }
  running = true;
  const previousPage = figma.currentPage;
  let page;
  try {
    const fonts = (await figma.listAvailableFontsAsync()).map(item => item.fontName);
    const chosen = {};
    for (const family of ['Manrope', 'IBM Plex Sans']) {
      for (const weight of [400, 500, 600, 650, 700]) {
        const preferred = weight >= 600 ? ['SemiBold', 'Semi Bold', 'Bold', 'Medium', 'Regular'] : weight >= 500 ? ['Medium', 'Regular'] : ['Regular'];
        chosen[family + weight] = preferred.map(style => fonts.find(f => f.family === family && f.style === style)).find(Boolean);
        if (!chosen[family + weight]) throw new Error('Required product font is unavailable: ' + family);
      }
    }
    const unique = new Map(Object.values(chosen).map(font => [JSON.stringify(font), font]));
    await Promise.all(Array.from(unique.values()).map(font => figma.loadFontAsync(font)));
    page = figma.createPage();
    page.name = 'SDP-7 · Interactive revision ' + PROTOTYPE.version;
    await figma.setCurrentPageAsync(page);
    const frames = {};
    let count = 0;
    for (const screen of PROTOTYPE.screens) {
      const frame = figma.createFrame();
      page.appendChild(frame);
      frame.name = screen.key + ' · ' + screen.name;
      frame.resize(screen.width, screen.height);
      frame.x = 200 + (count % 5) * 1560;
      frame.y = 200 + Math.floor(count / 5) * 1260;
      frame.clipsContent = true;
      const vectors = figma.createNodeFromSvg(screen.vectorSvg);
      frame.appendChild(vectors);
      vectors.name = 'Vector artwork'; vectors.x = 0; vectors.y = 0;
      // Keep text editable rather than embedding text outlines in the SVG artwork.
      for (const spec of screen.texts) {
        const t = figma.createText();
        t.fontName = chosen[spec.family + spec.weight];
        t.characters = spec.text; t.fontSize = spec.size;
        t.lineHeight = { unit: 'PERCENT', value: 120 };
        t.fills = [{ type: 'SOLID', color: rgb(spec.color) }];
        frame.appendChild(t); t.x = spec.x; t.y = spec.baseline - spec.size;
        t.name = spec.text;
        // Fit long labels without cropping the frame; report font differences in handoff.
        const available = screen.width - spec.x - 12;
        if (t.width > available) { t.textAutoResize = 'HEIGHT'; t.resize(available, t.height); }
      }
      frames[screen.key] = frame;
      status('Created ' + (++count) + ' / ' + PROTOTYPE.screens.length + ' screens…');
    }
    let interactions = 0;
    for (const screen of PROTOTYPE.screens) {
      const source = frames[screen.key];
      for (const item of screen.links) {
        const target = frames[item.to];
        if (!target || source === target) throw new Error('Invalid route: ' + screen.key + ' → ' + item.to);
        const hit = figma.createRectangle();
        source.appendChild(hit); hit.name = 'Action · ' + item.label;
        hit.resize(item.w, item.h); hit.x = item.x; hit.y = item.y;
        hit.fills = [{ type: 'SOLID', color: { r: 1, g: 1, b: 1 }, opacity: 0 }];
        await hit.setReactionsAsync([{ trigger: { type: 'ON_CLICK' }, actions: [{ type: 'NODE', destinationId: target.id, navigation: 'NAVIGATE', transition: null, preserveScrollPosition: false }] }]);
        interactions++;
      }
    }
    page.flowStartingPoints = Object.entries(PROTOTYPE.starts).map(([name, key]) => ({ name, nodeId: frames[key].id }));
    // Read every reaction back from the actual Figma document, not the input JSON.
    const results = [], errors = [];
    for (const screen of PROTOTYPE.screens) {
      const source = frames[screen.key];
      const hits = source.children.filter(n => n.name.startsWith('Action · '));
      if (hits.length !== screen.links.length) errors.push(screen.key + ': hotspot count mismatch');
      screen.links.forEach((item, i) => {
        const hit = hits[i], reaction = hit && hit.reactions[0];
        const actions = reaction && (reaction.actions || (reaction.action ? [reaction.action] : []));
        const target = actions && actions[0];
        const passed = !!(hit && reaction && reaction.trigger.type === 'ON_CLICK' && target &&
          target.type === 'NODE' && target.navigation === 'NAVIGATE' && target.destinationId === frames[item.to].id &&
          hit.x === item.x && hit.y === item.y && hit.width === item.w && hit.height === item.h);
        results.push({screen:screen.key, index:i, label:item.label, to:item.to, hotspotId:hit && hit.id,
          destinationId:target && target.destinationId, passed});
        if (!passed) errors.push(screen.key + ': ' + item.label);
      });
      for (const text of source.children.filter(n => n.type === 'TEXT')) {
        if (!['Manrope', 'IBM Plex Sans'].includes(text.fontName.family)) errors.push(screen.key + ': wrong product font');
        if (text.x + text.width > source.width + 1 || text.y + text.height > source.height + 1) errors.push(screen.key + ': clipped text ' + text.name);
      }
    }
    if (errors.length) throw new Error('Native audit failed: ' + errors.slice(0, 8).join('; '));
    const audit = {version:PROTOTYPE.version, pageId:page.id, fileKey:figma.fileKey || null,
      verifiedAt:new Date().toISOString(), method:'Read-back of every created Figma reaction, target and hotspot bounds; this is not a claim of individual Present clicks.',
      screenCount:count, transitionCount:results.length, errors,
      screens:Object.fromEntries(Object.entries(frames).map(([key,frame])=>[key,frame.id])), results};
    figma.ui.postMessage({type:'audit', audit});
    figma.currentPage.selection = [frames.login];
    figma.viewport.scrollAndZoomIntoView([frames.login]);
    completedPage = page;
    status('Ready: ' + count + ' screens, ' + interactions + ' linked actions. Native reaction audit passed. Page ' + page.id + '. Save the report, then close and press Present.', true);
  } catch (error) {
    // Roll back only the page created by this execution. Existing user pages are untouched.
    await figma.setCurrentPageAsync(previousPage);
    if (page) page.remove();
    figma.ui.postMessage({ type: 'error', text: String(error && error.message || error) });
  } finally { running = false; }
};

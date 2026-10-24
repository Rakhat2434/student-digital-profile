// Contract tests for construction and recovery. This is not a Figma runtime emulator.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const payload = JSON.parse(fs.readFileSync(path.join(__dirname, 'prototype.json'), 'utf8'));
const byKey = new Map(payload.screens.map(s => [s.key, s]));
assert.equal(byKey.size, payload.screens.length);
const reached = new Set();
function visit(key) { if (reached.has(key)) return; reached.add(key); for (const l of byKey.get(key).links) { assert(byKey.has(l.to)); assert.notEqual(l.to, key); visit(l.to); } }
Object.values(payload.starts).forEach(visit);
assert.equal(reached.size, payload.screens.length, 'Unreachable screens');
for (const flow of [['login','overview','records','course','records'],['achievements','add','add-error','add-filled','saved','achievements-saved','new-detail','delete-confirm','achievements'],['teacher','grade','grade-options','grade-invalid','grade-options','grade-ready','grade-saved','teacher-saved'],['mobile','mobile-records','mobile-achievements','mobile']]) {
  for(let i=0;i<flow.length-1;i++) assert(byKey.get(flow[i]).links.some(l=>l.to===flow[i+1]), flow[i]+' → '+flow[i+1]);
}
assert(!byKey.get('grade-arman').links.some(l=>l.to.startsWith('grade-')), 'Other student cannot mutate Dana');
const completedFlows = [
  ['research','edit-achievement','edit-achievement-error','edit-achievement-ready','edit-achievement-saved','research-updated','achievements-updated'],
  ['edit-achievement','edit-achievement-discard','research'],
  ['admin','admin-create','admin-create-error','admin-create-ready','admin-create-saved','admin-accounts-saved','admin-created-detail'],
  ['admin-create','admin-create-duplicate','admin-create-ready'],
  ['admin-create','admin-create-discard','admin'],
  ['admin','admin-account-detail','admin-edit','admin-role-options','admin-edit-ready','admin-role-confirm','admin-edit-saved','admin-updated-detail'],
  ['admin-edit','admin-edit-error','admin-edit-ready'],
  ['admin-edit','admin-edit-discard','admin-account-detail'],
  ['admin-assignments','admin-assignment-edit','admin-assignment-error','admin-assignment-ready','admin-assignment-confirm','admin-assignment-saved','admin-assignment-list-saved','admin-assignment-remove','admin-assignment-removed','admin-assignments'],
  ['admin-assignment-edit','admin-assignment-conflict','admin-assignment-ready'],
  ['admin-assignment-edit','admin-assignment-discard','admin-assignments'],
  ['admin-policy','admin-grading-edit','admin-grading-error','admin-grading-ready','admin-grading-preview','admin-grading-confirm','admin-grading-saved','admin-grading-version','admin-policy'],
  ['admin-grading-edit','admin-grading-discard','admin-policy'],
];
for(const flow of completedFlows) for(let i=0;i<flow.length-1;i++) {
  assert(byKey.get(flow[i]).links.some(l=>l.to===flow[i+1]), flow[i]+' → '+flow[i+1]);
}
for(const screen of payload.screens) for(const l of screen.links) {
  const dest=byKey.get(l.to);
  if(screen.role==='Administrator' && l.to!=='login') assert.equal(dest.role,'Administrator','Admin must stay in its scoped demonstration');
  if(screen.role==='Student' && l.to!=='login') assert.equal(dest.role,'Student','Student must stay in its scoped demonstration');
}
assert(byKey.get('admin-grading-preview').svg.includes('3.73'));
assert(byKey.get('admin-assignment-ready').texts.some(t=>t.text==='Teacher Demo'),'Teacher selection must not be replaced with the signed-in administrator');

async function exercise(failAtReaction=false) {
  const nodes=[], messages=[]; let next=1;
  function node(type) {
    const n={id:String(next++),type,children:[],width:100,height:30,
      appendChild(child){ if(child.parent) child.parent.children=child.parent.children.filter(x=>x!==child); this.children.push(child);child.parent=this; },
      resize(w,h){this.width=w;this.height=h;},
      remove(){this.removed=true;},
      async setReactionsAsync(r){ if(failAtReaction)throw Error('injected failure'); this.reactions=r; }
    };nodes.push(n);return n;
  }
  const old=node('PAGE');
  const figma={currentPage:old,ui:{postMessage:m=>messages.push(m)},showUI(){},closePlugin(){},
    async listAvailableFontsAsync(){return ['Manrope','IBM Plex Sans'].flatMap(family=>['Regular','SemiBold'].map(style=>({fontName:{family,style}})));},
    async loadFontAsync(f){assert(f.family);},createPage:()=>node('PAGE'),async setCurrentPageAsync(p){this.currentPage=p;},
    createFrame:()=>node('FRAME'),createText:()=>{const t=node('TEXT');t.height=1;return t;},createRectangle:()=>node('RECTANGLE'),createNodeFromSvg:s=>{assert(s.startsWith('<svg'));return node('FRAME');},viewport:{scrollAndZoomIntoView(){}}
  };
  vm.runInNewContext(fs.readFileSync(path.join(__dirname,'code.js'),'utf8'),{figma,__html__:'<p>UI</p>'});
  await figma.ui.onmessage({type:'build'});
  if(failAtReaction) {
    assert.equal(figma.currentPage,old);assert(!old.removed);assert(nodes.filter(n=>n.type==='PAGE'&&n!==old).every(n=>n.removed));assert(messages.some(m=>m.type==='error'));
  } else {
    assert(!messages.some(m=>m.type==='error'),JSON.stringify(messages.filter(m=>m.type==='error')));
    assert.equal(figma.currentPage.children.length,payload.screens.length);
    assert.equal(nodes.filter(n=>n.reactions).length,payload.screens.reduce((n,s)=>n+s.links.length,0));
    assert.equal(figma.currentPage.flowStartingPoints.length,4);
    const pages=nodes.filter(n=>n.type==='PAGE').length;await figma.ui.onmessage({type:'build'});
    assert.equal(nodes.filter(n=>n.type==='PAGE').length,pages,'Second click must not duplicate');
    assert(messages.some(m=>m.done));
    assert(messages.some(m=>m.type==='audit'&&m.audit.transitionCount===payload.screens.reduce((n,s)=>n+s.links.length,0)&&m.audit.errors.length===0));
  }
}
(async()=>{await exercise();await exercise(true);console.log('PASS: route reachability, main flows, safe rollback, no duplicate build and complete reaction construction. Actual Figma execution remains unverified.');})().catch(e=>{console.error(e);process.exitCode=1;});

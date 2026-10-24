# SDP-7 · Design revision 02

Author: Aimaut Bolatkhanuly (`aimautb`) · 23 October 2026

**Status: local visual redesign prepared and reviewed. Not applied to the Figma file.** The Figma Starter MCP limit still blocks reads and writes. These boards are a concrete import package, not a claim that the existing 13-screen prototype was updated.

## Review the screens

| Screen | Vector artwork | Reviewed PNG |
| --- | --- | --- |
| Student overview | [SVG](01-overview.svg) | [PNG](01-overview.png) |
| Academic records | [SVG](02-academic-records.svg) | [PNG](02-academic-records.png) |
| Achievements | [SVG](03-achievements.svg) | [PNG](03-achievements.png) |
| Teacher workspace | [SVG](04-teacher-workspace.svg) | [PNG](04-teacher-workspace.png) |
| Mobile overview | [SVG](05-mobile-overview.svg) | [PNG](05-mobile-overview.png) |

## What changed

- A 232 px persistent sidebar gives the desktop workspace a stable hierarchy.
- A compact summary strip separates key numbers from a fully labelled 0–4 GPA chart.
- A dark profile panel balances the chart and keeps student context visible.
- Course rows have aligned numerical columns, course codes and explicit grades.
- Achievements use evidence-focused cards; the second card represents the previously demonstrated saved state.
- The teacher table retains course-scoped access, with distinct recorded and pending labels.
- Mobile uses course cards and a compact bottom navigation composition.

The existing slate/teal palette and academic scope are preserved. No ranking, predictive risk score or new production feature has been introduced. Current GPA remains `47 / 13 → 3.62`; historical points remain illustrative fixtures.

## Import into Figma

Open the existing Figma design, create a separate page named `SDP-7 · Revision 02`, then drag the five `.svg` files from this folder onto the canvas. Keep the original page until the replacement is reviewed. The SVGs contain vector shapes and text rather than flattened screenshots; Figma may outline text during import. Imported artwork does not automatically gain auto-layout, shared components or prototype reactions.

Once connector access is available, rebuild the approved layouts with native text, component instances and auto-layout, then reconnect the original journeys and verify them in Present. The original node ledger continues to describe revision 01 only.

## Verification and limits

All five SVGs were rendered to PNG with Sharp and visually inspected at desktop/mobile sizes. The overview table was tightened to keep all three rows within its panel; the final renders have no observed clipped labels or overlapping sections. XML structure, artboard dimensions and the absence of embedded raster images were checked. This is visual-artifact verification, not browser accessibility testing.

The boards are static: illustrated controls do not accept input or save data. The export renderer used available system font fallbacks; the font declarations retain Manrope and IBM Plex Sans as the intended Figma typefaces. Confirm installed fonts and typography when rebuilding native Figma layers. Contrast and runtime keyboard semantics remain implementation checks.

## Regenerate

`python build_design.py` regenerates the SVGs and palette snapshot using Python's standard library. `node render_previews.cjs` renders PNGs when the `sharp` package is available in the Node module search path. Sharp is a rendering tool, not an application dependency. Do not edit generated SVG/PNG files independently of the generator.

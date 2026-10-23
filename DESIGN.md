---
version: alpha
name: "Student Digital Profile"
description: "Semester-first academic records with visible calculation evidence"
colors:
  primary: "#176887"
  background: "#F2F5F8"
  surface: "#FFFFFF"
  text: "#142C42"
  muted: "#526779"
  subtle: "#E8F2F6"
  border: "#D9E2EA"
  success: "#216B52"
  danger: "#A73732"
typography:
  display:
    fontFamily: "Manrope, sans-serif"
  sans:
    fontFamily: "IBM Plex Sans, sans-serif"
rounded:
  DEFAULT: "0.75rem"
  control: "0.5rem"
spacing:
  section-gap: "1.5rem"
  desktop-padding: "2rem"
  mobile-padding: "1.25rem"
components:
  button: {}
  academic-table: {}
  semester-summary: {}
  field: {}
---

# Student Digital Profile Design System

## Revision 02 · local visual proposal

The user's redesign request is captured in [five reviewed vector boards](docs/ux/redesign/README.md). These introduce a 232 px desktop sidebar, a compact metric strip, a labelled GPA chart, a dark profile panel and clearer academic tables while retaining this palette. The mobile board uses a dark GPA panel and course cards. `docs/ux/redesign/build_design.py` owns the generated SVG geometry and palette snapshot for this local proposal. The existing Figma file still contains revision 01 because its Starter MCP limit blocks changes. Do not treat revision 02 geometry as already synchronized with Figma variables, components or prototype links.

## Overview

### Creative North Star

An academic record sheet with a clear semester narrative: a student should be able to trace every displayed indicator back to results. The signature panel pairs semester GPA with a readable progression, followed immediately by its source courses.

Audience: university students, assigned teachers and administrators. This is a product workspace for repeated academic review on laptops and phones. The supplied diploma documents establish a university context in Kazakhstan, but the product is intended to support adaptation to other institutions. Prototype language is English, consistent with repository documentation; the Proposal puts full multilingual support after MVP.

Keep navigation and data entry familiar. Avoid decorative AI imagery, unexplained rankings, public student cards, gradient hero sections and decorative statistics unrelated to the academic task. Do not derive a marketing identity from the fact that this is a diploma project.

Token ownership for this design-only stage: the Figma collection `SDP · Academic light` holds primitive and semantic colour variables; this document records the same intended values. `figma-state.json` maps semantic tokens to exact IDs. There is no runtime CSS or component implementation yet; runtime token export and drift enforcement belong to the future frontend implementation. Do not claim they already exist.

## Colors

Use cool canvas and white paper for layout, slate ink for text, teal for primary actions and the semester series. Muted text is still readable body/supporting information. Success and danger must include words; colour alone cannot encode status.

| Document token | Figma semantic token | Future CSS target |
| --- | --- | --- |
| primary | color/accent | `--sdp-accent` |
| background | color/canvas | `--sdp-canvas` |
| surface | color/paper | `--sdp-paper` |
| text | color/ink | `--sdp-ink` |
| muted | color/muted | `--sdp-muted` |
| subtle | color/soft | `--sdp-soft` |
| border | color/line | `--sdp-line` |
| success | color/success | `--sdp-success` |
| danger | color/danger | `--sdp-danger` |

This iteration defines light mode only. Dark mode must preserve semantic contrast if later added, rather than invert colours mechanically.

## Typography

Manrope SemiBold: page titles 32 px, section headings 21 px, GPA value 48 px. IBM Plex Sans Regular: body 16 px; Medium: labels 14 px. Line height is 140%. Loaded Figma font styles were checked against the available-font list before creation. Final rendered-font verification remains pending due to the tool limit.

Keep identifiers and numerical columns aligned. Use sentence case for actions and headings. Long course titles wrap; never truncate an academic result or an error explanation without a way to read it.

## Layout

Desktop frames: 1440 px, 32 px outer padding, 24 px between major sections. Mobile: 390 px, 20 px outer padding, 350 px content. Cards use 24 px padding on desktop, 16–20 px in compact views. Auto-layout owns related content. Frame height follows content.

On phones, transform course table rows into labelled course cards; retain course, grade, credits and points. Maintain ordinary document scrolling for forms. Future table containers may scroll internally without constraining sibling form height. At 768 px, test the transition to stacked summaries before implementation acceptance.

## Elevation & Depth

Use surface separation and spacing rather than shadows. Data panels do not float. Reserve elevation for future menus/dialogs only; no glass or blurred text backgrounds.

## Shapes

12 px content radius and 8 px action radius. Charts use simple strokes and labelled points. Avoid pill-shaped containers for large content and ornamental icon boxes.

## Components

### Foundational visual states

Default, selected and invalid examples appear in the prototype. Hover, keyboard focus, disabled, busy and read-only states are implementation requirements. Focus uses a clearly visible 2 px accent outline with offset; busy actions retain dimensions and an accessible status. Loading uses a labelled progress indicator. Full state rendering and runtime behaviour have not been validated.

### Buttons and actions

Reuse the Simple Design System button instances with project fill, typography and radius overrides. Library discovery found compatible button variants and label properties; layout containers and academic data composition are project-specific. Primary actions use accent fill; secondary navigation uses subtle fill. Visible labels state the action. Controls are at least 44 px high. Component sources remain library-owned; semantic fill overrides map to SDP variables.

### Navigation and data display

Role navigation keeps overview, records and achievements stable for students; teachers work within assignments. Mark the current destination as selected and avoid self-navigation. GPA must include semester and scale. Empty values are textual; zero is a real value. Every implemented chart requires a data-table alternative, units, periods and policy provenance.

### Forms and overlays

Persistent labels; inline errors with correction guidance; explicit save/cancel. The prototype has static fields, not working inputs. In implementation use shared field and feedback primitives, preserve values on failures, prevent duplicate submit and guard unsaved navigation. Native select/date controls are acceptable for MVP only if OS-owned popup behaviour is accepted; do not imitate an authored picker with an inert drawing.

### Iconography

Text labels carry primary navigation in this prototype. If icons are added later, use one consistent SVG family with accompanying labels; never use emoji as status controls.

### Motion

Prototype navigation uses immediate transitions. Future micro-interactions may use short opacity changes; respect reduced motion. Do not animate chart values in ways that obscure accurate readings.

### Content and data visualization

Use fictional demo records. Current GPA is 47/13 → 3.62; historical values are illustrative fixtures. Do not introduce AI scores or academic-risk thresholds without approved requirements. Dates and numeric formatting must follow the active locale in implementation.

## Do's and Don'ts

- **Do:** place source records close to the calculated indicator.
- **Do:** preserve labels, actions and semester context across desktop and mobile.
- **Don't:** imply real authentication, saving or permission enforcement in a static prototype.
- **Don't:** substitute a public student portfolio for the private academic workspace described in the Proposal.

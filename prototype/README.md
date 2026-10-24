# SDP-7 · Prototype handoff

[YouTrack task](https://student-digital-profile.youtrack.cloud/issue/SDP-7) · [Figma file](https://www.figma.com/design/hOhNtoHcIS5VW5UfHqD0fC)

The task description was checked in authenticated YouTrack on 23 October 2026. This directory provides the required prototype entry point and exported materials.

## Open and install

- [Interactive browser preview](../docs/ux/figma-prototype/preview.html): open the downloaded file in a browser; no server is required.
- [Figma installation instructions](../docs/ux/figma-prototype/README.md): import the local manifest in Figma Desktop and run the builder.
- [Manifest](../docs/ux/figma-prototype/manifest.json): keep its sibling `code.js` and `ui.html` files together.
- [UX specification](../docs/ux/SDP-7-ux-prototype.md), [design decisions](../DESIGN.md), [interaction contract](../UX-CONTRACT.md).
- `exports/`: five SVG design boards for review and import. The 41-state interactive package remains in `docs/ux/figma-prototype/` to avoid duplicating executable sources.

Revision 03 is installed on page 14:173. The [native student-flow verification](acceptance-review.md) records the inspected login-to-achievement-save journey. The package has 41 screens and 288 transitions; teacher, administrator and mobile checks in native Figma remain pending. The old node ledger describes revision 01.

## Acceptance checklist

| YouTrack criterion | Evidence | Remaining action |
| --- | --- | --- |
| Key scenarios represented | Student progress, achievements, teacher grade update, administrator scope and mobile journeys in the package | Run the journeys below in Figma Present |
| Main screens designed | Login, overview, records, profile, achievements, teacher workspace, administrator view | Inspect typography and clipping after font substitution |
| Navigation demonstrated | 288 predefined transitions; route and browser tests passed | Confirm native Figma hotspots |
| Consistent with requirements | UX specification maps requirements and permission boundaries | Team confirms scope decisions; admin editing and skills remain limited or deferred |
| Figma link and exports in prototype/ on GitHub | This README and exports | Publish the SDP-7 branch to the agreed remote |
| Reviewed by another team member | No independent review recorded | Obtain reviewer approval and record its link |

## Five-minute demonstration

1. Start at `login`, choose Student, open results and each course detail, then return.
2. Change period to the empty semester, demonstrate request failure and retry.
3. Open achievements, inspect a certificate, then add an achievement. Save the empty form to show validation, populate the preset, save, and inspect the updated list. Delete the new demo record through its confirmation.
4. Restart at login and choose Teacher. Edit Dana's grade, show invalid input, select B (3.00), save, and confirm GPA changes from 3.62 to 3.23. Other students must not open Dana's edit state.
5. Choose Administrator and inspect accounts and access policy. These views do not change real accounts.
6. Choose Mobile and navigate through overview, records, achievements and profile; sign out.

Inputs and saved states are scripted demonstration data. General navigation can reset a scenario. This is not real authentication, file uploading, persistent storage, or an authorization test.

## Team review record

- Reviewer: pending
- Date: pending
- Branch/commit reviewed: pending
- Figma page and Present link: revision 03, page 14:173; see acceptance-review.md
- Findings and resolutions: pending
- Approval: pending

Do not mark SDP-7 Done before publication, Figma verification and independent review are recorded.

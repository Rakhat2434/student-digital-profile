# SDP-7 · Prototype handoff

[YouTrack task](https://student-digital-profile.youtrack.cloud/issue/SDP-7) · [Figma file](https://www.figma.com/design/hOhNtoHcIS5VW5UfHqD0fC)

The task description was checked in authenticated YouTrack on 23 October 2026. This directory provides the required prototype entry point and exported materials.

## Open and install

- [Interactive browser preview](../docs/ux/figma-prototype/preview.html): open the downloaded file in a browser; no server is required.
- [Figma installation instructions](../docs/ux/figma-prototype/README.md): import the local manifest in Figma Desktop and run the builder.
- [Manifest](../docs/ux/figma-prototype/manifest.json): keep its sibling `code.js` and `ui.html` files together.
- [UX specification](../docs/ux/SDP-7-ux-prototype.md), [design decisions](../DESIGN.md), [interaction contract](../UX-CONTRACT.md).
- `exports/`: nine SVG design boards, including achievement editing, account creation, teacher assignment and grading-policy preview. The 85-state interactive package remains in `docs/ux/figma-prototype/` to avoid duplicating executable sources.

Revision 04 contains **85 screens and 686 transitions**. Every local hotspot was clicked without force and reached its declared destination. [Revision-04 evidence and open gates](revision-04-review.md) distinguishes local checks and independently observed Figma results. The last independently observed cloud page is revision 03 (`14:173`); revision 04 still needs installation, a verified page link and native audit report.

## Acceptance checklist

| YouTrack criterion | Evidence | Remaining action |
| --- | --- | --- |
| Key scenarios represented | Student progress and achievement editing; teacher grade update; administrator profiles, roles, assignments and grading versions; mobile journey | Verify installed revision 04 in Figma Present |
| Main screens designed | Login, profile, records, achievements, teacher workspace, admin lists/forms/confirmations and mobile views | Inspect native typography and clipping |
| Navigation demonstrated | 686 individual local hotspot clicks passed; builder reads back native reactions after installation | Obtain native audit report and verify critical Present journeys |
| Consistent with requirements | UX specification and revision-04 mapping; protected academic fields and versioned grading | Team confirms D-01 import and D-06 visibility decisions; advanced skills remain outside MVP |
| Figma link and exports in prototype/ on GitHub | This README and exports; existing PR #10 | Update branch with revision 04 and add its verified Figma link |
| Reviewed by another team member | No independent review recorded | Obtain reviewer approval and record its link |

## Five-minute demonstration

1. Start at `login`, choose Student, open results and each course detail, then return.
2. Change period to the empty semester, demonstrate request failure and retry.
3. Open achievements, inspect a certificate, then add an achievement. Save the empty form to show validation, populate the preset, save, and inspect the updated list. Delete the new demo record through its confirmation.
4. Restart at login and choose Teacher. Edit Dana's grade, show invalid input, select B (3.00), save, and confirm GPA changes from 3.62 to 3.23. Other students must not open Dana's edit state.
5. Open the existing Research presentation → Edit achievement → show empty-title validation → use revised sample → save → inspect the updated details and list. Test cancellation through Discard edits.
6. Choose Administrator → Create student profile → show required/duplicate-ID errors → use valid sample → save → inspect Mira's new profile. Edit Dana's metadata and role, then confirm the proposed change.
7. Open Assignments → Add assignment → test required fields and duplicate assignment → save a valid scoped assignment → remove it through confirmation. Existing grades remain unchanged.
8. Open Grading policy → create demo-v2 draft → show invalid 5.00 points → select valid 3.30 → preview GPA 3.73 → confirm → inspect the preserved policy versions. These are illustrative policies, not approved institutional rules.
9. Choose Mobile and navigate through overview, records, achievements and profile; sign out.

Inputs and saved states are scripted demonstration data. General navigation can reset a scenario. This is not real authentication, file uploading, persistent storage, or an authorization test.

## Team review record

- Reviewer: pending
- Date: pending
- Branch/commit reviewed: pending
- Figma page and Present link: revision 04 awaiting independently verified link; revision 03 is historical
- Findings and resolutions: pending
- Approval: pending

Do not mark SDP-7 Done before revision-04 publication, Figma verification and independent review are recorded.

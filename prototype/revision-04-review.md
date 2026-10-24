# SDP-7 · Revision 04 review

Updated 24 October 2026. This record supersedes revision-03 scope gaps in the [historical acceptance review](acceptance-review.md).

## Completed package

85 screens; 686 predefined transitions. The original student, teacher and mobile journeys are retained. Added:

| Scenario | Main screen keys | Demonstrated result |
| --- | --- | --- |
| Edit existing achievement · UC-05 / FR-08–09 | research → edit-achievement → edit-achievement-ready → edit-achievement-saved → research-updated / achievements-updated | Updated title; date and evidence preserved; empty-title validation and discard confirmation |
| Create student profile · UC-09 / FR-11, FR-15 | admin → admin-create → admin-create-ready → admin-create-saved → admin-accounts-saved / admin-created-detail | Unique DEMO-004; own-record Student role; required and duplicate-ID errors |
| Edit metadata / role · UC-09 / FR-02, FR-11, FR-15 | admin-account-detail → admin-edit → admin-role-options → admin-role-confirm → admin-edit-saved → admin-updated-detail | Explicit role-change confirmation; protected ID and academic results; no assigned-course access by default |
| Manage assignments · UC-10 / FR-11 | admin-assignments → admin-assignment-edit → admin-assignment-confirm → admin-assignment-saved → admin-assignment-list-saved | Course/group/term boundary, required and duplicate validation, removal confirmation, academic records preserved |
| Configure grading · UC-11 / FR-12 | admin-policy → admin-grading-edit → admin-grading-preview → admin-grading-confirm → admin-grading-saved → admin-grading-version | Range validation, draft/preview/activation, new policy version and preserved historical version |

The grading preview uses (20 + 16.50 + 12) / 13 = 3.73 with final half-up rounding. The previous demo-v1 fixture remains 47 / 13 = 3.62. These are synthetic policies; changing this prototype does not approve university grading rules.

## Verification evidence

| Surface | Result | Limit |
| --- | --- | --- |
| Route graph and builder contract | Passed: all screens reachable, role boundaries, added positive/validation/cancel journeys, reaction construction, rollback and duplicate-build protection | Test adapter does not emulate real Figma |
| Local browser preview | All 686 hotspots clicked individually without force; each reached the expected screen; no page errors or 430 px overflow | Local preview, not native Figma |
| Local visual review | Achievement editing, account list, teacher assignment and grading preview rendered; four new SVG exports supplied | Product fonts and actual native frame layout still need Figma inspection |
| Native builder read-back | Implemented: checks every actual reaction, destination ID, hotspot bounds, product font and frame text bounds; exports JSON | A check existing in code is not evidence that it executed successfully |
| Cloud revision 04 | Installation instructions supplied for the owner's existing Desktop plugin; installation pending | No revision-04 page link or report is available; the cloud editor still shows revision 03 |
| Native Present | Revision-03 student add/save is historical; teacher correction/save/list and mobile records/achievements/profile/logout passed on 24 October | Revision-04 student edit/admin/teacher/mobile journeys not yet independently verified |

The complete local click log is [browser-route-audit.json](../docs/ux/figma-prototype/browser-route-audit.json). It identifies every source, label and destination. Download `sdp7-native-route-audit-v04.json` from the completed Figma plugin to obtain the actual node ledger and native reaction results. No native result is fabricated from the input JSON.

## Installation and remaining work

Figma MCP returned its Starter-plan call limit. The in-app web editor also failed to load the plugin environment. The owner confirmed that Figma Desktop and the local builder are available. Import the manifest from the current team checkout if the existing plugin points to an older copy:

`D:/diploma/githubOfProject/secondgit/student-digital-profile/docs/ux/figma-prototype/manifest.json`

Run the builder, wait for Ready, download its verification report and share the created revision-04 page link. Existing pages are preserved. Once independently confirmed, record the native report and actual Present journeys here.

Remaining before task acceptance: native revision-04 confirmation and Present checks; agree D-01 import / D-06 teacher visibility with the team; independent teammate review. No real authentication, persistent account changes, file upload or backend permission tests are claimed. General navigation returns to the baseline scenario; saved outcomes live in explicit saved states.

The previous baseline was merged in PR #10 by Rakhat2434 at aef39b9; its team approval record is preserved in Prototype.md. Revision 04 needs a separate follow-up PR and review. No merge of revision 04 into main is authorised.

## Additional native revision-03 checks · 24 October

Actual clicks in Figma Present at 1600 × 1100, page `14:173`:

- Teacher: login `14:639` → assigned list `14:482` → grade `14:1763` → options `14:1816` → invalid 5.00 `14:1872` → options → valid B `14:1925` → saved/GPA 3.23 `14:2080` → updated list `14:2129` (Dana B; other rows preserved).
- Mobile: login → overview `14:571` → records `14:2416` → achievements `14:2432` → profile `14:2448` → logout/login `14:639`.

Figma's own bottom stepper initially intercepted a mobile-navigation click. Using Options → Hide UI removed that overlay; the product's Records/Achievements/Profile/Sign out paths then passed. This is a viewer-control interaction, not a claim that all 288 revision-03 routes were individually clicked in Figma. New revision-04 screens still need installation and native verification.

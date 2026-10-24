# SDP-7 · Acceptance Review

Source: [YouTrack SDP-7](https://student-digital-profile.youtrack.cloud/issue/SDP-7), read while authenticated on 23 October 2026.

## Current evidence

**Historical revision-03 record.** The current package and open verification gates are recorded in [revision-04-review.md](revision-04-review.md): 85 screens, 686 transitions, with the previously missing achievement editing and administrator workflows added. The native steps below describe only the older revision and must not be reused as revision-04 proof.

The current local package has 41 screens and 288 transitions. Every exported hotspot was clicked in the browser preview without forced clicks and reached its declared destination. Student validation/saving, teacher correction/saving and mobile navigation passed. This proves the browser package's routing, not the installed Figma file or backend behavior.

Revision 03 is installed and its student add/save journey was verified in Figma Present; see the native verification record below. The old node ledger describes revision 01 only.

## Task acceptance matrix

| YouTrack criterion | Evidence | Remaining gate |
| --- | --- | --- |
| Key scenarios represented | Student progress and achievements; teacher correction; administrator overview; mobile journey | Team reviews the limited admin coverage described below |
| Main screens designed | Login, overview, profile, records/charts, achievements, teacher workspace, admin and mobile views | Final visual inspection of the installed Figma revision |
| Navigation demonstrated | 288 successful individual hotspot clicks in the local preview | Verify native Figma reactions in Present |
| Consistent with requirements and Use Case Diagram | Mapping below, synthetic GPA fixtures, role boundaries | Resolve source conflicts and agree deferred workflows |
| Figma link and exports in GitHub prototype/ | README, SVG exports and this review document | Publish the correct SDP-7 branch |
| Reviewed by another team member | Review checklist below | Independent reviewer approval |

## Requirements and architecture traceability

Architecture identifiers refer to the UC table in `07-architecture.md` on `origin/SDP-6` at `9104c87`. Requirement identifiers refer to SDP-5. These are traceability references, not a claim that all use cases are implemented.

| Architecture use case | Requirements | Current screen keys | Coverage |
| --- | --- | --- | --- |
| UC-01: login/logout | FR-01 | login, profile, mobile-profile | Preset role selection and logout; no credential validation |
| UC-02: view profile | FR-03 | profile, overview, mobile-profile | Demonstrated with fictional data |
| UC-03: academic records | FR-04 | records, course, course-db, course-research | Demonstrated |
| UC-04: dashboard/trends | FR-06, FR-07 | overview, period, empty, error | Demonstrated; historical trend is illustrative |
| UC-05: achievements/certificates | FR-08, FR-09 | achievements, add, add-error, add-filled, saved, achievements-saved, new-detail, delete-confirm, certificate | Add, inspect and delete demonstrated; editing an existing record is not yet prototyped |
| UC-06: assigned students | FR-02, FR-10 | teacher, teacher-period, teacher-profile | Assigned-list demonstration; no backend permission checks |
| UC-07: update grades | FR-05 | grade, grade-options, grade-invalid, grade-ready, grade-saved, teacher-saved | Demonstrated for Dana; other students are inspection states |
| UC-08: teacher analysis | FR-10 | teacher-profile | Limited course context; broader visibility awaits decision D-06 |
| UC-09: accounts/roles | FR-11, FR-15 | admin, admin-policy | Read-only overview; account/profile creation and role editing not yet prototyped |
| UC-10: assignments | FR-11 | admin-policy | Scope explained; assignment editing not yet prototyped |
| UC-11: grading rules | FR-12 | admin-policy | Policy boundaries only; configuration editing not yet prototyped |
| UC-12: import | Deferred scope D-01 | None | Proposal defers import; architecture labels it MVP; team decision required |
| UC-13: GPA calculation | FR-06 | records, grade-saved | Preset 47/13 = 3.62 and 42/13 = 3.23; not runtime calculation |

Skills/competency screens are suggested conditionally in SDP-7 and are outside the current proposed MVP. Profile management consists of student achievement management and planned administrative metadata correction; students must not directly edit institutional IDs or academic results.

## Navigation structure

```text
Login / demonstration role selection
├── Student overview ↔ Records → Course details
│   ├── Period → Empty semester → Request error → Retry
│   ├── Achievements → Details / Evidence
│   │   ├── Add → Validation → Preset form → Saved → Updated list
│   │   └── New detail → Delete confirmation → Initial list
│   └── Profile → Sign out
├── Teacher → Assigned student → Grade options
│   └── Invalid grade → Correction → Saved result → Updated list
├── Administrator → Accounts / Access policy
└── Mobile overview ↔ Records ↔ Achievements ↔ Profile → Sign out
```

## Review record

- Reviewer : Reviewd by Rakhat

SDP-7 **Done**

## Installed Figma verification — 23 October 2026

The browser editor confirms page `SDP-7 · Interactive revision 03` at page ID `14:173`. The user supplied node `14:640`; Present resolved the login frame to `14:639`.

Verified by actual clicks in Figma Present at a 1600 × 1100 browser viewport:

| Step | Observed frame |
| --- | --- |
| Demo login | `14:639` |
| Continue as student | `14:174` |
| Achievements | `14:398` |
| Add achievement | `14:1285` |
| Save empty form → validation error | `14:1355` |
| Fill sample values | `14:1426` |
| Save achievement | `14:1548` |
| View saved list with new entry | `14:1599` |

These screens rendered without visible clipping in the inspected desktop viewport. This is a sampled native-Figma check; all 288 transitions were tested in the local browser preview, not individually in Figma. Teacher, admin and mobile Present verification remains pending.

[Verified revision-03 start](https://www.figma.com/proto/hOhNtoHcIS5VW5UfHqD0fC?node-id=14-639&page-id=14%3A173&starting-point-node-id=14%3A639)

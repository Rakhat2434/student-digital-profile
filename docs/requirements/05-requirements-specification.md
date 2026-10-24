# 05 · Requirements Specification

**Student Digital Profile Information System**

Author: Aimaut Bolatkhanuly (`aimautb`) · Frontend developer

Version: 1.1 · 24 October 2026 · **Draft for team and supervisor review**

Task: [SDP-5](https://student-digital-profile.youtrack.cloud/issue/SDP-5)

## 1. Purpose and evidence

The project is a web-based information system that combines student academic records, calculated indicators and selected achievements into one digital profile. Students inspect their progress; teachers maintain results for assigned courses; administrators manage accounts, assignments and grading configuration.

This is a requirements baseline, not a claim that the application is implemented. The authenticated SDP-5 description and acceptance criteria were verified on 23 October 2026. They require identified and prioritized requirements, measurable mandatory criteria, publication under docs/, and review by another team member. The specification is published in [PR #9](https://github.com/Rakhat2434/student-digital-profile/pull/9); independent team review and the recorded scope decisions remain pending.

| Source | Used for |
| --- | --- |
| `Project Proposal & Scope.docx`, sections 4–9 | Users, MVP boundary, configurable GPA, future enhancements, evaluation |
| `diploma_obosnovanie_команда_4.docx`, sections 1 and 4–5 | Diploma topic, individual contributions, wider data-processing and visualization objectives |
| SDP-1, `docs/project-proposal/01-proposal.md`, commit `5b34023` | Repository version of the proposal |
| `docs/technology-comparison/05-technology-comparison.md` on baseline `7e04f9e` | Selected technologies; implementation context, not additional feature approval |
| SDP-6, `07-architecture.md`, commit `9104c87` | Architecture and use-case identifiers; conflicts recorded below |

Private source documents are referenced by filename, not copied into Git. Contact details, academic records and other personal information from the justification are excluded.

### Decisions requiring confirmation

| ID | Difference or missing rule | Treatment in this specification | Decision owner |
| --- | --- | --- | --- |
| D-01 | Proposal makes CSV/Excel import a future enhancement; SDP-6 labels it MVP | Keep import outside the committed MVP until approved; synthetic seed data supports the demo | Team + supervisor |
| D-02 | Justification names an adviser; Proposal names a teacher | Specify the Proposal's teacher role. Do not grant adviser access until its permissions are defined | Supervisor + backend owner |
| D-03 | Damir is Data Engineer/backend in justification and Analyst/QA in Proposal | Record both responsibilities; final workload to be agreed in SDP-9 | Team |
| D-04 | Retakes, incomplete results, rounding and institution-specific grade mappings are unspecified | Use the explicitly labelled test policy in section 5; no claim that it is AITU policy | Supervisor + profile backend owner |
| D-05 | Certificate storage limits, retention and deletion policy are unspecified | Use synthetic attachments only; production upload/release needs a documented policy | Team + data owner |
| D-06 | Teacher profile visibility beyond own course records is ambiguous | Demo only own-course records. Wider profile/achievement visibility requires explicit approval | Supervisor + backend owner |

## 2. Scope

**MVP:** test-account login/logout; role-scoped access; basic student profile; courses, grades and credits; configurable GPA; semester visualizations; selected achievements/certificates; account, group, course and assignment administration.

**Later:** CSV/Excel import, external LMS integration, advanced competencies, project portfolios, attendance, extracurricular analytics, PDF export and full Kazakh/Russian/English localization. These are not acceptance dependencies for this baseline.

**Excluded:** native mobile apps, replacing an LMS, accessing university databases without authorization, automatic academic-risk decisions, public student profiles and AI recommendations.

## 3. Actors and permission boundaries

Students, teachers and administrators are direct users. The academic supervisor approves project scope and grading assumptions; the project team maintains requirements and implementation; the institution/data owner would authorize any future use of institutional records. These stakeholders are not additional application roles.

Priority definitions: **Must** is required for the proposed MVP; **Should** is a desirable enhancement that does not block the baseline; **Could** is optional future work. Deferred scope is not silently treated as mandatory.

| Capability | Student | Teacher | Administrator |
| --- | --- | --- | --- |
| View basic profile | Own only | Assigned student context | Administrative support context |
| View academic records | Own only | Own assigned courses/students | Administrative support context |
| Enter or edit grades | No | Assigned course enrolments only | Not implicitly granted by the admin role; explicit policy required |
| Manage achievements | Own only | No edit rights | Policy to be agreed; no automatic edit grant |
| Manage accounts, groups and assignments | No | No | Yes |
| Configure grading rules | No | No | Yes, with impact review |
| Read another student's data by changing an ID | No | Only within assignment scope | Only through explicitly authorized administrative operations |

Authorization must be enforced by the server on list, detail, aggregate and attachment endpoints. Hiding navigation is insufficient. Aggregates must not include students or courses outside the caller's scope. Ambiguous privileges remain denied until decided; role editing must never allow self-service privilege escalation.

## 4. Functional requirements and acceptance criteria

`Must` denotes the proposed MVP baseline. `Should` is a proposed quality enhancement. The detailed product acceptance checks below are authored for team review and implement the task-level requirement for measurable criteria.

| ID | Priority | Requirement | Observable acceptance criterion |
| --- | --- | --- | --- |
| FR-01 | Must | Authenticate test users and terminate sessions | Valid credentials open the correct role workspace; invalid credentials show a generic error; logout prevents subsequent protected reads |
| FR-02 | Must | Enforce role, ownership and assignment checks | Student A cannot read Student B; Teacher A cannot list or mutate unassigned records, including through direct API calls |
| FR-03 | Must | Display the digital profile | An authorized user sees student identifier, name, programme and group matching stored data; unavailable optional values show an explicit empty value |
| FR-04 | Must | Show academic records by semester | Each row includes course code/name, credits, result and status; changing the semester updates rows and semester indicators consistently |
| FR-05 | Must | Allow teachers to enter/update assigned results | A valid edit persists and updates dependent indicators; invalid grade/credits are rejected without changing stored data |
| FR-06 | Must | Calculate GPA using a versioned grading policy | The same records and policy produce the same GPA; the worked example and edge cases in section 5 pass |
| FR-07 | Must | Visualize academic progress | Charts label semester, scale and measure; every plotted value matches the accompanying data table; missing semesters are not plotted as zero |
| FR-08 | Must | Manage selected personal achievements | A student adds and edits their own title, category, date and description; another student cannot modify the record |
| FR-09 | Must | Associate certificate evidence with achievements | Authorized users can open the synthetic test evidence attached to the correct achievement; unauthorized access is refused |
| FR-10 | Must | Provide a teacher workspace | A teacher can filter their assigned students by group/course, open an allowed academic record and return with filters preserved |
| FR-11 | Must | Administer users and academic assignments | An administrator can manage test accounts, groups, courses and teacher assignments; a revoked assignment stops future access |
| FR-12 | Must | Configure grading rules | The configuration names scale/version and validates mappings; recalculation uses the recorded policy version, not an undocumented client formula |
| FR-13 | Must | Recover from empty and failed requests | Empty datasets offer an explanation; failures offer retry; form failures preserve entered values and do not claim successful saving |
| FR-14 | Should | Provide traceability for academic edits | Result changes record actor, time, previous value and new value; the UI can show when results were updated |
| FR-15 | Must | Create and maintain a student profile through authorized administration | Creating a test student account with a unique student ID creates exactly one linked profile. An authorized administrator can correct programme/group metadata; duplicate IDs and invalid references are rejected without partial writes. Students cannot change their institutional ID or academic results through profile fields. |

### Main use cases

| Flow | Preconditions and steps | Result / alternative |
| --- | --- | --- |
| UC-S1: understand progress | Student signs in → opens dashboard → changes semester → inspects records | Semester GPA and course rows agree; no results shows “No results for this semester” |
| UC-S2: add evidence | Student opens achievements → enters metadata and authorized test evidence → saves | New item appears once; failed save retains the form |
| UC-T1: update result | Teacher selects assigned course/student → edits result → validates → saves | Result and dependent GPA refresh; an invalid value leaves data unchanged |
| UC-A1: manage assignment | Administrator chooses teacher and course/group → reviews → saves | New scope applies on the next authorized request; failures preserve previous assignment |

## 5. Academic calculation contract

For eligible graded records, with numeric grade points `p_i` and positive credits `c_i`:

```text
GPA = sum(p_i × c_i) / sum(c_i)
```

Semester GPA includes records from the selected semester. Cumulative GPA uses eligible records across semesters under the selected policy. Never average already-rounded semester GPAs. The backend owns calculation; the frontend displays returned values and policy metadata.

### Synthetic demonstration policy — not an official university policy

Use a 0–4 point scale. For the sample only: A = 4.00, B = 3.00, C = 2.00, F = 0.00; each completed graded record has positive credits. Unassessed records are excluded and displayed as pending. Failed graded courses remain in the GPA denominator but do not count as earned credits. Round only the final displayed GPA to two decimal places, using half-up rounding for nonnegative values.

| Course | Credits | Result | Grade points | Weighted points |
| --- | ---: | --- | ---: | ---: |
| Software architecture | 5 | A | 4.00 | 20.00 |
| Database systems | 5 | B | 3.00 | 15.00 |
| Research methods | 3 | A | 4.00 | 12.00 |
| **Total** | **13** | | | **47.00** |

Expected semester GPA: `47 / 13 = 3.615384… → 3.62`. Earned credits: `13`. These values are reused in SDP-7.

| Check | Expected result |
| --- | --- |
| No eligible grades / zero denominator | GPA is `null`; UI shows “Not available”, never 0.00 |
| Zero or negative credits | Validation error; no persistence |
| Grade outside configured mapping | Validation error; no partial update |
| Repeated submission of the same result | One result for the enrolment; no duplicate contribution |
| Change Database systems from B to A | Weighted sum becomes 52; GPA becomes 4.00 |
| A failed 2-credit course is added | GPA becomes `47 / 15 = 3.13`; earned credits remain 13 |
| Pending 2-credit course is added | GPA remains 3.62; pending course is visible separately |
| Different policy version / retake | Follow an explicitly approved policy; flag unsupported test cases rather than guess |

## 6. Data requirements

| Entity | Minimum information | Integrity condition |
| --- | --- | --- |
| Account | Identifier, role, account status | Unique identity; credential material never returned in profile responses |
| Student profile | Student ID, account link, name, programme, group | One profile per student identity |
| Course and semester | Code, title, credits, academic period | Stable identifiers; positive graded credits |
| Enrolment / result | Student, course, semester, result/status | Unique enrolment result; grade fits selected policy |
| Teacher assignment | Teacher, course/group scope | Checked on every protected read/write |
| Grading policy | Version, mapping, eligibility and rounding rules | Identifiable version accompanies calculations |
| Achievement | Owner, title, category, date, description | Ownership checked; evidence access inherits owner scope |
| Certificate evidence | Achievement reference, storage reference, type | No public unrestricted file URL assumed |

Store raw grades and credits independently from derived indicators. Expose freshness and policy version with aggregates so the UI cannot silently combine old indicators and new rows. Seed all demonstrations with fictional students; do not reuse GPA or contact details from the supplied justification.

## 7. Non-functional requirements

The numerical targets below are **proposed test targets** to align with SDP-8, not measured results.

| ID | Priority | Requirement | Measurement / acceptance target |
| --- | --- | --- | --- |
| NFR-01 | Must | Security and privacy | All negative role/ownership cases in section 8 pass; no credentials, real student data or secrets committed |
| NFR-02 | Must | Calculation correctness | All approved GPA fixtures pass exactly before display rounding; chart/table reconciliation has zero mismatches |
| NFR-03 | Must | Performance | On a recorded local/demo environment with 1,000 synthetic students and 20 concurrent sessions, p95 profile/dashboard API response ≤ 1 s; record hardware, dataset and cache conditions |
| NFR-04 | Must | Usability | Proposed moderated test with 5 participants: at least 4 complete own-progress and result-inspection tasks without assistance; record completion time and errors |
| NFR-05 | Must | Accessibility | Target WCAG 2.2 AA; keyboard access, visible focus, labels, non-colour status and chart data alternatives; verify at implementation stage |
| NFR-06 | Must | Responsive presentation | Core student flow remains usable at 390, 768 and 1440 px; no page-wide overflow; tables may use a labelled internal scroll region |
| NFR-07 | Must | Reliability | Failed saves do not corrupt data; duplicate requests do not duplicate results; empty and unavailable values remain distinguishable from zero |
| NFR-08 | Must | Maintainability | At implementation review, every Must FR has at least one linked test case and API/UI owner; the documented setup succeeds in a clean supported environment. Record commands and results once runnable code exists |
| NFR-09 | Should | Scalability | With the same recorded hardware and query mix as NFR-03, compare 1,000 and 10,000 synthetic students at 20 concurrent sessions; target p95 dashboard response ≤ 2 s, zero cross-user leakage and no lost updates. Record query plans and bottlenecks; this is a proposed benchmark, not a measured capacity claim. |

## 8. Requirement-to-verification traceability

| Test ID | Requirements | Evidence to collect |
| --- | --- | --- |
| AT-01 | FR-01, FR-02, NFR-01 | Login/logout and direct-request authorization tests for each role |
| AT-02 | FR-03, FR-04, FR-15 | Create one account/profile, reject a duplicate ID, update authorized metadata, reject student edits to protected fields, and compare stored fixtures with profile/semester views |
| AT-03 | FR-05, FR-06, FR-12, NFR-02 | GPA fixtures, invalid-input rejection and recalculation after edit |
| AT-04 | FR-07, NFR-02, NFR-05 | Chart values versus table; keyboard and text alternative inspection |
| AT-05 | FR-08, FR-09, NFR-01 | Own achievement lifecycle and unauthorized attachment request |
| AT-06 | FR-10, FR-11 | Teacher scope before/after assignment change, preserved filters |
| AT-07 | FR-13, NFR-07 | Empty semester, disconnected request, rejected save and retry |
| AT-08 | NFR-03, NFR-09 | Reproducible performance report with p50/p95 and environment |
| AT-09 | NFR-04, NFR-05, NFR-06 | Moderated usability notes, responsive and accessibility checks |

## 9. Review checklist

- [x] Define project purpose, evidence, MVP and excluded scope.
- [x] Document functional requirements with stable identifiers and observable checks.
- [x] Specify calculation examples, invalid data and missing-data behaviour.
- [x] Record source conflicts and unapproved policies explicitly.
- [x] Read and reconcile the SDP-5 task-level YouTrack criteria.
- [ ] Resolve D-01–D-06 with the team/supervisor.
- [x] Publish this branch to the agreed GitHub repository under docs/; review continues in [PR #9](https://github.com/Rakhat2434/student-digital-profile/pull/9).
- [ ] Obtain review from another team member and record the review link.
- [ ] Agree NFR measurement targets with the owner of SDP-8.
- [ ] Validate requirements with representative students and teachers.

Completing this document does not close SDP-5 automatically. Approval and implementation verification remain separate steps.

## 10. SDP-5 task acceptance review

Checked against the authenticated YouTrack card on 23 October 2026.

| Task criterion | Evidence | Status |
| --- | --- | --- |
| Functional and non-functional requirements documented | Sections 4 and 7 | Prepared |
| Each requirement has a unique identifier and priority | FR-01–FR-15; NFR-01–NFR-09 | Prepared |
| Mandatory requirements have testable criteria | Requirement rows, GPA fixtures and AT-01–AT-09 | Prepared for review |
| Requirements align with project scope | Sections 1–2; D-01–D-06 explicitly identify unresolved source conflicts | Team agreement pending |
| Uploaded to GitHub under docs/ | docs/requirements/05-requirements-specification.md in [PR #9](https://github.com/Rakhat2434/student-digital-profile/pull/9) | Published |
| Reviewed by another team member | Reviewer name and review link not yet recorded | Pending |

Task completion concerns the reviewed specification. Passing production tests and completing a usability study are later implementation/evaluation activities, not evidence that has already been obtained. The independent reviewer must confirm the proposed scope and measurement targets before acceptance.

# SDP-7 · UX / Prototype

**Student Digital Profile Information System**

Author: Aimaut Bolatkhanuly (`aimautb`) · 23 October 2026

Status: **Editable prototype created; visual QA and stakeholder validation pending**

Task: [SDP-7](https://student-digital-profile.youtrack.cloud/issue/SDP-7)

## 1. Open the deliverable

**Revision 03:** [Local Figma prototype builder](figma-prototype/README.md) packages 41 screens and 288 linked actions. It is ready for local installation and includes a browser-tested interaction preview. The cloud Figma file has not been updated; Desktop execution and final Present verification remain pending.

**Revision 02:** [Five redesigned screens with SVG import files and reviewed PNGs](redesign/README.md). Prepared locally in response to the redesign request; the Figma file below remains revision 01 until connector editing is available.

- [Editable Figma design](https://www.figma.com/design/hOhNtoHcIS5VW5UfHqD0fC)
- [Student overview](https://www.figma.com/design/hOhNtoHcIS5VW5UfHqD0fC?node-id=4-993)
- [Student prototype start](https://www.figma.com/proto/hOhNtoHcIS5VW5UfHqD0fC?node-id=4-957)
- [Teacher prototype start](https://www.figma.com/proto/hOhNtoHcIS5VW5UfHqD0fC?node-id=4-1284)
- [Mobile overview](https://www.figma.com/design/hOhNtoHcIS5VW5UfHqD0fC?node-id=4-1546)
- [Design direction and tokens](../../DESIGN.md)
- [Behaviour and handoff contract](../../UX-CONTRACT.md)
- [Figma node ledger](figma-state.json)

The file contains native text, auto-layout frames, vector chart elements, button instances, colour variables and text styles. It is not a flattened screenshot. The creation call returned 13 screen frames and prototype navigation definitions. The subsequent structural read and screenshot request were blocked by the Figma Starter MCP call limit; therefore no final visual approval is claimed.

## 2. Product and scope

The interface helps a student answer: **What changed in my academic progress, and which course results explain it?** A teacher needs a short path from an assigned student to a valid result update. An administrator needs a clear view of account roles and assignment boundaries.

The two supplied DOCX files, the SDP-1 proposal and the SDP-4 technology comparison ground this design. Requirement IDs refer to `docs/requirements/SDP-5-requirements-specification.md` in the separate `SDP-5-requirements-specification` branch. That document is intentionally not duplicated into SDP-7.

The initial MVP includes authentication, profiles, course results, GPA, achievements and administration. Import, PDF export, advanced competencies, AI recommendations and external university integration are not presented as implemented features. Teacher/adviser terminology and broader profile visibility remain decisions for the team.

All names, IDs and academic values in the design are fictional fixtures. The UI uses English to match the repository's academic documentation. Full localization remains a future enhancement in the Proposal.

## 3. Design rationale

The visual reference is an academic record sheet made interactive: strong course labels, a semester-first hierarchy and a visible connection between a calculated number and its underlying records.

The signature is the **semester evidence panel**: GPA and earned credits sit alongside the semester progression; the course table follows immediately below. This keeps interpretation close to evidence. Avoid decorative rankings, unexplained risk scores and unrelated statistics.

Manrope gives headings a clear, compact voice; IBM Plex Sans supports dense records and form labels. Slate-blue text, cool paper surfaces and a restrained teal accent preserve a serious academic tone. Cards group related tasks; they do not turn every line of content into a separate box.

## 4. Screen inventory

| ID | Screen | Role / purpose | Requirements |
| --- | --- | --- | --- |
| S01 | Your academic record, in one place | Login entry and explicit demonstration role entries | FR-01 |
| S02 | A clearer view of your semester | Student identity, semester GPA, trend and source rows | FR-03, FR-04, FR-06, FR-07 |
| S03 | Academic records | Course/credit/grade table and transparent calculation | FR-04, FR-06 |
| S04 | Achievements with evidence | Existing certificate and entry to add flow | FR-08, FR-09 |
| S05 | Add achievement | Labelled fields, sample evidence, save/cancel | FR-08, FR-09 |
| S06 | Achievement saved | Explicit success feedback for the sample operation | FR-08, FR-13 |
| S07 | Your assigned students | Teacher's course-scoped student table | FR-02, FR-10 |
| S08 | Edit academic result | Invalid result, inline correction and cancellation | FR-05, FR-13 |
| S09 | Academic result saved | Confirmed example result and return path | FR-05, FR-06 |
| S10 | Accounts & assignments | Read-only administrative review of roles/scopes | FR-11, partial design coverage |
| S11 | No results for this semester | Missing results distinguished from a zero GPA | FR-07, FR-13 |
| S12 | Academic records are unavailable | Request failure, retry and safe navigation | FR-13 |
| S13 | My semester | 390 px mobile composition with course cards | NFR-06 |

Desktop frames are 1440 px wide with content-driven height; the mobile frame is 390 px. Screen names and exact node IDs are stored in `figma-state.json`.

## 5. Prototype walkthroughs

### Student: inspect progress

1. Start S01 and select **Sign in as student**.
2. On S02, inspect the current GPA and three graded courses.
3. Open **View academic records** to reach S03 and inspect the formula.
4. Return to the overview; select **Spring 2027 · no results** to reach S11.
5. Return to Autumn 2026. A missing semester must never be mistaken for zero performance.

### Student: add an achievement

1. Use **Achievements** to open S04.
2. Select **Add achievement** to open S05.
3. Review the prefilled fictional form; **Cancel** returns to S04.
4. **Save achievement** opens S06 with explicit success feedback.

### Teacher: recover from invalid input

1. Start S07 or select the teacher review entry on S01.
2. Open **Edit Dana’s result**.
3. S08 shows an invalid value of 5.00 and explains the permitted 0–4 range.
4. Select **Use A (4.00) and save** to see S09; return to assigned students.

### Error recovery and mobile review

Start the separate **Error recovery** flow at S12; **Try again** leads to S03. Use **Mobile overview** for S13. The mobile composition is an inspection frame, not a complete separate mobile journey.

### Prototype limits

The clickable prototype navigates predefined states. It does not authenticate, accept real typed values, upload files, calculate GPA or persist changes. S06 demonstrates a saved state; returning to S04 restores its initial sample list. Administrative changes and grading-policy editing are intentionally not wired, because their detailed policies require agreement. Loading, focus, hover and blocked-access behaviour are specified below but not all rendered as standalone Figma screens. Do not describe this as a working application or complete production flow coverage.

## 6. Content and calculation consistency

The current-semester fixture matches SDP-5:

| Course | Credits | Points | Contribution |
| --- | ---: | ---: | ---: |
| Software architecture | 5 | 4.00 | 20.00 |
| Database systems | 5 | 3.00 | 15.00 |
| Research methods | 3 | 4.00 | 12.00 |

`47 / 13 = 3.62` after display rounding; 13 earned credits and three graded courses. Historical trend points 3.10 and 3.35 are separately labelled illustrative test history, not computed from the three current rows. In implementation, replace all points with service responses and provide an accessible table for the full history.

No official institutional grading policy, academic-risk classification or student ranking is implied.

## 7. States and interaction handoff

| State | Required behaviour | Evidence now |
| --- | --- | --- |
| Loading | Keep the content region stable; show a labelled progress indicator | Specification only |
| Empty semester | Explain absence; show no numeric GPA; offer another period | S11 |
| Empty achievements | Explain what can be added; primary action adds an achievement | Specification only |
| No search results | Preserve query/filter; offer clear filters | Specification only |
| Request failure | Preserve navigation and input; offer retry without success feedback | S12 for records |
| Invalid field | Text error next to field; preserve values; focus first error on submit | S08 visual state; runtime focus pending |
| Saved | Name the result; return to the owning list with filters retained | S06, S09 predefined states |
| Unauthorized | Server rejects access; UI gives a safe return route without leaking details | Specification only |
| Unsaved form | Cancel returns safely; implementation warns when real edits would be lost | Static cancel links; runtime guard pending |

## 8. Usability review script

Use fictional data and ask participants to narrate their interpretation. Proposed sample: five people covering students and teaching/advising experience. Do not collect real academic records.

| Task | Success condition | Observation |
| --- | --- | --- |
| Explain the selected GPA | Finds the semester and connects 3.62 to its course results | Time, incorrect interpretation, assistance |
| Inspect an empty semester | States that results are missing, not failed | Misinterpretation count |
| Add a certificate entry | Finds the form and understands saved feedback | Navigation errors, unclear labels |
| Correct an invalid grade | Identifies the range error and safe correction path | Error comprehension |
| Read on a phone | Finds GPA and all three course results | Clipping, scrolling, touch clarity |

The proposed target is four of five participants completing the progress task without assistance. No participant sessions have been run; results must be added after testing rather than inferred from the design.

## 9. Review checklist and comment draft

- [x] Create an editable Figma file with 13 screens.
- [x] Add prototype paths for student and teacher tasks, error recovery and empty data.
- [x] Use the SDP-5 calculation fixture consistently.
- [x] Record visual tokens, behaviour rules and exact Figma IDs.
- [ ] Complete visual screenshot review after Figma tool access is available.
- [ ] Verify screen bounds, typography, prototype links and mobile composition in Figma Present.
- [ ] Review role permissions and remaining admin workflow with the team.
- [ ] Run participant sessions and reconcile the actual SDP-7 YouTrack acceptance criteria.

**Prepared review comment:** “SDP-7 adds the editable Student Digital Profile prototype, 13 screen states, student/teacher walkthroughs, a mobile overview and design/behaviour documentation. The sample GPA is aligned with SDP-5. Final visual QA is pending because the Figma Starter tool limit blocked the verification calls; administrative mutations and real data persistence are outside this prototype.”

This comment is a local draft for review; it has not been posted to GitHub or YouTrack.

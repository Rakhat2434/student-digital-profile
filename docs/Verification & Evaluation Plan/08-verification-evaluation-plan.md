# Verification and Evaluation Plan

**Project:** Student Digital Profile Information System
**YouTrack task:** SDP-8 — Verification & Evaluation Plan
**Status:** Draft for review (pre-defense 1)


---

## 1. Purpose and approach

This plan defines how the team will show that the system **meets its requirements** (verification) and **achieves the project aim** (evaluation): giving students and teachers a single, accurate and understandable view of academic progress over time.

- **Verification** answers "did we build the system right?" — every Must requirement is linked to at least one test with a pass/fail criterion.
- **Evaluation** answers "did we build the right system?" — the system is compared with the current approach (baseline) using measurable metrics with real users.

The plan follows the evaluation areas listed in the Project Proposal (Section 9): data accuracy, calculation correctness, visualization accuracy, access control, performance and usability. Use case IDs (UC-xx) refer to `docs/07-architecture.md`. Requirement IDs (FR-xx, NFR-xx) below are the planned IDs of `docs/06-requirements.md`; the traceability matrix (Section 8) will be updated when that document is merged.

## 2. Features under test

| # | Feature | Use cases | Priority | Owner |
|---|---|---|---|---|
| F1 | Authentication and role-based access control | UC-01, UC-06, UC-09 | Must | Rakhat |
| F2 | Digital profile (personal data, records, achievements, indicators) | UC-02, UC-08 | Must | Rakhat |
| F3 | Academic records and grade entry | UC-03, UC-07 | Must | Rakhat |
| F4 | GPA and indicator calculation with configurable grading rules | UC-11, UC-13 | Must | Rakhat / Damir |
| F5 | Data import from CSV/Excel (cleaning, validation) | UC-12 | Should | Damir |
| F6 | Dashboards and charts (GPA by semester, statistics) | UC-04, UC-08 | Must | Aimaut |
| F7 | Achievements and certificates management | UC-05 | Must | Rakhat / Aimaut |
| F8 | Administration of users, groups, courses, assignments | UC-09, UC-10 | Must | Rakhat |
| F9 | History of indicators over time (snapshots, trends) | UC-04, UC-13 | Must | Damir |

Out of scope for testing: features listed as future enhancements or out of scope in the proposal (mobile app, LMS integration, SSO, PDF export).

## 3. Testing methods

| Level / method | What it checks | Tools | Applied to | When |
|---|---|---|---|---|
| Unit tests | Calculation and validation logic in isolation | Jest (TypeScript), pytest (Python) | GPA formulas, grading rule conversion, Zod/Pydantic schemas, data cleaning functions | Every pull request |
| API / integration tests | Endpoints with a real test database | Jest + Supertest, pytest + FastAPI TestClient, Postman collection | All REST endpoints, Core Backend ↔ Data Processing Service ↔ PostgreSQL | Every pull request touching the backend |
| Access control tests | Each role can do only what is allowed | Automated API tests with test accounts of each role | F1 and every protected endpoint | Every pull request |
| End-to-end (E2E) tests | Main user scenarios through the browser | Playwright | Scenarios TS-01 … TS-10 | Before each milestone |
| Data accuracy check | Stored and displayed data equals the source data | SQL queries and scripts comparing DB with the source file / reference spreadsheet | F2, F3, F5, F6 | After each import and before each milestone |
| Performance tests | Response time and load | k6 (or Apache JMeter) | Dashboard, profile and grade endpoints | Before pre-defense 2 and final defense |
| Security checks | Common web vulnerabilities, secrets | OWASP ZAP baseline scan, `npm audit`, `pip-audit`, GitHub secret scanning | Whole application | Before each milestone |
| Usability evaluation | Ease of use and clarity | Moderated sessions, SUS questionnaire, task timing | Prototype (now), working system (later) | Prototype stage and before final defense |
| Code review | Quality and correctness of each change | GitHub pull requests, at least one reviewer | All changes | Continuously |

## 4. Test scenarios for key features

Test data: synthetic dataset (see Section 6). Expected results are pass/fail criteria.

| ID | Feature | Scenario | Steps (short) | Expected result |
|---|---|---|---|---|
| TS-01 | F1 | Login with valid and invalid credentials | Log in as student with correct password; then with wrong password | Correct → redirect to student dashboard; wrong → error message, no session created |
| TS-02 | F1 | Teacher cannot see students outside own courses | Log in as Teacher A; request profile of a student enrolled only with Teacher B (UI and direct API call) | UI does not list the student; API returns 403 |
| TS-03 | F1 | Student cannot edit grades or view other students | Log in as student; call `POST /api/grades` and `GET /api/students/{other_id}` | Both return 403; no data changed |
| TS-04 | F3, F4 | Teacher enters a grade and GPA is recalculated | Teacher enters grade for a 5-credit course; student opens dashboard | Grade saved; semester and cumulative GPA equal the reference value from the calculation spreadsheet (difference 0.00) |
| TS-05 | F4 | GPA calculation with configured grading rules | Run calculation for 30 reference students covering edge cases (no grades, retakes, failed course, 0-credit course, different credit sizes) | 30/30 results match the reference values to 2 decimal places |
| TS-06 | F4 | Change of grading rule | Admin changes the letter-to-points mapping; recalculation runs | All affected GPAs updated according to the new rule; previous snapshots remain unchanged in history |
| TS-07 | F5 | Import of a valid CSV/Excel file | Admin uploads file with 500 students × 8 courses | All valid rows imported; row count in DB equals file; import report shows 0 errors |
| TS-08 | F5 | Import of a file with errors | Upload file with duplicates, missing IDs, grade out of range, wrong column names | Invalid rows rejected and listed in the report with row number and reason; valid rows imported; no partial corrupt records |
| TS-09 | F6, F9 | Dashboard matches stored data | Open student dashboard; compare every chart value with DB query results | All GPA-by-semester points, totals and statistics equal the DB values |
| TS-10 | F7 | Add and view an achievement with certificate | Student adds achievement with PDF certificate; teacher opens profile | Achievement and file visible to the student and the assigned teacher; file type and size validated |
| TS-11 | F8 | Administrator manages users and assignments | Create teacher, assign to course, deactivate a user | Teacher sees students of the course; deactivated user cannot log in |
| TS-12 | F2 | Complete digital profile view | Open profile of a student with records, achievements and 4 semesters | Profile shows personal data, records, achievements, current GPA and trend for all 4 semesters |

## 5. Evaluation metrics

| ID | Area | Metric | How it is measured | Target |
|---|---|---|---|---|
| M1 | Calculation correctness | Share of GPA/indicator results equal to the reference calculation | Automated comparison on the reference set (TS-05) | 100 % (tolerance ±0.01) |
| M2 | Data accuracy | Share of imported records that match the source file | Script comparing source file and DB after import | 100 % of valid rows; 100 % of invalid rows reported |
| M3 | Visualization accuracy | Share of chart values that equal the DB values | Automated check of dashboard API vs SQL queries (TS-09) | 100 % |
| M4 | Access control | Unauthorised requests that succeed | Automated role matrix test: every role × every protected endpoint | 0 |
| M5 | Performance — response time | 95th percentile response time of dashboard and profile API | k6, 50 concurrent virtual users, 5 minutes | ≤ 1.0 s (p95) |
| M6 | Performance — page load | Time until the student dashboard is fully rendered | Lighthouse / Playwright timing, desktop, local network | ≤ 2.5 s |
| M7 | Reliability | Error rate under load | k6, same conditions as M5 | < 1 % failed requests |
| M8 | Usability | System Usability Scale (SUS) score | SUS questionnaire after test sessions, ≥ 10 participants (students and teachers) | ≥ 70 |
| M9 | Effectiveness vs baseline | Time to answer typical questions (see Section 7) | Timed tasks, same participants on baseline and on the system | At least 50 % less time than baseline |
| M10 | Effectiveness vs baseline | Task success rate | Share of tasks completed correctly without help | ≥ 90 % (baseline measured for comparison) |
| M11 | Test coverage | Line coverage of calculation and validation modules | Jest / pytest coverage report | ≥ 80 % for calculation and validation modules |
| M12 | Requirements coverage | Must requirements with at least one passed test | Traceability matrix (Section 8) | 100 % |

## 6. Testing conditions, resources and expected results

**Environments**

| Environment | Description |
|---|---|
| Local / CI | Docker Compose: Next.js app, FastAPI service, PostgreSQL 16 with a clean test database recreated for each run; GitHub Actions for unit and API tests |
| Staging (demo) | Deployed web app and data service with the synthetic dataset; used for E2E, performance and usability sessions |

**Test data**

- Synthetic dataset generated by a script: 500 students, 5 groups, 40 courses, 4 semesters, 10 teachers, 3 administrators, 300 achievements. No real personal data is used.
- Reference set of 30 students with GPA calculated manually in a spreadsheet by two team members independently (used for M1).
- Faulty import files with known errors (used for TS-08).
- Test accounts for every role.

**Measurement conditions**

- Performance: staging environment, database filled with the full synthetic dataset, 50 concurrent virtual users, 5-minute run, measured after a 1-minute warm-up; results reported as p50/p95 and error rate.
- Usability: sessions of 20–30 minutes, same task list for all participants, observer records time and errors; SUS filled immediately after the session.

**Resources**

| Resource | Responsible |
|---|---|
| Unit and API tests for the core backend | Rakhat |
| Data import tests, synthetic data generator, data accuracy scripts | Damir |
| E2E tests, dashboard checks, usability sessions | Aimaut |
| Test plan maintenance, traceability matrix, test reports | Damir (QA) |
| Participants for usability evaluation (≥ 10 students and teachers) | Whole team, agreed with supervisor |

**Expected results:** all scenarios TS-01 … TS-12 pass, metrics M1–M12 reach their targets, and the results are recorded in a test report (`docs/testing/test-report.md`) for each milestone.

## 7. Baseline for comparison

**Baseline:** the **current approach** used by students and advisors — looking up grades in the university's existing information system / LMS (transcript and journal pages) and calculating or tracking progress manually (for example, in a spreadsheet), with achievements and certificates kept separately (files, messengers, personal notes).

**Why this baseline:** the proposal states that student information is fragmented across several systems and has limited visualization (Section 3). The project aim is to replace this fragmented process with one profile, so the fairest comparison is the same tasks done the current way by the same users. A fully equivalent commercial digital-profile product is not available to the team for a controlled comparison; the feature comparison with existing systems is documented separately in the existing system comparison.

**Comparison tasks** (performed by each participant on the baseline and on the system, order alternated to reduce learning effects):

1. Find your cumulative GPA and the GPA of each semester.
2. Determine whether your GPA increased or decreased over the last two semesters.
3. List all your achievements and certificates for the last year.
4. (Teacher) Identify students in your course whose grades dropped below a threshold.

Measured for both: time per task (M9), success rate (M10), number of systems/screens used, and subjective clarity (SUS for the new system, short questionnaire for the baseline).

## 8. Verification of functional and non-functional requirements

Each requirement is verified by the method in the table and is considered **met** only when its linked tests pass. The matrix is kept in this document and updated in each pull request that adds tests.

**Functional requirements (planned IDs)**

| Requirement | Description | Verified by | Method |
|---|---|---|---|
| FR-01 | Users log in with their role | TS-01 | API, E2E |
| FR-02 | Access is restricted by role and course assignment | TS-02, TS-03, M4 | Access control tests |
| FR-03 | Teacher enters and updates grades | TS-04 | API, E2E |
| FR-04 | System calculates GPA using configurable rules | TS-05, TS-06, M1 | Unit, API |
| FR-05 | Student views digital profile | TS-12 | E2E |
| FR-06 | Dashboard shows GPA by semester and statistics | TS-09, M3 | API, data accuracy |
| FR-07 | Student manages achievements and certificates | TS-10 | API, E2E |
| FR-08 | Administrator manages users, groups, courses, assignments | TS-11 | API, E2E |
| FR-09 | Administrator imports data from CSV/Excel | TS-07, TS-08, M2 | Integration, data accuracy |
| FR-10 | System keeps history of indicators over time | TS-06, TS-09 | API, data accuracy |

**Non-functional requirements (planned IDs)**

| Requirement | Description | Verified by | Method |
|---|---|---|---|
| NFR-01 Performance | Dashboard/profile API p95 ≤ 1 s; page load ≤ 2.5 s | M5, M6, M7 | Load testing, Lighthouse |
| NFR-02 Security | Passwords hashed; all inputs validated; no secrets in repository; no high-severity findings | M4, OWASP ZAP, `npm audit`, `pip-audit`, secret scanning | Security checks |
| NFR-03 Data integrity | No invalid or duplicate records after import or grade entry | TS-07, TS-08, M2 | Integration, DB constraints review |
| NFR-04 Usability | SUS ≥ 70; task success ≥ 90 % | M8, M10 | Usability evaluation |
| NFR-05 Maintainability | Calculation/validation coverage ≥ 80 %; every change reviewed in a PR | M11, PR history | Coverage report, code review |
| NFR-06 Portability / adaptability | Grading rules changed without code changes | TS-06 | API, E2E |
| NFR-07 Compatibility | Works in current Chrome, Firefox, Edge on desktop and in mobile browser width | E2E run in 3 browsers | Playwright |

**Acceptance of the project aim:** the aim is considered achieved when all Must requirements are verified (M12 = 100 %), correctness metrics M1–M4 are met, and the evaluation shows improvement over the baseline (M9, M10) with SUS ≥ 70.

## 9. Schedule

| Milestone | Verification activities |
|---|---|
| Pre-defense 1 (24 Oct 2026) | This plan; usability walkthrough of the Figma prototype with 3–5 users |
| Pre-defense 2 | Unit and API tests for F1–F4 in CI; reference GPA set (M1); first access-control matrix (M4) |
| Final pre-defense | All scenarios TS-01 … TS-12; performance (M5–M7); security checks; usability and baseline comparison (M8–M10); final test report |

## 10. Risks to verification

| Risk | Mitigation |
|---|---|
| Not enough participants for usability evaluation | Recruit early through the supervisor and student groups; minimum 10, otherwise report results as indicative |
| Reference GPA values contain mistakes | Calculated independently by two people and reconciled before use |
| Grading rules of the university are unclear | Confirm the rules with the supervisor/registrar; keep rules configurable and documented |
| Staging environment differs from production | Document hardware and configuration with every performance result |

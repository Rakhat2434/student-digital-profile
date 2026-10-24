# Project Management and Risk Assessment

**Project:** Student Digital Profile Information System  
**YouTrack Task:** SDP-9 — Project Management and Risks  
**Author:** Damir Ushkempir  
**Date:** 2026-10-2ң

## 1. Project Overview

Student Digital Profile is a proposed web-based information system for organizing students' academic records, displaying progress across semesters, and presenting selected achievements. The intended users are students, teachers, and system administrators. The initial concept includes role-based access, course and grade records, a configurable GPA calculation, academic dashboards, and certificates.

The project is currently at **Pre-Defense 1**. The focus of this stage is to establish a clear problem statement, review existing research and systems, define requirements, justify technical choices, and present an initial design. A working production system, university database integration, and completed user evaluation are not deliverables of this stage.

The project is being developed by three students with guidance from academic supervisor Gulzhan Soltan. Because detailed requirements from an external university client are not available, the design is based on the agreed project concept and uses synthetic or otherwise authorized data in later prototyping.

This document describes how the first-stage work is divided among the team, how the individual documents relate to one another, and which risks could affect the quality of the Pre-Defense 1 submission.

## 2. Team and Task Distribution

The project has three complementary responsibilities. Rakhat Dosmagambetov focuses on backend and technical design. Aimaut Bolatkhanuly is responsible for frontend and interface design. Damir Ushkempir works on system analysis, research, documentation consistency, and quality assurance. Gulzhan Soltan provides academic supervision and feedback.

The YouTrack board groups the first-stage work into eleven tasks.

| Task   | Deliverable                          | Assigned member      |
| ------ | ------------------------------------ | -------------------- |
| SDP-1  | Project Proposal & Scope             | Damir Ushkempir      |
| SDP-2  | Literature Review                    | Damir Ushkempir      |
| SDP-3  | Existing Systems Comparison          | Damir Ushkempir      |
| SDP-4  | Technology Comparison                | Rakhat Dosmagambetov |
| SDP-5  | Requirements Specification           | Aimaut Bolatkhanuly  |
| SDP-6  | System Architecture & Diagrams       | Rakhat Dosmagambetov |
| SDP-7  | UX / Prototype                       | Aimaut Bolatkhanuly  |
| SDP-8  | Verification & Evaluation Plan       | Rakhat Dosmagambetov |
| SDP-9  | Project Management & Risks           | Damir Ushkempir      |
| SDP-10 | GitHub README & Repository Structure | Aimaut Bolatkhanuly  |
| SDP-11 | Supervisor Feedback                  | Rakhat Dosmagambetov |

The assignments reflect the shared YouTrack screenshot. The account `dlsk8946` is associated here with Rakhat based on his authorship of the SDP-4 and SDP-6 files. All three members contribute comments to documents outside their primary assignments when those documents affect their own work.

This division keeps the project manageable for a small team. It also allows the research, interface planning, and architecture work to develop in parallel while the shared project scope provides a common reference.

## 3. Work Plan for Pre-Defense 1

The first-stage work is organized into four connected areas. These are **documentation checkpoints for Pre-Defense 1**, not deadlines for implementing or deploying the entire system.

| Area                                          | YouTrack tasks             | Main output for Pre-Defense 1                                                                       |
| --------------------------------------------- | -------------------------- | --------------------------------------------------------------------------------------------------- |
| Project definition and background             | SDP-1, SDP-2, SDP-3        | A defined problem, justified project scope, literature review, and comparison with existing systems |
| Requirements and design                       | SDP-4, SDP-5, SDP-6, SDP-7 | Requirements, technology rationale, architecture diagrams, and early interface designs              |
| Quality and project planning                  | SDP-8, SDP-9               | Evaluation approach, responsibility allocation, document dependencies, and risk assessment          |
| Submission organization and academic feedback | SDP-10, SDP-11             | A navigable repository and a record of the supervisor's comments and related revisions              |

The research documents explain why the proposed system is relevant. The requirements and architecture documents explain what the system should do and how it is expected to be structured. The UX materials communicate the intended experience to a non-technical audience. The evaluation plan describes how the completed system can later be assessed. SDP-9 connects these contributions at the project level.

Some documents can be prepared at the same time. For example, the Literature Review and Existing Systems Comparison do not depend on completed database or interface designs. Other materials need closer coordination. Requirements, use cases, interface screens, and planned tests describe the same functions from different perspectives, so differences between them can create confusion during the defense.

The project calendar is maintained in YouTrack. No calendar dates are reproduced here because the provided task list did not include confirmed deadlines. Progress for this stage is assessed through the quality and consistency of the documents rather than through unverified implementation milestones.

## 4. Dependencies and Document Consistency

Several relationships are especially important for Pre-Defense 1.

| Connected work                  | Relationship                                                                     | Relevance to the submission                                                                                   |
| ------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| SDP-1 → SDP-5                   | The proposal establishes the intended MVP and user roles                         | Requirements remain within the declared project scope                                                         |
| SDP-2 and SDP-3 → SDP-1 / SDP-5 | Research and system comparisons support the problem statement and design choices | The project's value is argued with evidence, without claiming that competing systems lack unverified features |
| SDP-4 → SDP-6                   | Selected technologies are reflected in the architecture                          | The components and diagrams match the documented stack                                                        |
| SDP-5 ↔ SDP-6                   | Requirements are represented by system use cases and components                  | The main functions are not described differently across files                                                 |
| SDP-5 ↔ SDP-7                   | Role permissions and user needs shape the interface prototype                    | Student, Teacher, and Admin interactions remain consistent                                                    |
| SDP-5 and SDP-6 → SDP-8         | Requirements and use cases provide the basis for planned verification            | Later tests can be traced to specific system functions                                                        |
| SDP-11 → relevant documents     | Supervisor feedback may clarify the scope or expected deliverables               | Important revisions are reflected consistently across the submission                                          |

The technology choices in SDP-4 are Next.js with React and TypeScript, Next.js Route Handlers, a Python FastAPI/Pandas processing service, PostgreSQL, and Apache ECharts. SDP-6 uses the same general structure. This gives the technical sections a consistent starting point.

One issue needs particular attention. In SDP-1, CSV/Excel import appears among possible future enhancements. SDP-6 also shows a file-import use case within the initial system design. This does not prevent presentation of the architecture, but the intended scope should be explained consistently. A basic method of loading synthetic demonstration data is different from delivering a complete user-facing import feature.

The GPA feature presents a second design boundary. Both the proposal and architecture support calculation from grades and credits under configurable rules. The precise grading scale depends on an institutional policy and is not established by the research documents. At Pre-Defense 1, it is reasonable to explain the planned calculation method and note the need to document the selected conversion rules before implementation.

## 5. Project Coordination and Traceability

YouTrack provides the task list, ownership, and progress information. GitHub holds the project documents, diagrams, and their revision history. These two tools cover different parts of the same work. A task describes the intended contribution, while its repository changes show what was actually prepared.

The team uses the `SDP-n` issue number in relevant branch names, commit messages, and Pull Request descriptions. This makes it possible to relate a document to its YouTrack task and reviewer feedback. The repository README, owned under SDP-10, brings the separate documents together for readers of the project.

For the first defense, the important evidence is the existence of the relevant document, its consistency with the project scope, and any review outcome. An uploaded file or an individual commit does not by itself establish that a task has passed review. The official task state remains the one recorded in YouTrack.

Academic feedback is handled through SDP-11. Its role is to keep the supervisor's comments connected to the changes made in the proposal, requirements, architecture, or other related documents. This is particularly useful when one decision affects several contributors.

## 6. Risk Assessment for Pre-Defense 1

The following register concentrates on the research and design stage. Risks related to running a production service, deployment capacity, and operational security will become more important during later development and are not treated as current Pre-Defense 1 milestones.

Each risk is assessed using **Probability (P)** and **Impact (I)** on a five-point scale, where 1 means low and 5 means very high. The risk score is calculated as `P × I`. Scores from 1 to 5 are Low, 6 to 11 are Medium, 12 to 19 are High, and 20 to 25 are Critical. These are qualitative planning estimates rather than measured probabilities.

| ID   | Risk                                                                                           |   P |   I |        Score | Responsible member | Mitigation                                                                                                             |
| ---- | ---------------------------------------------------------------------------------------------- | --: | --: | -----------: | ------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| R-01 | MVP boundaries differ between the proposal and architecture, particularly for CSV/Excel import |   4 |   4 |  **16 High** | Damir              | Compare scope statements and record one agreed interpretation in the related documents                                 |
| R-02 | Requirements, diagrams, and UX materials describe different behavior for the same user role    |   3 |   4 |  **12 High** | Aimaut             | Cross-check the main user scenarios against the requirements and use cases                                             |
| R-03 | Supervisor feedback arrives after major documentation decisions have been made                 |   3 |   4 |  **12 High** | Rakhat             | Keep the assumptions visible in the relevant documents and track feedback through SDP-11                               |
| R-04 | Sources in the literature review or system comparison do not adequately support a claim        |   3 |   4 |  **12 High** | Damir              | Use verifiable scientific publications and official product documentation, with careful wording for uncertain features |
| R-05 | The selected technology stack is described inconsistently across technical documents           |   3 |   3 | **9 Medium** | Rakhat             | Align the SDP-4 decisions with SDP-6 component descriptions and diagrams                                               |
| R-06 | Documents are committed but remain unreviewed or contain contradictory information             |   4 |   3 |  **12 High** | Damir              | Track review evidence and compare related sections before accepting a document                                         |
| R-07 | Coursework and other commitments reduce the time available to complete first-stage tasks       |   3 |   3 | **9 Medium** | Damir              | Prioritize the agreed Pre-Defense 1 deliverables and redistribute review effort when necessary                         |
| R-08 | The GPA formula is presented without a clearly defined grading scale                           |   3 |   3 | **9 Medium** | Rakhat             | Separate the general weighted-average method from institution-specific conversion rules                                |
| R-09 | The project is presented as depending on real university records that the team cannot access   |   2 |   3 | **6 Medium** | Damir              | State the synthetic-data constraint consistently in the proposal, architecture, and evaluation plan                    |
| R-10 | The UX prototype does not clearly reflect the permissions of all three roles                   |   3 |   3 | **9 Medium** | Aimaut             | Compare the designed screens with Student, Teacher, and Admin use cases                                                |

The highest risks concern consistency between documents and the quality of the evidence used to justify the system. These issues matter directly to Pre-Defense 1 because the submission is primarily assessed through the clarity and credibility of the proposed design.

## 7. Pre-Defense 1 Evaluation Focus

At this stage, project quality is reflected in the submitted materials. The review concerns the following areas.

| Area                  | Evidence in the project package                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------------- |
| Scope clarity         | A consistent MVP and a clear distinction between current features and future enhancements                     |
| Research foundation   | Scientific literature with verifiable references and a reasoned comparison of related systems                 |
| Requirements          | Defined users, functional expectations, constraints, and traceable use cases                                  |
| Technical design      | Technology choices supported by SDP-4 and consistent architecture diagrams in SDP-6                           |
| User experience       | Prototype screens that reflect the intended Student, Teacher, and Admin workflows                             |
| Verification approach | A plan for evaluating correctness, access permissions, visualization accuracy, and usability at a later stage |
| Project organization  | Identifiable task ownership, relationships between documents, and the risk register in this report            |

The planned verification in SDP-8 is distinct from completed testing. No claim is made that the system has already passed GPA, authorization, performance, or usability tests. Those results will belong to subsequent development and evaluation stages.

## 8. Conclusion

Pre-Defense 1 establishes the foundation for Student Digital Profile before full implementation begins. The team's eleven YouTrack tasks cover project definition, research, design, evaluation planning, repository organization, and supervisor feedback. Work is shared across backend, frontend, and system-analysis responsibilities, with related documents connected through a common MVP scope.

The main management concern at this stage is not deployment speed. It is whether the separate contributions describe one coherent and well-supported system. The risk assessment therefore focuses on scope differences, source quality, requirements alignment, and timely review. Resolving these issues will give the team a clearer basis for development after the first defense.

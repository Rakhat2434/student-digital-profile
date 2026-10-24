# Existing Systems Comparison

**Project:** Student Digital Profile Information System  
**YouTrack Task:** SDP-3 — Existing Systems Comparison  
**Author:** Damir Ushkempir  
**Date:** 2026-10-23

---

## 1. Introduction

The proposed Student Digital Profile Information System aims to bring together selected academic records, automated academic indicators, achievements, and visualizations in a single web interface. Before designing the system, it is important to examine existing solutions and establish which functions are already supported by available products.

This comparison reviews five real-world education systems: **Ellucian Banner Student, Moodle LMS, Canvas LMS, Mahara ePortfolio, and Digication ePortfolio**. These systems were selected because they represent three relevant categories: student information systems (SIS), learning management systems (LMS), and electronic portfolio platforms. Comparing these categories helps identify both useful approaches and potential limitations without assuming that every product has the same purpose.

The analysis uses **nine consistent criteria** based on the proposed project's scope. Evidence is drawn primarily from official product documentation, vendor materials, and institutional support documentation. Availability can depend on product edition, configuration, enabled modules, institutional policies, and integrations.

## 2. Overview of Selected Systems

### 2.1. Ellucian Banner Student

**Category:** Student Information System (SIS)  
**Website:** https://www.ellucian.com/

Ellucian Banner Student supports university student administration, including student records, registration, grades, student and advisor self-service, and academic progress. Banner Self-Service describes a consolidated student profile, grade viewing, faculty grade entry, and degree-progress features [1]. An institutional support guide also documents grade views, GPA summaries, and course-credit information [2].

**Relevance:** Banner is the closest of the selected systems to the proposed project's formal academic-record and GPA components.

**Consideration:** Banner is a comprehensive institutional system. Its extensive administrative scope is broader than the planned initial Student Digital Profile MVP. A lack of portfolio emphasis in the reviewed materials should **not** be interpreted as proof that portfolio functionality is impossible within the broader Ellucian ecosystem.

### 2.2. Moodle LMS

**Category:** Learning Management System (LMS)  
**Website:** https://moodle.org/

Moodle focuses on online teaching and learning. Each course has a gradebook, and teachers can enter grades. Moodle also supports competencies, course-completion tracking, badges, reports, and learning analytics [3], [4], [13]. Portfolio export is possible when an administrator enables the relevant portfolio functionality and plugins [12]. Moodle provides web services for integration with other systems [14].

**Relevance:** Moodle offers ideas for teacher-managed grade entry, progress tracking, and competency-related data.

**Consideration:** The reviewed Moodle documentation mainly describes course-level learning information rather than a standalone institution-wide student profile with a configurable cumulative GPA and semester-by-semester GPA charts. Course completion views should not be conflated with visual analysis of institutional academic performance. Portfolio export is not equivalent to a built-in longitudinal project portfolio; additional plugins, integrations, or customization may address these needs.

### 2.3. Canvas LMS

**Category:** Learning Management System (LMS)  
**Website:** https://www.instructure.com/canvas

Canvas provides course grades and learning analytics. Its instructor documentation describes interactive charts and tables for grades, activity, submissions, and individual student performance [5]. Course Outcomes can be used to track learning mastery [15], and Canvas supports SIS imports through a documented API [17]. Digital badges can be enabled through the related Parchment Digital Badges service [16].

**Relevance:** Canvas is especially useful as a reference for academic dashboards and teacher-facing performance analytics.

**Consideration:** Course grade scales in an LMS should not automatically be treated as equivalent to institution-wide cumulative GPA based on all credited courses. The course-centered analytics and related badges/portfolio products are not evidence of a single standard cross-semester profile available in every deployment.

### 2.4. Mahara ePortfolio

**Category:** Electronic Portfolio Platform  
**Website:** https://mahara.org/

Mahara allows learners to create portfolios with reusable content and share selected pages and collections. Its résumé functions include education history, skills, achievements, certificates, and supporting files [7]. Access to portfolio pages can be managed by sharing permissions, and Mahara supports connections to learning systems through LTI and web services [8], [9].

**Relevance:** Mahara provides a strong example of student-owned achievements and skills presentation.

**Consideration:** The reviewed portfolio documentation does not establish Mahara as a conventional university gradebook, an institutional GPA-calculation system, or a tool for automatically charting academic grades over semesters. Mahara's résumé can display self-described skills, but this alone does not establish formal institution-wide competency assessment [7]. Its main emphasis is student-selected evidence and reflection.

### 2.5. Digication ePortfolio

**Category:** Electronic Portfolio Platform  
**Website:** https://www.digication.com/

Digication supports portfolios containing students' work, reflections, and evidence of learning across courses and years [10]. It also advertises LMS/SIS integrations, single sign-on, API access, and role-based access controls [11].

**Relevance:** Digication provides examples of a long-term digital record of student projects, experiences, and accomplishments.

**Consideration:** The vendor describes grade transfer and synchronization with an LMS [11], but that does not establish teacher entry of formal academic grades directly in Digication, or a standard built-in institution-wide GPA engine. The reviewed materials do not separately verify a dedicated certificate register or academic-grade trend charts. They primarily describe portfolio and reflective-learning workflows.

## 3. Comparison Criteria and Evaluation Method

The following **nine criteria** were chosen based on the proposed project's initial and future functional requirements:

1. **Consolidated student academic profile:** A single view combining important student and academic information.
2. **Teacher-managed academic grades:** Ability for authorized teaching staff to enter or manage academic results.
3. **Institutional GPA and credits:** Availability of institution-level GPA and credit information, not merely a course grading scale.
4. **Academic progress visualization:** Charts, dashboards, or visual progress views of academic results. The table differentiates course-completion and course-grade views from institution-wide GPA trends.
5. **Skills and competencies:** Representation of student skills, learning outcomes, or competencies.
6. **Achievements and certificates:** Recording or presenting awards, badges, certificates, or related evidence.
7. **Student project portfolio:** Collection and presentation of student projects or learning artifacts.
8. **Controlled access and sharing:** Role permissions or user-controlled visibility of relevant information.
9. **External system integration:** Documented methods for connecting other educational systems or services.

**Evaluation labels:**

- **Supported:** Clearly documented within the reviewed system's functionality.
- **Partial / contextual:** Supported at a different scope (e.g., per course rather than institution-wide), through a related product/module, or in a limited form.
- **Not verified:** The reviewed references do not clearly establish the requested functionality as a standard feature. This does **not** mean the feature cannot exist.

These labels are **qualitative judgments**, not measured product scores or evidence that a feature works identically across installations.

## 4. Comparative Analysis Table

| Comparison criterion                 | Ellucian Banner Student | Moodle LMS           | Canvas LMS           | Mahara ePortfolio    | Digication ePortfolio |
| ------------------------------------ | ----------------------- | -------------------- | -------------------- | -------------------- | --------------------- |
| 1. Consolidated academic profile     | **Supported**           | Partial / contextual | Partial / contextual | Partial / contextual | Partial / contextual  |
| 2. Teacher-managed grades            | **Supported**           | **Supported**        | **Supported**        | Not verified         | Not verified          |
| 3. Institution-level GPA and credits | **Supported**           | Not verified         | Not verified         | Not verified         | Not verified          |
| 4. Academic progress visualization   | Partial / contextual    | Partial / contextual | **Supported**        | Not verified         | Not verified          |
| 5. Skills and competencies           | Not verified            | **Supported**        | **Supported**        | **Supported**        | Partial / contextual  |
| 6. Achievements and certificates     | Not verified            | Partial / contextual | Partial / contextual | **Supported**        | Partial / contextual  |
| 7. Student project portfolio         | Not verified            | Partial / contextual | Partial / contextual | **Supported**        | **Supported**         |
| 8. Controlled access and sharing     | **Supported**           | **Supported**        | **Supported**        | **Supported**        | **Supported**         |
| 9. External system integration       | **Supported**           | **Supported**        | **Supported**        | **Supported**        | **Supported**         |

**Evidence for the table:** Banner academic records, student profile and GPA [1], [2]; Moodle grades, course progress, skills, badges, optional portfolio export and web services [3], [4], [12]–[14]; Canvas course-grade analytics, outcomes, legacy portfolio guidance, related digital badges and SIS API [5], [6], [15]–[17]; Mahara résumé, sharing and integration [7]–[9]; Digication portfolio and integration functionality [10], [11].

### Evidence Qualification Notes

- **Course-level versus institutional indicators:** Moodle completion reports and Canvas course-grade charts are useful references, but neither should be cited as proof of a standard institution-wide, credit-weighted cumulative GPA dashboard [3], [5], [13].
- **Moodle portfolios:** The documented portfolio capability concerns export to enabled portfolio plugins or external destinations; it does not on its own establish an integrated student project portfolio [12].
- **Canvas achievements:** Badge functionality described in the additional reference uses the related Parchment Digital Badges service, so the matrix retains a contextual assessment [16].
- **Mahara skills:** Skills can be documented in the résumé; the sources do not confirm that all skills are assessed against a formal competency framework [7].
- **Digication grades and certificates:** Grade synchronization with an LMS is supported by vendor materials, but independent direct teacher grade entry, a formal GPA engine, and a structured certificate register are not established by the reviewed sources [10], [11].

### 4.1. Interpretation of Key Results

**Academic information and grades.** Banner is designed for institution-level records and provides the strongest match for student profiles, GPA summaries, academic credits, and faculty grade entry among the selected sources [1], [2]. Moodle and Canvas clearly support course grades but should not be assumed to calculate an institution-wide cumulative GPA without an SIS connection or additional development [3], [5].

**Progress visualization.** Moodle provides course completion and reporting views, while Canvas explicitly documents interactive performance charts at course level [3], [5], [13]. Banner offers academic-progress and advising views; however, this review does not establish the same type of configurable charts planned for the proposed MVP [1], [2]. The reviewed Mahara and Digication references describe evidence and reflection rather than automatic charting of academic grade trends [7], [10].

**Skills, achievements, and portfolios.** Mahara documents skills, awards, certificates and evidence attachments [7]; Digication documents longitudinal portfolios and reflections, but the reviewed sources do not establish a dedicated certificate register [10]. Moodle supports formal competencies and achievement badges, with optional portfolio-export facilities [3], [4], [12]. Canvas has outcomes and related digital badges through Parchment Digital Badges [15], [16].

**Roles and interoperability.** All five platforms document some form of role control, sharing, or integration. Moodle offers web services, Canvas documents SIS imports, Mahara supports LTI and web services, and Digication advertises LMS/SIS integrations [9], [11], [14], [17]. However, academic-record access, course membership, and user-controlled portfolio sharing are not identical security models [1], [3], [7]–[9], [11].

## 5. Limitations and Opportunities Relevant to the Proposed System

The comparison identifies **differences in primary emphasis**, rather than proving that existing systems are inadequate:

- **SIS-oriented approach:** Banner provides authoritative academic records and administrative functions. For a small student-profile prototype, the proposed team can concentrate on a narrower set of academic and visualization workflows instead of reproducing an entire SIS.
- **LMS-oriented approach:** Moodle and Canvas offer course-centered teaching, grades, analytics, and outcomes. The proposed system can focus on an aggregated, cross-semester student profile, provided that appropriate academic data are available.
- **ePortfolio-oriented approach:** Mahara and Digication emphasize student-owned artifacts, achievements, and reflection. The proposed system can connect selected portfolio information with automatically calculated academic indicators.

The opportunity for the proposed project is therefore a **focused combination of academic profile management, configurable GPA calculation, selected achievements, and accessible progress dashboards** within one MVP. This is a proposed design direction, **not a proven claim of superiority** over the reviewed products.

## 6. Justification of the Proposed Student Digital Profile System

The proposed system will use a **web-based, modular design** suitable for a three-member development team. It is not intended to replace Moodle, Canvas, or an enterprise SIS. Rather, its initial purpose is to demonstrate a coherent digital profile experience with core academic functions.

The initial MVP is planned to include:

- User authentication and three roles: student, teacher, and administrator.
- Basic student profile and academic information.
- Teacher-managed grades for assigned students.
- Storage of course credits and configurable grade-conversion rules.
- Automatic calculation of selected academic indicators, including GPA.
- Charts presenting academic results and changes over semesters.
- Selected student achievements and certificate records.

Because official university data and APIs are not currently available, the first version will use synthetic or otherwise authorized test data. More advanced competencies, portfolios, attendance, multilingual support, and external integrations may be added later, depending on time and supervisor feedback.

The **expected design benefit** is an understandable, centralized presentation of selected student information. Whether the proposed application improves accuracy, task completion time, or usability must be tested; it cannot be established by a feature comparison alone.

## 7. Conclusion

The five selected systems demonstrate complementary approaches to digital student information. Ellucian Banner concentrates on institution-level academic records and student administration. Moodle and Canvas concentrate on teaching, course grades, learning outcomes, and analytics. Mahara and Digication concentrate on electronic portfolios and evidence of student development.

This comparison supports the decision to investigate a focused Student Digital Profile Information System that combines essential academic data and visual summaries with selected student achievements. The proposed project will prioritize a realistic MVP, and its effectiveness will be evaluated through testing rather than assumed from the comparison.

## 8. References

The following sources support the analysis. Product documentation describes available functionality; it should not be confused with peer-reviewed academic literature. Scientific publications will be reviewed separately under **SDP-2 — Literature Review**.

1. **Ellucian.** _Learn More About Ellucian Banner Self-Service_. Official vendor brochure. https://www.ellucian.com/assets/en/brochure/brochure-learn-more-about-ellucian-banner-self-service.pdf
2. **Farmingdale State College IT Support.** _Banner 9 Self Service for Students — OASIS_. Institutional guide illustrating student profiles, credits, grades and GPA summary. https://support.farmingdale.edu/TDClient/277/Portal/KB/Article/10768/Banner-9-Self-Service-for-Students-OASIS
3. **Moodle Documentation.** _Tracking Progress_. https://docs.moodle.org/503/en/Tracking_progress
4. **Moodle Documentation.** _Badges_. https://docs.moodle.org/503/en/Badges
5. **Instructure Community.** _How do I view Course Analytics for a student in a course?_ (updated July 2026). https://community.instructure.com/en/kb/articles/660626-how-do-i-view-course-analytics-for-a-student-in-a-course
6. **Instructure Community.** _What are ePortfolios?_ (updated September 2026; contains notice of December 2026 retirement). https://community.instructure.com/en/kb/articles/662752-what-are-eportfolios
7. **Mahara.** _Mahara 26.04 Manual: Résumé_ (education, achievements, certificates, goals and skills). https://manual.mahara.org/en/26.04/content/resume.html
8. **Mahara.** _Mahara 26.04 Manual: Shared by Me_. https://manual.mahara.org/en/26.04/portfolio/share.html
9. **Mahara.** _Mahara 26.04 Manual: Introduction_ (LTI and integration). https://manual.mahara.org/en/26.04/intro/introduction.html
10. **Digication Help Desk.** _Why Use Digication: Faculty_ (portfolio and reflection; updated June 2026). https://support.digication.com/hc/en-us/articles/51550060702235-Why-use-Digication-Faculty
11. **Digication.** _Seamless Integrations_. https://www.digication.com/community/integrations
12. **Moodle Documentation.** _Managing Portfolios_ (configuration and enabled portfolio plugins). https://docs.moodle.org/503/en/Managing_portfolios
13. **Moodle Documentation.** _Course Completion_ (course-level progress and reporting). https://docs.moodle.org/503/en/Course_completion
14. **Moodle Documentation.** _Web Services_ (connections to external systems). https://docs.moodle.org/503/en/Web_services
15. **Instructure Community.** _How do I use the course Outcomes page in Improved Outcomes Management?_ https://community.instructure.com/en/kb/articles/660936-how-do-i-use-the-course-outcomes-page-in-improved-outcomes-management
16. **Instructure Community.** _How do I use Parchment Digital Badges Pathways in a Canvas course?_ https://community.instructure.com/en/kb/articles/663756-how-do-i-use-parchment-digital-badges-pathways-in-a-canvas-course
17. **Instructure Developer Documentation.** _SIS Imports API_ (Canvas integrations). https://developerdocs.instructure.com/services/canvas/resources/sis_imports

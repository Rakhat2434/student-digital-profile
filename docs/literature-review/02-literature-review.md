# Literature Review

**Project:** Student Digital Profile Information System  
**YouTrack task:** SDP-2 — Literature Review  
**Author:** Damir Ushkempir (System Analyst / QA)  
**Date:** 2026-10-23

---

## 1. Introduction

The Student Digital Profile project proposes a web-based information system for organizing selected student information, managing academic records, automatically calculating grade point averages (GPA) from grades and course credits, visualizing progress across semesters, and presenting achievements and certificates. It is intended as a focused, adaptable prototype, not as a replacement for a university student information system (SIS) or learning management system (LMS).

This review examines scientific research on electronic portfolios, learning analytics, student-facing dashboards, university use of educational data, and the ethical treatment of student information. It complements **SDP-3 — Existing Systems Comparison**, which examines Ellucian Banner, Moodle, Canvas, Mahara, and Digication through product documentation. Product documentation establishes features; the scholarly literature provides research evidence, theoretical arguments, and methodological limitations.

Four questions guide the review:

1. What educational purposes and limitations of electronic portfolios have been demonstrated?
2. What is known about the design, interpretation, use, and effectiveness of student-facing dashboards?
3. What challenges affect the aggregation and deployment of educational information in universities?
4. Which privacy and evaluation principles apply to a student digital profile prototype?

## 2. Review Method and Evidence Boundaries

This is a **structured narrative review**, not a claim of an exhaustive systematic review or PRISMA study. Targeted searches in October 2026 used combinations of _ePortfolio_, _electronic portfolio_, _higher education_, _student profile_, _learning analytics_, _learning dashboard_, _academic performance_, _student success_, _privacy_, and _consent_. Bibliographic information and central claims were checked against journal/publisher pages, university research repositories, the journal's own material, or ERIC. DOI links are provided where verified.

Publications were selected if they concerned university portfolios, dashboards, institutional deployment, or privacy; contributed an empirical investigation, scholarly synthesis, or ethical/conceptual analysis; and were available as scholarly journal or peer-reviewed conference publications. The set contains **16 scholarly publications**, including **15 with verified DOI identifiers** and one journal paper linked to its ERIC record. Product documentation is not counted here as scientific evidence. Both accessible full text and publisher abstracts were used; data from paywalled studies were not independently reanalyzed. Findings are therefore interpreted conservatively.

The review includes 16 scholarly publications. This selection brings together empirical studies, systematic reviews, and conceptual analyses to evaluate the evidence for the proposed system and its limitations.

## 3. Critical Synthesis of Research

### 3.1. Electronic portfolios: evidence, skills, and reflection

An ePortfolio can store achievements, projects, and certificates, but it can also support reflection on learning. These purposes should not be conflated. Bryant and Chittum [1] found that discussions of ePortfolio effectiveness frequently mix descriptions of technologies, users' favorable perceptions, and actual student outcomes. The presence of a portfolio therefore does not, by itself, demonstrate improved academic performance.

Beckers, Dolmans, and Van Merriënboer [2] synthesized 17 studies on ePortfolios and self-directed learning. They identified conditions such as curricular integration, regular teacher coaching, scaffolding, and portfolio activities that support planning and self-evaluation. Cheng and Chau [3], studying 26 undergraduates over three months, reported positive associations between self-regulated learning strategies and portfolio achievement. Because that was a small correlational study, it does not demonstrate that portfolio use causes self-regulation.

López-Crespo and colleagues [4] implemented an ePortfolio using **Mahara** in a university course. Among 73 active student participants, portfolio performance correlated with conventional assessments, and the researchers reported increased self-efficacy after a semester. The pre/post questionnaire subset was smaller, and participants selected an assessment route. These factors restrict causal interpretation and transferability.

**Relevance to the proposed system.** The Student Digital Profile MVP will present selected achievements and certificates with titles, dates, descriptions, and supporting evidence. Self-entered claims will be distinguished from institutionally verified results. Advanced portfolio reflection, formal competencies, and project showcases are reserved for later development. The evaluation focuses on accurate representation and usable workflows rather than untested learning gains.

### 3.2. Learning analytics: useful dashboards require explanation and evaluation

Learning dashboards aggregate indicators so learners and teachers can interpret educational activity. Schwendimann and colleagues [5] analyzed 55 dashboard studies and emphasized the need for longitudinal investigation and comparisons of different designs. Bodily and Verbert [6] reviewed 93 student-facing reporting studies and identified weaknesses in usability assessment, justification of design choices, and measurement of real effects. These reviews suggest that dashboard adoption and educational benefit cannot be assumed from the existence of charts.

Bodily and colleagues [7] evaluated deployed student-facing dashboards through focus groups and a perceptions survey. Although many participants found them useful, only about one-quarter returned more than once. Positive first impressions and sustained use are therefore different outcomes.

Broader reviews offer a cautious picture. Viberg and colleagues [8] analyzed 252 studies and found limited evidence for several commonly anticipated benefits of learning analytics. Matcha and colleagues [9] found that dashboards were frequently insufficiently connected to self-regulated learning theory or tested for learning impact. Ifenthaler and Yau [10] synthesized 46 studies of analytics for university study success, reporting promising methods but diverse designs and contexts. Paulsen and Lindsay [11] identified an emerging movement toward student-focused dashboards while noting that descriptive monitoring remains common. Jivet and colleagues [12] likewise stressed the importance of pedagogically justified feedback and evaluation.

**Relevance to the proposed system.** The dashboard will display semester and cumulative GPA, course credits, contributing grades, and academic trends. Explanatory labels, rounding conventions, grading rules, and treatment of missing data will support correct interpretation. The MVP uses descriptive visualizations, without AI predictions or at-risk modeling. Evaluation will measure users' ability to interpret the dashboard rather than assume that chart use increases grades.

### 3.3. Educational information systems and institutional integration

Student data may originate in an SIS, an LMS, registrar exports, or student-maintained artifacts. These sources differ in authority, update cycles, and access rights. Tsai and colleagues [13] consulted managers from 83 higher education institutions in 24 European countries using mixed methods. They found that learning analytics initiatives were often limited in scale, with relatively little student engagement and limited institution-wide policy or evaluation. This strengthens the argument for explicit stakeholder involvement and manageable implementation scope.

Studies of institutional analytics [8], [10], [13] also show that findings depend heavily on local education processes and data quality. For the proposed GPA feature, a credit-weighted aggregate is meaningful only when the institution's grade conversion, repeated-course handling, missing grades, and rounding policies are specified. **No universal grading policy is established by the papers in this review.**

**Relevance to the proposed system.** The MVP uses synthetic or otherwise authorized data, consistent with SDP-1, and distinguishes institution-controlled grades from student-contributed achievements. Future LMS/SIS or SSO integration would require authorization, compatible data mappings, and security review. The prototype does not depend on access to official university databases.

### 3.4. Privacy and access control

Educational analytics may involve identifiable and sensitive information. Slade and Prinsloo [14] analyzed consent, transparency, surveillance, and institutional power. Pardo and Siemens [15] connected analytics with trust, accountability, and practical privacy principles. Jones [16] examined autonomy when universities aggregate student profiles and educational activity, proposing transparency and stronger preference controls. These articles provide ethical frameworks, not certificates of implementation security.

**Relevance to the proposed system.** The three roles follow least-privilege access: students view their own records, teachers access assigned students, and administrators manage authorized system functions. Certificate access is kept separate from private academic transcripts. Testing covers authorization boundaries and accidental disclosure using synthetic student records.

## 4. Comparative Research Matrix

The matrix differentiates methods, findings, limitations, and design relevance. A limitation is a boundary on interpretation, not evidence that the study lacks value.

| Source / topic                                   | Approach; methods or data                                                   | Reported finding / contribution                                                        | Limitations and caution                                      | Relevance to Student Digital Profile                            |
| ------------------------------------------------ | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------- |
| **[1] Bryant & Chittum (2013)** — ePortfolio     | Critical synthesis of portfolio scholarship                                 | Descriptive claims and user perceptions often outnumber demonstrated learning outcomes | No universal effect estimate                                 | Avoid unsupported educational-benefit claims                    |
| **[2] Beckers et al. (2016)** — ePortfolio       | Systematic review, 17 included studies                                      | Coaching, integration, and scaffolding influence self-directed learning support        | Heterogeneous settings and interventions                     | Use structured evidence; guided reflection as later enhancement |
| **[3] Cheng & Chau (2013)** — ePortfolio         | Correlational study; 26 undergraduates                                      | Self-regulation strategies associated with ePortfolio achievement                      | Small, context-specific sample; no causation                 | Keep skills/reflection distinct from GPA data                   |
| **[4] López-Crespo et al. (2022)** — Mahara      | Semester study; 73 active students, assessment and pre/post survey measures | Associations with conventional performance; reported increase in self-efficacy         | Single course; self-selection; smaller matched survey sample | Achievements and evidence workflow; no assumed learning gain    |
| **[5] Schwendimann et al. (2017)** — dashboards  | Systematic review, 55 papers                                                | Dashboard designs varied and long-term evaluations were needed                         | Earlier research often exploratory                           | Test GPA-chart comprehension and trends                         |
| **[6] Bodily & Verbert (2017)** — dashboards     | Review, 93 studies                                                          | Insufficient usability, design, and effects evidence in many systems                   | Studies differ greatly in methods                            | Include user-centered testing                                   |
| **[7] Bodily et al. (2018)** — dashboards        | Deployment, focus groups, student perceptions survey                        | Favorable perceptions but low repeated usage                                           | One deployment context; usage not grade improvement          | Separate usability, engagement, and outcome measures            |
| **[8] Viberg et al. (2018)** — analytics         | Review, 252 publications                                                    | Limited evidence for several predicted educational benefits                            | Inconsistent definitions and designs                         | Make measured, modest project claims                            |
| **[9] Matcha et al. (2020)** — dashboards        | Systematic review using self-regulated learning framework                   | Many dashboards lack actionable, theory-grounded feedback and strong evaluation        | Inherits weaknesses of included research                     | Explain metrics; test interpretation                            |
| **[10] Ifenthaler & Yau (2020)** — study success | Systematic review, 46 key studies                                           | Analytics can support study success in varied conditions                               | Intervention and context heterogeneity                       | Define evaluation metrics before implementation                 |
| **[11] Paulsen & Lindsay (2024)** — dashboards   | Systematic review of learner-facing dashboards                              | Shift toward student-focused designs, though monitoring remains prevalent              | Trends do not establish causation                            | Design simple, goal-oriented visuals                            |
| **[12] Jivet et al. (2018)** — evaluation        | Peer-reviewed conference analysis                                           | Feedback and comparisons need learning-theory and evaluation rationale                 | Guidance is not a trial of our system                        | Justify indicator and chart selection                           |
| **[13] Tsai et al. (2020)** — institutions       | Mixed-methods consultations, 83 institutions / 24 countries                 | Scale, governance, and student participation were barriers                             | European context; self-selection                             | Keep integrations future-facing and involve users               |
| **[14] Slade & Prinsloo (2013)** — ethics        | Sociocritical conceptual analysis                                           | Consent, privacy, transparency, and power matter                                       | Does not validate implementation                             | Access-control and disclosure rules                             |
| **[15] Pardo & Siemens (2014)** — ethics         | Conceptual synthesis of privacy principles                                  | Trust, accountability, and transparency are intertwined                                | No evaluation of specific RBAC code                          | Define privacy and security checks                              |
| **[16] Jones (2019)** — consent                  | Conceptual analysis and proposed model                                      | Aggregated identifiable profiles create autonomy concerns                              | Proposed model is not our tested architecture                | Minimize and explain data exposure                              |

## 5. Research Gap and Justification

The selected literature treats three connected but distinct concerns. Portfolios can present evidence and reflection, though benefits depend on pedagogy and participation [1]–[4]. Dashboards can represent learner data, but usability, sustained use, and improved outcomes require measurement [5]–[12]. Institutional adoption and aggregation introduce governance, access, privacy, and data-quality challenges [13]–[16].

The **project-level design opportunity** is to investigate a **focused, integrated student view** combining structured academic records, transparent credit-weighted GPA calculations, explained semester trends, and selected achievements under defined access permissions. This does **not** prove that commercial systems lack these functions or that the proposed combination is superior. The actual contribution of the diploma prototype will be established through implementation and evaluation against explicit criteria.

This conclusion aligns with **SDP-3**: Banner informs academic-record and GPA workflows; Moodle and Canvas inform teacher grades and progress views; Mahara and Digication inform portfolios and evidence. Product functions and research evidence remain separate.

## 6. Traceability to Project Documents and Evaluation

| Proposed requirement or evaluation            | Research rationale                                                                  | Team document / component                            | MVP verification                                                   |
| --------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------ |
| Course, grade, credit, and semester data      | Institutional data quality and context [8], [10], [13]                              | SDP-1; SDP-6 Academic Records Service, PostgreSQL    | Correct storage, enrollment relation, and updates                  |
| Automatic, configurable GPA                   | Interpretable indicators [5], [6], [9]; actual formula is an institutional decision | SDP-1; SDP-6 UC-07/UC-13, GPA Service                | Known grade/credit cases, rule changes, missing data               |
| GPA dashboard and semester charts             | Dashboard research [5]–[12]                                                         | SDP-6 UC-04; SDP-4 Apache ECharts                    | Chart-data consistency, labels, interpretation tasks               |
| Teacher entry limited to assigned students    | Student privacy [13]–[16]                                                           | SDP-1 three roles; SDP-6 UC-06/UC-07, RBAC           | Reject unauthorized read and edit requests                         |
| Achievements and certificates                 | Portfolio evidence [1]–[4]                                                          | SDP-1; SDP-6 UC-05, Achievements Service             | CRUD, file access, accurate evidence status                        |
| Synthetic input and possible CSV/Excel import | Institutional deployment and consent [13]–[16]                                      | SDP-1 constraints; SDP-4 FastAPI/Pandas; SDP-6 UC-12 | Row validation if import is agreed in MVP; no external data access |
| User-centered evaluation                      | Weaknesses in dashboard evaluation [5]–[12]                                         | SDP-8 Verification & Evaluation Plan                 | Task success, GPA understanding, feedback, access checks           |

### 6.1. Credit-weighted GPA calculation

For courses eligible under the selected institutional grading policy, the general credit-weighted average is:

$$
\mathrm{GPA} = \frac{\sum_{i=1}^{n} (p_i \times c_i)}{\sum_{i=1}^{n} c_i}
$$

In this expression, `p_i` is the grade-point value assigned to course `i`, and `c_i` is its credit value. In plain language, **multiply the grade points for each course by its credits, add those products, and divide by the total credits included in the calculation**.

For example, assume _only for illustration_ that a 3-credit course has 4.0 grade points and a 2-credit course has 3.0 grade points:

`GPA = (4.0 × 3 + 3.0 × 2) / (3 + 2) = 18 / 5 = 3.60`

This example does not prescribe any university-specific conversion scale. The implemented rule set must specify eligible courses, retakes, incomplete/pass-fail grades, zero-credit cases, and rounding. The GPA is calculated from individual grades and credits rather than manually entered as a final total.

### 6.2. Scope and architecture consistency

SDP-4 currently selects **Next.js/React/TypeScript** for the client and core API, **PostgreSQL** for academic data, **Apache ECharts** for dashboards, and **FastAPI/Pandas** for data processing. SDP-6 diagrams specify Student, Teacher, and Administrator, a Core Backend, a Data Processing Service, controlled data access, and GPA indicator snapshots. These are **team engineering decisions**; the educational papers above do not claim that this stack is universally superior. This review provides the rationale for the _information, behaviors, safeguards, and evaluation_, while SDP-4 and SDP-6 provide implementation decisions.

In the baseline scope, a reusable CSV/Excel import interface is listed as a future enhancement in SDP-1. SDP-6 also illustrates file-based initialization of test data. These can be distinguished: supplying a reproducible synthetic dataset for demonstration does not necessarily require delivery of a general-purpose administrator import interface in the initial MVP.

## 7. Methodological Limitations

- This is a targeted structured narrative review and does not claim exhaustive coverage of all relevant databases or studies.
- Portfolio and dashboard findings often come from specific courses or LMS activity, not institution-wide credit-weighted profiles. Their use here is an **inference**, not a direct evaluation of the proposed system.
- Perceived usability, sustained usage, GPA accuracy, student self-efficacy, and academic achievement are different constructs and require different measures.
- Synthetic test data permit functional, calculation, access-control, and usability tests, but cannot establish improvement in real students' longitudinal outcomes.
- The effectiveness of the proposed system must be evaluated separately; cited studies do not validate the prototype's particular grading rules, permission model, or implementation architecture.

## 8. Conclusion

Research supports a cautious rationale for a student digital profile that combines academic information with understandable visual summaries and selected achievements. Portfolios can present evidence; dashboards can support awareness; both require careful design and empirical evaluation. Institutional research further emphasizes transparent data handling and restricted access.

The proposed system will therefore demonstrate a **role-aware, centralized student profile** with correct academic records, automatically calculated GPA, interpretable semester trends, and selected achievements. The project will evaluate accuracy, access control, usability, and user interpretation, without assuming superiority over existing educational platforms or untested benefits for academic performance.

## 9. References

All 16 entries are scholarly publications; the product manuals used in SDP-3 are not counted here.

1. Bryant, L. H., & Chittum, J. R. (2013). ePortfolio effectiveness: A(n ill-fated) search for empirical support. _International Journal of ePortfolio, 3_(2), 189–198. [ERIC EJ1107810](https://eric.ed.gov/?id=EJ1107810).
2. Beckers, J., Dolmans, D., & Van Merriënboer, J. (2016). e-Portfolios enhancing students’ self-directed learning: A systematic review of influencing factors. _Australasian Journal of Educational Technology, 32_(2), 32–46. https://doi.org/10.14742/ajet.2528
3. Cheng, G., & Chau, J. (2013). Exploring the relationship between students’ self-regulated learning ability and their ePortfolio achievement. _The Internet and Higher Education, 17_, 9–15. https://doi.org/10.1016/j.iheduc.2012.09.005
4. López-Crespo, G., Blanco-Gandía, M. C., Valdivia-Salas, S., Fidalgo, C., & Sánchez-Pérez, N. (2022). The educational e-portfolio: Preliminary evidence of its relationship with student’s self-efficacy and engagement. _Education and Information Technologies, 27_, 5233–5248. https://doi.org/10.1007/s10639-021-10827-2
5. Schwendimann, B. A., Rodríguez-Triana, M. J., Vozniuk, A., Prieto, L. P., Boroujeni, M. S., Holzer, A., Gillet, D., & Dillenbourg, P. (2017). Perceiving learning at a glance: A systematic literature review of learning dashboard research. _IEEE Transactions on Learning Technologies, 10_(1), 30–41. https://doi.org/10.1109/TLT.2016.2599522
6. Bodily, R., & Verbert, K. (2017). Review of research on student-facing learning analytics dashboards and educational recommender systems. _IEEE Transactions on Learning Technologies, 10_(4), 405–418. https://doi.org/10.1109/TLT.2017.2740172
7. Bodily, R., Ikahihifo, T. K., Mackley, B., & Graham, C. R. (2018). The design, development, and implementation of student-facing learning analytics dashboards. _Journal of Computing in Higher Education, 30_, 572–598. https://doi.org/10.1007/s12528-018-9186-0
8. Viberg, O., Hatakka, M., Bälter, O., & Mavroudi, A. (2018). The current landscape of learning analytics in higher education. _Computers in Human Behavior, 89_, 98–110. https://doi.org/10.1016/j.chb.2018.07.027
9. Matcha, W., Uzir, N. A., Gašević, D., & Pardo, A. (2020). A systematic review of empirical studies on learning analytics dashboards: A self-regulated learning perspective. _IEEE Transactions on Learning Technologies, 13_(2), 226–245. https://doi.org/10.1109/TLT.2019.2916802
10. Ifenthaler, D., & Yau, J. Y.-K. (2020). Utilising learning analytics to support study success in higher education: A systematic review. _Educational Technology Research and Development, 68_, 1961–1990. https://doi.org/10.1007/s11423-020-09788-z
11. Paulsen, L., & Lindsay, E. (2024). Learning analytics dashboards are increasingly becoming about learning and not just analytics—A systematic review. _Education and Information Technologies, 29_, 14279–14308. https://doi.org/10.1007/s10639-023-12401-4
12. Jivet, I., Scheffel, M., Specht, M., & Drachsler, H. (2018). License to evaluate: Preparing learning analytics dashboards for educational practice. In _Proceedings of the 8th International Conference on Learning Analytics and Knowledge_ (pp. 31–40). ACM. https://doi.org/10.1145/3170358.3170421
13. Tsai, Y.-S., Rates, D., Moreno-Marcos, P. M., Muñoz-Merino, P. J., Jivet, I., Scheffel, M., Drachsler, H., Delgado Kloos, C., & Gašević, D. (2020). Learning analytics in European higher education—Trends and barriers. _Computers & Education, 155_, Article 103933. https://doi.org/10.1016/j.compedu.2020.103933
14. Slade, S., & Prinsloo, P. (2013). Learning analytics: Ethical issues and dilemmas. _American Behavioral Scientist, 57_(10), 1510–1529. https://doi.org/10.1177/0002764213479366
15. Pardo, A., & Siemens, G. (2014). Ethical and privacy principles for learning analytics. _British Journal of Educational Technology, 45_(3), 438–450. https://doi.org/10.1111/bjet.12152
16. Jones, K. M. L. (2019). Learning analytics and higher education: A proposed model for establishing informed consent mechanisms to promote student privacy and autonomy. _International Journal of Educational Technology in Higher Education, 16_, Article 24. https://doi.org/10.1186/s41239-019-0155-0

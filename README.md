COSMIC Cognitive Harmonisation to HRS-HCAP

This repository contains code, documentation, and methodological materials for harmonising cognitive assessment data from participating COSMIC (Cohort Studies of Memory in an International Consortium) studies to the cognitive framework used by the Harmonized Cognitive Assessment Protocol (HCAP).

The project is being conducted at UNSW Sydney.

Project Aim

COSMIC includes longitudinal ageing studies from multiple countries, but participating cohorts differ in the cognitive tests they administer. These differences make direct comparison of cognitive performance across studies challenging.

The aim of this project is to develop harmonised cognitive scores that allow cognitive performance to be compared across participating COSMIC cohorts using HRS-HCAP as a reference framework.

The proposed HCAP cognitive domains are:

* Orientation
* Memory
* Executive function
* Language/fluency
* Visuospatial function

Where supported by the available measures and statistical analyses, the project will generate:

1. Harmonised domain-specific cognitive scores
2. A harmonised global cognition score

Not every cohort is expected to contain sufficient information to estimate every cognitive domain.

⸻

Harmonisation Strategy

The proposed workflow consists of five main stages:

1. Identify participating cohorts

Determine which COSMIC cohorts will participate and compile an inventory of the cognitive assessments administered by each study.

2. Map cognitive measures to HCAP domains

A modified Delphi study will be used to obtain expert consensus regarding which HCAP cognitive domains are assessed by each cognitive measure.

Rather than assuming that each cognitive test measures only one construct, experts will rate the extent to which each measure assesses each HCAP domain before nominating its primary domain.

3. Determine cognitive-domain coverage

The resulting mappings will be combined with the cognitive-test inventory to determine which HCAP domains can be adequately represented within each cohort.

4. Construct harmonised domain scores

The expert-derived measurement structure will be evaluated empirically using methods such as:

* Confirmatory factor analysis (CFA)
* Measurement invariance
* Differential item functioning (DIF)

Where the evidence supports cross-study comparability, harmonised domain scores will be constructed.

5. Construct global cognition

For cohorts meeting prespecified minimum domain-coverage and statistical criteria, harmonised domain information will be combined to derive a global cognitive score.

The overall workflow is:

Cohort participation → Measure inventory → Delphi domain mapping → Domain coverage → Statistical harmonisation → Domain scores → Global cognition

⸻

Conceptual and Statistical Harmonisation

A central principle of this project is to separate conceptual harmonisation from statistical harmonisation.

Expert judgement will be used to determine which mappings between cognitive measures and HCAP constructs are theoretically plausible. These hypotheses will then be tested empirically.

In particular, the project distinguishes between:

Does this test measure the same cognitive domain?

and

Is this test sufficiently comparable across studies to function as a linking indicator?

A cognitive measure may provide useful information about a domain without being sufficiently equivalent across studies to serve as a linking measure.

Therefore, expert consensus will inform the statistical models rather than determine them.

⸻

Modified Delphi

The proposed Delphi panel will include experts with experience in:

* COSMIC
* HCAP
* Neuropsychological assessment
* Cognitive ageing
* Epidemiology
* Cross-study cognitive harmonisation
* Cognitive assessment across different countries and languages

For each cognitive measure, experts will initially rate its relationship with each HCAP domain and nominate a primary domain.

In subsequent rounds, participants will receive anonymised summaries of the panel’s responses and have the opportunity to reconsider their classifications.

A provisional criterion of ≥75% agreement on the primary domain is being considered as the threshold for consensus.

Measures without clear consensus will not necessarily be excluded and may instead be treated as multidomain, examined in subsequent Delphi rounds, or evaluated through sensitivity analyses.

⸻

Linking Measures

Measures that appear comparable across COSMIC cohorts and HCAP will undergo an additional assessment of their suitability as potential linking indicators.

This assessment may consider differences in:

* Administration
* Instructions
* Stimulus material
* Number of items or trials
* Timing
* Recall versus recognition
* Scoring
* Language and translation
* Mode of administration
* Cohort-specific adaptations

Potential linking measures may then be classified as high-confidence, tentative, or unsuitable links before empirical evaluation.

⸻

Repository Structure

The repository will be updated as the project develops.

cosmic_harmonisation/
│
├── README.md
├── documentation/
│   └── harmonisation_decisions.Rmd
│
├── delphi/
│   ├── survey_materials/
│   └── results/
│
├── data/
│   └── cognitive_measure_inventory/
│
├── scripts/
│   ├── data_management/
│   ├── cfa/
│   ├── measurement_invariance/
│   └── scoring/
│
└── outputs/
    ├── tables/
    └── figures/

The repository structure above is provisional and will evolve as the project progresses.

⸻

Methodological Documentation

Detailed methodological decisions are documented separately in the project R Markdown documentation.

This includes:

* Delphi design and consensus criteria
* HCAP domain definitions
* Cognitive-test classifications
* Cohort domain coverage
* Linking-item decisions
* Statistical harmonisation decisions
* Criteria for constructing domain scores
* Criteria for constructing global cognition
* Outstanding methodological questions
* A chronological decision log

The intention is to maintain a transparent record of both what was decided and why it was decided throughout the harmonisation process.

⸻

Project Status

Current stage: Method development and cognitive measure mapping.

Current priorities include:

* Confirm participating COSMIC cohorts
* Compile cognitive-test inventories
* Finalise HCAP domain definitions
* Finalise the modified Delphi protocol
* Conduct Delphi Round 1
* Establish cohort-by-domain coverage
* Identify candidate linking measures
* Develop the statistical harmonisation model
* Generate harmonised domain scores
* Evaluate construction of global cognition

⸻

Contact

James Lian, PhD
UNSW Sydney
j.lian@unsw.edu.au

For questions regarding this repository or the COSMIC cognitive harmonisation project, please contact the project team.

# COSMIC cognitive harmonisation: strategy and work-to-date overview

Prepared 3 Nov 2026 for external review. Author context: James Lian, postdoc (about 2 months in) at UNSW CHeBA, delivering Prof. Susanne Röhr's NIH-funded project. Items marked **[unverified]** come from general knowledge or memory, not from checked sources.

## 1. Project and goal

- **Aim:** harmonise cognitive data from COSMIC (Cohort Studies of Memory in an International Consortium) cohorts so that domain scores and a global cognition score are comparable across cohorts. The target framework is the HRS-HCAP (Harmonized Cognitive Assessment Protocol).
- **Original design (from the earlier ChatGPT project export):**
  - Item-level curation of each cohort's cognitive tests against HCAP.
  - An expert/Delphi process (a panel of about 14 experts).
  - Statistical harmonisation (item response theory / co-calibration) using the Rmonize R package.
  - Data held on UNSW DPAU servers and in the ADDI AD Workbench, a trusted research environment where row-level data cannot leave.
- **My earlier assessment:** feasible but partial. Suggested tiers: Tier 1 anchor-linked, Tier 2 caveated, Tier 3 not harmonisable. Suggested a global score rule of at least 3 of 5 domains (including memory and executive function) with at least 2 tests per domain. This is a suggestion, not agreed.

## 2. Timeline of the strategy

1. **Original plan:** all COSMIC cohorts, HCAP item linking, then co-calibration.
2. **After Alden Gross (HCAP) meeting:** revised to a proof-of-concept pilot on Western, English-speaking cohorts. Shortlist: MAS, PATH, EAS, MYHAT. Other candidates: TILDA, NICOLA, CFAS. Excluded: CSHA (French/English) and WHICAP (Spanish/English). I do not have my notes from the Alden meeting, so that part is thin.
3. **After Karen Blackmon meeting:** learned the International Brain Health Index (IBHI), an alternative that needs only domain-level mapping, not linking items.
4. **After Susanne meeting (3 Nov), current strategy:**
   - Move away from the Western-only pilot. Susanne no longer wants to do only WEIRD cohorts.
   - Go back to the original idea of looking at all contributing studies together, starting with an agreement process.
   - Send each cohort custodian/PI the HCAP domain structure and a tailored questionnaire (generated with AI from their data dictionary). The custodians map their own cognitive tests to HCAP domains, with a confidence rating.
   - Round 2: sanity check by CHeBA neuropsychologists or a diverse expert panel.
   - Rationale: respects regional context and local expertise (for example animal naming mapped to language processing in bilingual cohorts) and is defensible on equity grounds. HCAP is seen as too granular. Karen's method is seen as insufficiently described.
   - Known risk: custodians become a bottleneck. Mitigation: pre-filled, short forms with deadlines.
   - Incentives: co-authorship, visibility of their data, involvement in future COSMIC projects.
   - Susanne suggests contacting all cohorts and seeing who replies first. Likely early responders: LEILA75+, Ding Ding's cohort.

## 3. The two methodological routes

| | HCAP / co-calibration (Alden) | IBHI counting method (Karen Blackmon) |
|---|---|---|
| Core idea | Link confidently equivalent items, then statistically co-calibrate | Map items to 5 domains, dichotomise against local regression-based norms, count impaired domains |
| Needs | Common, similarly administered linking items | Domain mapping, normative reference group per cohort |
| Output | Continuous comparable scores | Burden (0 = brain health, 1 = alert, ≥2 = loss), severity, profile |
| Strengths | Granular, allows invariance/DIF testing | Keeps local instruments; suits LMIC; meta-metrics can be shared instead of raw data |
| Limits | Linking items are sparse across heterogeneous retrospective cohorts | Loses granularity; tested only in 10/66 data (5 Latin American/Caribbean countries); unreviewed |

### IBHI: general overview
- IBHI is a categorical, multidimensional counting approach (modelled on the Alkire-Foster method used for multidimensional poverty indices). Each cohort maps its own measures to a small set of brain health domains and classifies each person against locally derived norms.
- Individuals are summarised by whether impairment is present, how severe it is and what the profile across domains looks like, and these meta-metrics can be aggregated to the population level.
- Appeal for COSMIC: local instruments are retained, no linking items are needed, and it supports comparison where individual-level cross-country comparison is inappropriate.
- Caveats: the approach is not yet peer reviewed (a preprint is under review and is not reproduced here), it has so far been tested in a single multi-country dataset (10/66), it loses granularity compared with co-calibration, and the way normative reference groups are defined needs close scrutiny.

### Karen meeting notes (key points)
- Education and culture effects are large; animal naming plus word recall is inadequate in LMIC.
- Advice: map measures to domains, derive regression-based norms from a normative reference group (not sample distribution), apply the actuarial approach. Verbal fluency can count as executive function when data are lacking. Cross-walking required.
- Data may indicate what is pragmatic, instead of starting with a Delphi.
- She may start a consortium with Gheorghe and apply IBHI to more datasets.
- HCAP differs because it used prospective harmonisation with controlled interviewer training.

## 4. Work completed (files in ~/Downloads)

- **Cohort review.xlsx:** sheets Cohort review, Data request tracker, Data in hand, Read me. Tracker updated from emails on 30 Oct and 3 Nov.
- **Curation schema draft.xlsx:** HCAP-aligned item schema (HCAP's 17 columns plus COSMIC additions: cohort_wave, link_status, expert_review_needed, verified_against_source, decision_note). 15 example items; 8 MYHAT rows are from the real data dictionary, 7 MAS/PATH/EAS rows are unverified placeholders. Also Linking Items (12 pairs), Domains_and_subdomains, Studies, Items_description. Not opened in Excel for layout. An earlier version is kept as v1.
- **HCAP schema (read from HCAP Prestatistical Harmonization Resource.xlsx, v0.1c):** Items sheet with about 1,250 rows. IDs are u###; code1 uses car::recode syntax; linking confidence 2 = confident, 1 = tentative, -1 = not in HRS-HCAP. Domains: orientation, memory (immediate/delayed/recognition), language/fluency, attention, speed, executive, visuospatial, depression.
- **Webinar decks:** 10-minute COSMIC webinar (v2, 9 slides), Alden meeting plan and 11-slide deck.
- **Susanne meeting handout (docx, 2 Nov):** written before the 3 Nov meeting, so it reflects the older tiered plan and is now out of date.
- **Blackmon notes and agenda (md):** the notes were written from an AAIC abstract only and predate the preprint.
- **Dementia incidence paper review** (Vella et al., JAMA Neurology 2026, 22 COSMIC cohorts, N = 38,418): its harmonisation was diagnostic and analytic (cohort-specific clinical diagnoses, common person-period R pipeline, inverse-probability censoring weights, Poisson models, two-step random-effects meta-analysis), not cognitive-test harmonisation. It noted that cognitive tests and thresholds may differ in performance across language, literacy and education, and that education harmonisation varied.

## 5. Cohort data-access status

Data folders held (as of 26 Oct 2026): AGELESS, ALBION, Bambui, BPRHS, CLAS, Como Vai, ESPRIT, HELIAD, I-Lan, IMIAS, Indianapolis Ibadan, InveceAb, ISA, KLOSCAD, Leiden85+, LEILA75+, MMAP, MYHAT, MYNAH, SALSA, SLASII, SPAH, TIGER, plus Uganda, Vallecas, ZARADEMP.

| Cohort | Status (emails 29-30 Oct, meeting 3 Nov) | Next action / owner |
|---|---|---|
| MYHAT | In hand | Start pilot curation (James) |
| MAS | Committee approval needed; Susanne completed extra procedures | Naja to confirm approval sent |
| PATH | Committee approval needed; unclear if application submitted | Renecia to confirm |
| EAS | Promised updated data on 1 Sept; Renecia says delayed but coming soon | Renecia to follow up |
| TILDA | ISSDA (non-EU agreements not finalised) or ICPSR (latest waves missing) | James to check both |
| NICOLA | Difficult; DTA with Queen's Belfast needed; HCAP substudy exists; Susanne says data can be downloaded from the HCAP repository | Susanne to contact Carol Brayne |
| CFAS | Stalled since Carol Brayne left | Low priority |
| SLASII | In hand; assessed in participant's habitual language (including English) but language is not a variable | Ask Darren |
| IIDP (US arm) | Suggested by Darren | Check Indianapolis-Ibadan folder |
| PREHCO | Follow up (Susanne) | TBD |

Correction made on the way: NICOLA is not "screening only", since it ran an HCAP substudy. CFAS and TILDA main waves are the ones thought to be screening-level **[unverified; item-level coverage still to check]**.

## 6. Current plan and next steps

1. Pitch the revised plan to Darren Lipnicki, who needs to be convinced.
2. Contact PIs directly rather than relying on Darren or Renecia.
3. Design the custodian questionnaire:
   - closed list of HCAP domains with definitions and examples;
   - fields: test/item, proposed domain, optional secondary domain, confidence (1-5), rationale, language/administration notes, culturally or education-adapted flag, comments;
   - clear instructions, deadline, one tailored form per cohort, pre-filled from data dictionaries with AI (custodians confirm or correct).
4. Ask Susanne's computer science contacts (Somya and a PhD student) about AI tools; bring Xiaoxi back onto the project.
5. Round 2 review by neuropsychologists or a diverse expert panel. Previously named reviewers: Adam Bentvelzen and Nicole Kochan (third reviewer unknown).
6. Pending admin: 10/66 access, chat with Ash, tracking data requests.

## 7. My own assessment of the strategy

**Strengths:** removes the dependence on data access (mapping needs only data dictionaries); respects local expertise and equity; avoids over-granular HCAP linking; yields a publishable consensus-mapping result with an agreement statistic (custodian versus expert panel).

**Risks:** custodian bottleneck and slow replies; inconsistent mappings across cohorts; self-selection among early responders; mapping alone does not harmonise scores, so a downstream method (IBHI-style norms or co-calibration where items overlap) must still be chosen; AI-generated draft mappings may be wrong; uncertainty about the IBHI foundations.

## 8. Questions for the reviewer

1. Is custodian-led mapping to HCAP domains a defensible basis for harmonisation, and how should inter-custodian consistency be controlled?
2. Which downstream method best follows domain mapping when few linking items exist: IBHI-style norm-based categories, co-calibration on the subset with overlap, or something else?
3. How should normative reference groups be defined retrospectively when cohorts lack healthy, condition-free subsamples?
4. What should the questionnaire contain to maximise response rate and data quality?
5. How should confidence ratings be used when pooling mappings?
6. What risks have been missed, especially around education, language and cultural effects?

## 9. Known gaps and unverified items

- No notes from the Alden meeting; the HCAP-side details above are from the earlier plan and the schema file.
- Cohort battery details (MAS, PATH, TILDA, NICOLA, EAS, CFAS) are from general knowledge and not verified against data dictionaries.
- Karen Blackmon's preprint is deliberately not included in this repository; only a general description of the approach is given.
- Nothing from this work has been committed to git.

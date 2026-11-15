# Harmonisation strategy

**Version of 15 Nov 2026.** This describes the current plan and the evidence it rests on. Each stage is marked **Decided**, **Proposed** or **Open**. The dated history of how we got here is in the decision log.

## 1. Goal

Produce cognitive scores that can be compared across COSMIC cohorts:

- a **global cognition** score first (**Proposed**), because a general factor can use any cognitive item and needs fewer shared items per domain;
- **domain scores** for memory, executive function (including attention and speed), orientation and language where a cohort has enough linked items. These are the domains HCAP scored (Gross et al., 2023). Visuospatial is recorded, but HCAP did not score it and COSMIC coverage is thin.

Not every cohort will support every score. A cohort or measure that cannot be linked defensibly is left out of the linked scores (**Decided**, 4 Nov 2026).

### What "harmonised" means here

Three claims are kept apart, because they need different evidence:

| Level | Claim | Evidence needed |
|---|---|---|
| Construct | Two tests measure the same domain | Expert classification |
| Scale | Scores are on one metric | Linked items and a fitted model |
| Comparability | A difference in scores means a difference in ability | Bias (DIF) testing for the comparison being made |

Standardising scores within each cohort (z-scores) gives none of the three across cohorts, so it is not used as the harmonisation method.

## 2. The evidence we are following

HCAP harmonised cognitive data from six countries (USA, England, India, Mexico, China, South Africa). Their method, in order:

1. **Pre-statistical harmonisation.** Every item was reviewed for what it measures and for differences in content, administration, language and scoring between studies (Briceño et al., 2023).
2. **Expert rating of links.** Two neuropsychologists rated each item against the HRS-HCAP reference as a confident link, a tentative link or non-linking (Gross et al., 2023).
3. **Co-calibration.** Confirmatory factor models, equivalent to item response theory models, were fitted study by study. Parameters of linking items were held equal across studies ("item banking"), with HRS-HCAP setting the scale. Non-linking items stayed in the model with their own parameters.
4. **Bias testing.** Linking items were tested for differential item functioning. Items with salient bias were demoted to non-linking. Three were: orientation to year in India and South Africa, and two language items in China.

This produced reliable scores for general cognition, memory, executive function, orientation and language.

### How COSMIC differs, and what we change

| Difference | Consequence | Our response |
|---|---|---|
| HCAP studies shared a protocol; COSMIC cohorts did not | Far fewer shared items | Build a linkage map and check the cohorts can be connected **before** promising scores (stage 5) |
| COSMIC has about 70 cohorts | Two experts cannot cover everything, and their judgement is open to challenge | Two-rater review plus a modified Delphi with a larger, more diverse panel (stage 3) |
| HRS-HCAP is a US study | A US-only reference suits some cohorts badly | Links between COSMIC cohorts, and to HCAP's studies in India, China, Korea, Mexico, Chile, South Africa and Kenya, count as much as links to HRS-HCAP |
| Many cohort teams have moved on | Cohorts may not reply | Cohort input is a factual check with a deadline, not a dependency (**Decided**, 4 Nov 2026) |

## 3. Stages

### Stage 1. Inventory: Done for the pilot

List every cognitive variable in each cohort's files, from names and labels only. Six pilot cohorts chosen on 4 Nov 2026 because their data are in hand and they span six regions: MYHAT, HELIAD, KLOSCAD, MYNAH, SPAH and the Uganda study.

### Stage 2. Item-level curation: Draft v0.2

One row per item per cohort, in the layout of HCAP's pre-statistical resource (**Decided**, 4 Nov 2026). See `item_mapping_conventions.md`.

- An item that looks equivalent to an HCAP item takes HCAP's code. This is a **proposed** link, flagged for expert review.
- Other items get a COSMIC code. Two cohorts sharing a COSMIC code is a proposed COSMIC-to-COSMIC link.
- Every source variable in v0.2 was checked against the cohort file headers on 13 Nov 2026.

### Stage 3. Expert judgement: In preparation

For each test version, experts judge the domain, what else might affect scores, and whether it can be linked to a comparison item. The link categories are HCAP's: confident, tentative, none. Details are in `delphi_protocol.md`.

- **Modified Delphi with a diverse panel** (**Decided**, 4 Nov 2026).
- **Two raters first, panel for the hard cases** (**Proposed**). The six pilot cohorts alone give about 120 distinct test versions. Sending all of them to a panel is not workable, and it grows with every cohort.
- Consensus rules are fixed before Round 1 (**Proposed**: 75% agreement, two rounds).

### Stage 4. Cohort check: Not started

Each cohort contact is asked whether our description of their tests is correct. No reply by the deadline means the description is used and marked unconfirmed (**Decided** in principle, 4 Nov 2026).

### Stage 5. Linkage map and feasibility: Not started

Draw the network of cohorts joined by confident and tentative links, for global cognition and for each domain. A cohort with no path to the others cannot be put on the common scale by modelling alone. The minimum number of links required per cohort is **Open** and will be set before any model is fitted.

### Stage 6. Co-calibration: Not started

Factor / item response models with linking items held equal across cohorts, following Gross et al. (2023). **Open:** the reference metric (HRS-HCAP, which needs HRS-HCAP data, or a COSMIC cohort), the software, and how cohorts with only total scores are handled.

### Stage 7. Bias testing and validation: Not started

- Bias tests are targeted. The expert questionnaire asks what might affect each score (schooling, translation, cultural familiarity), and those answers decide which tests are run.
- **Proposed:** adopt the thresholds in Gross et al. (2023). Items with salient bias are demoted to non-linking, not dropped.
- Report reliability, and how much scores move when the set of anchors changes.

### Stage 8. Scale up: Not started

Add cohorts in batches once the pilot shows the pipeline works and how long each cohort takes.

## 4. Approaches considered and set aside

| Approach | When | Why it was set aside |
|---|---|---|
| Pilot restricted to English-speaking cohorts | Oct 2026 | Does not serve the project's aim of including diverse and low- and middle-income cohorts |
| Cohort custodians map their own tests | 3 Nov 2026 | Depends on replies that many cohorts can no longer give |
| Grouping cohorts as culturally similar or different | Dropped 4 Nov 2026 | Differences are specific to each cohort's version of a test, not to regions |
| Norm-based categorical index (International Brain Health Index) | Discussed Oct to Nov 2026 | Needs only domain mapping, which is attractive, but was unpublished and gives categories, not scores. Could complement co-calibration later |

## 5. Main risks

- **Too few links.** Some cohorts may not connect. Stage 5 exists to find this out early.
- **Descriptions without manuals.** Test descriptions come from data dictionaries and published papers. Stage 4 is the safeguard.
- **Workload.** Curation is slow. The pilot will give a time per cohort to plan against.

## References

- Gross AL, Li C, Briceño EM, Arce Rentería M, et al. *Lancet Healthy Longevity* 2023;4(10):e573–e583. doi:10.1016/S2666-7568(23)00170-8
- Briceño EM, Arce Rentería M, Gross AL, Jones RN, et al. *Neuropsychology* 2023;37(3):247–257. doi:10.1037/neu0000816

# COSMIC cognitive harmonisation: modified Delphi protocol

**Draft v0.1 for discussion, 15 Nov 2026.** Everything here is a proposal until the project team agrees it. Items marked **[decide]** need a decision before Round 1.

## 1. Why we are doing this and what it must produce

Statistical harmonisation needs two expert judgements for every cognitive item, before any model is fitted:

1. **What it measures** (its domain), so it can be assigned to a factor.
2. **Whether it can act as a link** to the same item in another study, so scores can be put on a common scale.

HCAP made these judgements with a small expert group: two neuropsychologists rated each non-HRS item against the HRS-HCAP reference as a *confident* link, a *tentative* link or *non-linking*, and tentative links were then tested statistically for bias (Gross et al., 2023). The Delphi does the same job for COSMIC with a larger and more diverse panel, and uses the same three categories so that our decisions are directly comparable with HCAP's.

Each answer feeds a specific column in the item-mapping workbook:

| Question | Feeds | Used for |
|---|---|---|
| Main domain | `domain` | Assigning the item to a domain factor |
| Other domains | notes; cross-loading flag | Deciding whether an item is used for the global factor only |
| Confidence | reported with each decision | Weighing borderline decisions |
| What else affects scores | bias hypotheses | Choosing which bias (DIF) tests to run, and for which groups |
| Link to comparison item | `Link status`, linking confidence (2 / 1 / none) | Choosing anchors for the common scale |
| What differs | `notes_comparability` | Building general rules for curators |

## 2. Design

- **Modified Delphi.** "Modified" because the items are prepared by the project team from the curation work; there is no open first round.
- **Online, in REDCap,** one test per page with a reference panel.
- **Two rounds, three at most.** **[decide]**
- **Blinded between panellists.** Answers are stored under a code. Only the moderator holds the key. Panellists never see who gave which answer.
- **HCAP's existing classifications are not shown,** so they do not anchor the ratings.

## 3. Panel

- Invite about 15 to finish with at least 10. **[decide]**
- Mix of clinical neuropsychologists, psychometricians and people who know the cohorts, with at least 40% from outside Australia, the UK and the US. **[decide]**
- Project team members do not rate. One team member facilitates contact with cohorts and one moderates the rounds.
- The list of candidates is kept privately until people have been invited.

## 4. Items

- **Unit of rating:** one test version as given in one study (language, materials, timing, scoring). Where two studies used the same protocol they share a card and the card says so.
- **Reference panels** are written from data dictionaries, variable labels and published battery descriptions. Each panel states its source and lists anything not yet confirmed.
- **Cohort check before Round 1:** each study contact is asked one factual question, "is this description of your test correct?". No reply within three weeks means the panel goes out marked as unconfirmed. **[decide]**
- **No copyrighted test content** (word lists, story text, stimuli) appears in any panel.

### Which items go to the panel

The six pilot cohorts alone produce about 120 distinct cards, of which about 90 are not straightforward. At roughly 3 minutes a card that is more than four hours per rater, which is not workable, and it gets worse with every cohort added. Proposed triage **[decide]**:

1. **Two-rater review of everything.** Two neuropsychologists independently rate every card, as HCAP did.
2. **Delphi panel for the hard cases only:** cards where the two raters disagree, any test with no HCAP counterpart, and any version with a known adaptation (language, script, modality, scoring).
3. **Calibration cards:** a few uncontested items with an HCAP precedent in every batch, to check the panel is using the scale as intended.

Batches of about 20 cards, each under an hour.

## 5. Questions asked for every card

| # | Question | Answer options |
|---|---|---|
| 1 | Which cognitive domain does this version mainly measure? | Orientation; Memory; Attention / processing speed; Executive function; Language; Visuospatial / constructional; No single domain; Another domain (named); Cannot judge |
| 2 | Does it also measure any other domain to a substantial degree? | Tick any of the six, or "No other domain" |
| 3 | How confident are you in your choice of main domain? | 1 to 5 |
| 4 | Apart from the ability being measured, is the score likely to be noticeably affected by any of these? | Literacy or schooling; language or translation; cultural familiarity; vision, hearing or hand movement; who gives the test and where; none |
| 5 | Could it be linked to the comparison item (would two people of the same ability score the same on both)? Asked once per comparison item. | Confident link; Tentative link; No link; Cannot judge |
| 5a | If tentative or no link: what differs? | Language; content; presentation; timing or trials; scoring; literacy demands; cultural familiarity; other |
| 6 | Comments | Free text |

Notes on the choices:

- **Domains.** Six domains with one-line definitions shown on every page. Attention / processing speed is kept separate from executive function because that boundary is where experts disagree most. HCAP's published scores combine them, so agreement is also reported with the two merged.
- **Memory is one domain.** Whether a score is immediate recall, delayed recall or recognition is a fact about the task. The curator records it; raters are not asked to judge it.
- **Comparison items** can be an HCAP item or another COSMIC cohort's version. COSMIC-to-COSMIC links matter as much as links to HCAP.

## 6. Consensus rules, fixed before Round 1 **[decide]**

- **Denominator:** panellists who gave a judgement. "Cannot judge" is counted separately.
- **Domain consensus:** at least 75% choose the same main domain.
- **Link consensus:** at least 75% choose the same category. If neither "confident" nor "tentative" reaches 75% but together they do, the item is a tentative link.
- **Too little information:** if 30% or more answer "cannot judge", the panel is revised with the cohort's help and the card is rated again.
- **Minimum:** consensus is only declared when at least 8 panellists gave a judgement.

The 75% threshold is the most common one in published Delphi studies (Diamond et al., 2014).

## 7. Round 2

- Only cards without consensus are rated again.
- Each panellist sees the group's distribution of answers, the anonymised comments and their own Round 1 answer.
- Panellists may keep or change their answer.

## 8. After the final round

| Result | Decision |
|---|---|
| Domain consensus | Item assigned to that domain |
| No domain consensus | Item treated as multi-domain: used for the global score only |
| Consensus: confident link | Shared code; anchor |
| Consensus: tentative link | Shared code, flagged; tested for bias before use as an anchor |
| Consensus: no link, or no consensus | Separate code; not an anchor |
| Bias factor ticked by 50% or more | A specific bias test is planned for that item |

Every decision is logged with the vote counts. A measure or cohort that cannot be resolved is left out of the linked scores, as agreed on 4 Nov 2026.

## 9. Pilot

Purpose: test the questionnaire, not the items.

- Time per card and in total.
- Whether each reference panel had enough information.
- Whether the domain list, definitions and link question were clear.

Pilot answers are not used in the main rounds. Changes made after the pilot are recorded.

## 10. Analysis and reporting

- Percentage agreement and median confidence for each card, by round.
- Agreement with HCAP's existing classification on the calibration cards.
- Descriptive comparison by discipline and region, where numbers allow.
- Reported against the ACCORD guideline for consensus methods (Gattrell et al., 2024).
- Protocol registered on OSF before Round 1. **[decide]**

## 11. Ethics and data **[check]**

- Confirm with UNSW whether an expert Delphi needs HREC approval or an exemption. The consent wording in the questionnaire is a placeholder until then.
- Responses are held in UNSW REDCap. The code key is kept separately by the moderator.
- Agree what panellists are offered: authorship, group authorship or acknowledgement. **[decide]**

## 12. Limitations to state up front

- Reference panels are descriptions, not test manuals. Raters judge what is described.
- Expert judgement is subjective. It sets up the statistical checks; it does not replace them.
- Card order is fixed, so earlier cards may influence later ones. Reversing the order for half the panel would address this at the cost of a second survey. **[decide]**
- The questionnaire is in English, which limits who can take part.

## 13. Open decisions

1. First target score: global cognition first (recommended), or domains.
2. Whether pilot-cohort leads rate, or only confirm their own descriptions.
3. The triage in section 4.
4. Thresholds and number of rounds in section 6.
5. Ethics route and what panellists are offered.

## References

- Gross AL, et al. Harmonisation of later-life cognitive function across national contexts: results from the Harmonized Cognitive Assessment Protocols. *Lancet Healthy Longevity* 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10637129
- Gattrell WT, et al. ACCORD (ACcurate COnsensus Reporting Document): a reporting guideline for consensus methods in biomedicine. *PLOS Medicine* 2024.
- Diamond IR, et al. Defining consensus: a systematic review recommends methodologic criteria for reporting of Delphi studies. *Journal of Clinical Epidemiology* 2014.

- Briceño EM, et al. A cultural neuropsychological approach to harmonization of cognitive data across culturally and linguistically diverse older adult populations. *Neuropsychology* 2023;37(3):247–257.

The questionnaire itself is in `delphi/`: `cards.py` holds the test descriptions and answer options, and `build_redcap.py` turns them into the REDCap import file.

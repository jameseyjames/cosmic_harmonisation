# CLAUDE.md

Guidance for AI assistants working in this repository.

## Project
Harmonising cognitive test data across COSMIC ageing cohorts, using HCAP as the reference framework. Lead: James Lian, CHeBA, UNSW Sydney. Start with `README.md`, then `documentation/harmonisation_strategy.md`.

## Current state (15 Nov 2026)
- Six pilot cohorts curated at item level: `curation/COSMIC_Item_Mapping_Pilot_v0.2.xlsx`.
- Pilot Delphi questionnaire built for REDCap: `delphi/`.
- Delphi protocol drafted, not yet agreed: `documentation/delphi_protocol.md`.
- No statistical modelling yet.

## Rules
- **This repository is public. Never add participant-level data**, unpublished third-party material (including the HCAP pre-statistical resource), contact details, or lists of people who have not agreed to be named.
- **Do not reproduce copyrighted test content** (word lists, story text, stimuli).
- **Record decisions in `Harmonisation Decision Log.Rmd`** with a date, a reason and a status (Decided, Done, Proposed, Open, Superseded). Do not present a proposal as a decision.
- **Generated files are built from source.** Edit `curation/build_item_mapping.py` or `delphi/cards.py`, then re-run the build script. Do not hand-edit the workbook, the REDCap CSV or the preview page.
- Follow HCAP's curation conventions (`documentation/item_mapping_conventions.md`).
- Keep these distinctions: what a test measures is not whether it can link cohorts; a shared construct is not a common scale; within-cohort z-scores are not harmonisation.
- UK English. Plain, direct wording.

## Build
```bash
pip install openpyxl
python delphi/build_redcap.py
python curation/build_item_mapping.py   # needs private/HCAP_Prestatistical_Harmonization_Resource.xlsx (git-ignored)
```

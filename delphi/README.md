# Delphi questionnaire (pilot, Round 1)

| File | What it is |
|---|---|
| `cards.py` | The 18 test descriptions and all answer options. **Edit the questionnaire here.** |
| `build_redcap.py` | Turns `cards.py` into the two files below |
| `COSMIC_Delphi_R1_REDCap_DataDictionary_v2.csv` | REDCap import file |
| `rater_preview.html` | What a panel member sees. Download and open in a browser; nothing is saved |
| `preview_template.html` | Layout for the preview page |

## Setting it up in REDCap

1. Create an empty project and enable surveys.
2. Upload the CSV on the **Data Dictionary** page and commit. Do not open and re-save it in Excel first.
3. In the Online Designer, enable the instrument as a survey.
4. Survey settings: question display **One section per page**; progress bar on; **Save & Return Later** on.
5. Send the **public survey link**. Panel members identify themselves with a code, not a name.

## Design

One test per page. Each page opens with a reference panel describing the test as one cohort gave it, then asks:

1. the main cognitive domain;
2. any other domains;
3. confidence;
4. what else might affect scores (schooling, translation, cultural familiarity and so on);
5. whether it can be linked to a comparison item, which may be an HCAP item or another COSMIC cohort's version;
6. comments.

The reasoning and the consensus rules are in `documentation/delphi_protocol.md`.

Test descriptions are written from data dictionaries, variable labels and published papers. They do not reproduce copyrighted test content, and each one lists anything not yet confirmed with the cohort.

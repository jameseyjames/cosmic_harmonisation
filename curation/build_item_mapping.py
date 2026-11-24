"""Build the COSMIC item-level cognitive mapping workbook (HCAP Items layout).

Usage:  python curation/build_item_mapping.py [output.xlsx]
Needs:  openpyxl, and the HCAP Prestatistical Harmonization Resource workbook, which is not public and is not in this
        repository. Put it at private/HCAP_Prestatistical_Harmonization_Resource.xlsx or set HCAP_RESOURCE to its path.

All mapping decisions are hard-coded below (add() calls per cohort; NEW = COSMIC c-code registry).
Source variable names come from the cohort files held by COSMIC (names and labels only, no data).
Edit here, re-run, and bump the version in the output filename + ReadMe tab.
"""
import openpyxl, collections
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

import os, sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HCAP=os.environ.get('HCAP_RESOURCE',os.path.join(ROOT,'private','HCAP_Prestatistical_Harmonization_Resource.xlsx'))
OUT=sys.argv[1] if len(sys.argv)>1 else os.path.join(ROOT,'curation','COSMIC_Item_Mapping_Pilot_v0.3.xlsx')
wb0=openpyxl.load_workbook(HCAP,data_only=True)
rows=list(wb0['Items'].iter_rows(values_only=True)); h=rows[0]
hc=collections.defaultdict(lambda:{'lab':collections.Counter(),'dom':collections.Counter(),'studies':set()})
for r in rows[1:]:
    d=dict(zip(h,r))
    if not d['item']: continue
    x=hc[d['item']]; x['lab'][d['item_label']]+=1; x['dom'][(d['domain'] or '',d['subdomain'] or '')]+=1
    if d['study']: x['studies'].add(d['study'])
def hlab(u): return hc[u]['lab'].most_common(1)[0][0]
def hdom(u): return hc[u]['dom'].most_common(1)[0][0]
def hstud(u):
    import re
    def norm(x):
        for suf in ['w1w2g','_g2a','w2','_v1']:
            if x.endswith(suf): x=x[:-len(suf)]
        return {'CHARLSHCAPg':'CHARLSHCAP','HAALSIHCAPx':'HAALSIHCAP','NHATS11':'NHATS','NHATS6':'NHATS'}.get(x,x)
    base=sorted({norm(s) for s in hc[u]['studies']})
    return ', '.join(base)

# COSMIC-new code registry: code -> (label, domain, subdomain)
NEW={
 'c120':('Orientation – two streets near home (CSI-D)','Orientation','Orientation_place'),
 'c240':('CSI-D 3-word immediate recall (CSI-D word set)','Memory','Memory_episodic_immediate'),
 'c241':('CSI-D 3-word delayed recall (CSI-D word set)','Memory','Memory_episodic_delayed'),
 'c242':('CSI-D short story recall','Memory','Memory_episodic_immediate'),
 'c243':("CSI-D recall of interviewer's name",'Memory','Memory_episodic_delayed'),
 'c244':('CSI-D long-term memory item','Memory','(not specified)'),
 'c250':('Logical Memory Story B immediate (WMS-R, MYHAT)','Memory','Memory_episodic_immediate'),
 'c251':('Logical Memory Story B delayed (WMS-R, MYHAT)','Memory','Memory_episodic_delayed'),
 'c252':('Fuld Object Memory Evaluation – learning (3 trials)','Memory','Memory_episodic_immediate'),
 'c253':('Fuld Object Memory Evaluation – delayed recall','Memory','Memory_episodic_delayed'),
 'c254':('Face-Name Associative Memory – total recall (3 trials)','Memory','Memory_episodic_immediate'),
 'c255':('WMS-R Visual Reproduction – immediate','Memory','Memory_episodic_immediate'),
 'c256':('WMS-R Visual Reproduction – delayed','Memory','Memory_episodic_delayed'),
 'c257':('Rey Auditory Verbal Learning Test – trials 1–5 total','Memory','Memory_episodic_immediate'),
 'c258':('Rey Auditory Verbal Learning Test – short-delay recall (trial 6)','Memory','Memory_episodic_delayed'),
 'c259':('Rey Auditory Verbal Learning Test – long-delay recall (trial 7)','Memory','Memory_episodic_delayed'),
 'c267':('Benton Visual Retention Test – recognition','Memory','Memory_recognition'),
 'c260':('Greek Verbal Learning Test – trials 1–5 total','Memory','Memory_episodic_immediate'),
 'c261':('Greek Verbal Learning Test – short-delay free recall','Memory','Memory_episodic_delayed'),
 'c262':('Greek Verbal Learning Test – long-delay free recall','Memory','Memory_episodic_delayed'),
 'c263':('Greek Verbal Learning Test – recognition','Memory','Memory_recognition'),
 'c264':('MCG Complex Figure – immediate recall','Memory','Memory_episodic_immediate'),
 'c265':('MCG Complex Figure – delayed recall','Memory','Memory_episodic_delayed'),
 'c266':('MCG Complex Figure – recognition','Memory','Memory_recognition'),
 'c270':('CERAD-K constructional recognition','Memory','Memory_recognition'),
 'c340':('Digit span total (forward + backward)','Executive','(not specified)'),
 'c341':('Frontal Assessment Battery total','Executive','(not specified)'),
 'c342':('Anomalous sentence repetition – correct','Executive','(not specified)'),
 'c420':('Months forward – time','Attention_speed','(not specified)'),
 'c421':('Months backward – time','Attention','(not specified)'),
 'c422':('Digit Symbol-Coding (WAIS-III)','Attention_speed','(not specified)'),
 'c530':('Letter fluency – P (60 s)','Language_fluency','(not specified)'),
 'c531':('Letter fluency – S (60 s)','Language_fluency','(not specified)'),
 'c532':('Letter fluency – Greek alpha (60 s)','Language_fluency','(not specified)'),
 'c533':('Semantic fluency – objects (Greek)','Language_fluency','(not specified)'),
 'c534':('Boston Naming Test – full/long form (spontaneous + stimulus cue)','Language_fluency','(not specified)'),
 'c535':('Boston Naming Test – 15-item CERAD-K (spontaneous)','Language_fluency','(not specified)'),
 'c536':('Boston Naming Test – 15-item BDAE short form (HELIAD)','Language_fluency','(not specified)'),
 'c537':('Word/phrase repetition (BDAE-type, HELIAD)','Language_fluency','(not specified)'),
 'c538':('Auditory comprehension (BDAE complex ideational material, HELIAD)','Language_fluency','(not specified)'),
 'c539':('Modified Indiana University Token Test (12 items)','Language_fluency','(not specified)'),
 'c540':('CSI-D object naming – chair','Language_fluency','(not specified)'),
 'c541':('CSI-D object naming – shoes','Language_fluency','(not specified)'),
 'c542':('CSI-D object naming – knuckle','Language_fluency','(not specified)'),
 'c543':('CSI-D object naming – shoulder','Language_fluency','(not specified)'),
 'c544':('CSI-D comprehension – nod head','Language_fluency','(not specified)'),
 'c545':('CSI-D definition – what is done in a place of worship','Language_fluency','(not specified)'),
 'c546':('CSI-D definition – where medicines are bought','Language_fluency','(not specified)'),
 'c547':('Boston Naming Test – 30-item form','Language_fluency','(not specified)'),
 'c548':('Letter fluency – F, A, S total (COWAT)','Language_fluency','(not specified)'),
 'c620':('Clock drawing – 15-point scoring (MYHAT)','Visuospatial','(not specified)'),
 'c621':('Clock drawing – free draw (HELIAD scoring)','Visuospatial','(not specified)'),
 'c622':('Clock drawing – copy (HELIAD scoring)','Visuospatial','(not specified)'),
 'c623':('CLOX1 – free-drawn clock','Visuospatial','(not specified)'),
 'c624':('CLOX2 – copied clock','Visuospatial','(not specified)'),
 'c625':('Block Design','Visuospatial','(not specified)'),
 'c626':('Benton Visual Form Discrimination','Visuospatial','(not specified)'),
 'c627':('MCG Complex Figure – copy','Visuospatial','(not specified)'),
 'c628':('Judgement of Line Orientation – 10-item abbreviated','Visuospatial','(not specified)'),
 'c629':('Block Design – WAIS-R','Visuospatial','(not specified)'),
 'c901':('MMSE total score (version-specific)','(not specified)','(not specified)'),
}
def lab(code): return hlab(code) if code.startswith('u') else NEW[code][0]
def dom(code): return hdom(code) if code.startswith('u') else NEW[code][1:]

R=[]  # rows
def add(code,study,file,src,rng,notes_cmp,conf,admin='',code2='',coding='',sim='',waves='',level='Item',label_extra=''):
    d,sd=dom(code)
    R.append(dict(item=code,item_label=lab(code)+(f' [{label_extra}]' if label_extra else ''),study=study,domain=d,subdomain=sd,
      curator='JL',source_file=file,source_item=src,code2=code2,possible_range=rng,coding_notes=coding,
      notes_comparability=notes_cmp,conf=conf,hcap_studies=(hstud(code) if code.startswith('u') else ''),
      similar_items=sim,admin=admin,waves=waves,level=level,
      status=('Proposed anchor – for Delphi' if code.startswith('u') else 'New COSMIC item – link to be decided')))

# ---------------- MYHAT ----------------
F='COSMIC_CogHarmo_MYHAT.csv'; S='MYHAT'; W='Multiple cycles (long format; variable cycle)'
A='US English; in-person; MMSE administered with BOTH serial 7s and WORLD backward'
for c,v,cf,n in [('u107','MMSE01',2,'Standard MMSE, US English – same as HRS-HCAP.'),('u116','MMSE02',2,''),('u105','MMSE03',2,''),('u108','MMSE04',2,''),('u106','MMSE05',2,''),
                 ('u113','MMSE06',2,'US state – same as HRS-HCAP.'),('u114','MMSE07',1,'County – HCAP rates this tentative for HRS-HCAP too.'),('u115','MMSE08',2,''),('u117','MMSE09',2,''),
                 ('u118','MMSE10',1,'Item is "name of this place or address" – HRS requires street number AND name; scoring rule may differ.')]:
    add(c,S,F,v,'0 1',n,cf,A,waves=W)
add('u258',S,F,'MMSE11','0 3','Registration of 3 words; MYHAT word set to confirm against HRS-HCAP word set.',1,A,waves=W)
add('u412',S,F,'MMSE12_7','0 5','Serial 7s not administered in HRS-HCAP (HRS uses WORLD backward). Links to ELSA/LASI-DAD/MexCog/CHARLS serial 7s.',-1,A,waves=W)
add('u409',S,F,'MMSE12_W','0 5','WORLD backward administered to all (not only serial-7 refusers) – a rare bridge between serial-7 and WORLD cohorts.',2,A,waves=W)
add('u209',S,F,'MMSE13to15','0 3','3-word delayed recall; confirm word set vs HRS-HCAP.',1,A,waves=W)
add('u505',S,F,'MMSE16','0 1','',2,A,waves=W)
add('u506',S,F,'MMSE17','0 1','',2,A,waves=W)
add('u513',S,F,'MMSE18','0 1','Same English phrase as HRS-HCAP.',2,A,waves=W)
add('u511',S,F,'MMSE19','0 1','',2,A,waves=W)
add('u523',S,F,'MMSE20','0 3','MYHAT stores the 3-step command as one 0–3 score; equals sum of HRS-HCAP u519+u520+u521.',2,A,coding='Compare with HRS-HCAP by summing u519–u521.',waves=W)
add('u509',S,F,'MMSE21','0 1','HCAP flags unclear HRS scoring rules for "write a sentence" – tentative.',1,A,waves=W)
add('u602',S,F,'MMSE22','0 1','',2,A,waves=W)
add('c901',S,F,'calcMMSEscore7 calcMMSEscoreW','0 30','Two totals provided (serial-7 version and WORLD version). Total-score bridge to HELIAD/KLOSCAD only.',None,A,waves=W,level='Total',sim='u4xx/u1xx MMSE items')
add('u203',S,F,'STORYA_LINE1_IR STORYA_LINE2_IR STORYA_LINE3_IR STORYA_LINE4_IR STORYA_LINE5_IR STORYA_LINE6_IR STORYA_LINE7_IR','0 25',
    'MYHAT: WMS-R Logical Memory Story A, scored 0–25, stored as line-level sub-scores. HRS-HCAP: WMS-IV Logical Memory Story B, 25 units (Briceño et al. 2023, Table 1). WMS-R Story A and WMS-IV Story B are understood to be versions of the same story, but wording and scoring criteria were revised between editions – confirm with a neuropsychologist before treating as an anchor.',1,A,code2='sum_source',coding='Story-A total also supplied as NPLOGMEM_IMMA.',waves=W,label_extra='Story A')
add('u207',S,F,'STORYA_LINE1_DR STORYA_LINE2_DR STORYA_LINE3_DR STORYA_LINE4_DR STORYA_LINE5_DR STORYA_LINE6_DR STORYA_LINE7_DR','0 25',
    'As u203 – depends on story equivalence across WMS editions and on the delay interval.',1,A,code2='sum_source',coding='Story-A total also supplied as NPLOGMEM_DELA.',waves=W,label_extra='Story A')
add('c250',S,F,'STORYB_LINE1_IR STORYB_LINE2_IR STORYB_LINE3_IR STORYB_LINE4_IR STORYB_LINE5_IR STORYB_LINE6_IR STORYB_LINE7_IR STORYB_LINE8_IR','0 25','Second WMS-R story (Story B); HRS-HCAP gave only one WMS-IV story plus the Brave Man story, so no HCAP counterpart.',None,A,code2='sum_source',sim='u203',waves=W)
add('c251',S,F,'STORYB_LINE1_DR STORYB_LINE2_DR STORYB_LINE3_DR STORYB_LINE4_DR STORYB_LINE5_DR STORYB_LINE6_DR STORYB_LINE7_DR STORYB_LINE8_DR','0 25','',None,A,code2='sum_source',sim='u207',waves=W)
add('c252',S,F,'NPFuld_T1 NPFuld_T2 NPFuld_T3','0 30','Fuld OME with semantic interference; item-level (10 objects x 3 trials, e.g. BALL_TRIAL1…) also available.',None,A,code2='sum_source',sim='u201 u202',waves=W,level='Subtest')
add('c253',S,F,'NPFuld_DELAY','0 10','Item-level ball_del…scissors_del available.',None,A,sim='u210 u211',waves=W,level='Subtest')
add('c254',S,F,'fname_tot','0 36','Added 2016, replacing Visual Reproduction. fname_type flags estimated scores – filter on fname_type = 0.',None,A,waves=W,level='Subtest')
add('c255',S,F,'NPVISREP_IMMA NPVISREP_IMMB NPVISREP_IMMC NPVISREP_IMMD','0 41','Administered until Feb 2016 only. Memory vs visuospatial domain is contested – Delphi item.',None,A,code2='sum_source',sim='u212 c264',waves=W+' (to 2016)',level='Subtest')
add('c256',S,F,'NPVISREP_DELA NPVISREP_DELB NPVISREP_DELC NPVISREP_DELD','0 41','As c255.',None,A,code2='sum_source',sim='u212 c265',waves=W+' (to 2016)',level='Subtest')
add('u401',S,F,'NPTRAILA_TIME','time (s)','HRS-HCAP score is seconds to complete, with errors adding time; HCAP scales as 1 − log(time)/log(max time). Check MYHAT time cap and use of NPTRAILA_PTS for incompletes.',2,A,waves=W,level='Subtest')
add('u303',S,F,'NPTRAILB_TIME','time (s)','As u401; check MYHAT discontinuation rule versus HRS-HCAP.',2,A,waves=W,level='Subtest')
add('u309',S,F,'Q1digit Q2digit Q3digit Q4digit Q5digit Q6digit','0 12','Digit span FORWARD only (6 spans, 3–8 digits, 2 trials). HCAP codes digit span as Executive – contested (attention). Version/scoring differs from LASI-DAD/KLPS.',-1,A,code2='sum_source',coding='Total also supplied as NPDIGIT_TOT; longest span = NPDIGIT_MAX.',waves=W,level='Subtest')
add('u501',S,F,'NPFLUENT_ANIM','0 max','Animals, 60 s.',2,A,waves=W,level='Subtest')
add('c530',S,F,'NPFLUENT_P','0 max','Phonemic fluency – language vs executive domain contested. HCAP precedent (HAALSI u714) = Language_fluency.',None,A,sim='u714',waves=W,level='Subtest')
add('c531',S,F,'NPFLUENT_S','0 max','As c530.',None,A,sim='u714',waves=W,level='Subtest')
add('c534',S,F,'NPBOSTON_A NPBOSTON_B','0 60','Item-level Q1_BED…Q60_ABACUS available. Noose item removed 2009 and scores prorated; reverse/basal administration (Qstart). Spontaneous + stimulus-cued (BostonNaming = A+B).',None,A,code2='sum_source',sim='u715 c535 c536',waves=W,level='Subtest')
add('c539',S,F,'Q1token Q2token Q3token Q4token Q5token Q6token Q7token Q8token Q9token Q10token Q11token Q12token','0 24',
    'HCAP has Token Test u306 (LASI-DAD) coded EXECUTIVE; COSMIC proposes Language (comprehension) – Delphi item. Versions differ.',None,A,code2='sum_source',sim='u306',waves=W,level='Subtest')
add('c620',S,F,'Q1CONTOUR Q2SIZE Q3NUMBERS Q4ARABIC Q5ORDER Q6ROTATED Q7POSITION Q8INSIDE Q9HANDS Q10HOUR Q11MINUTE Q12PROPORTION Q13SUPERFLUOUS Q14JOINED Q15CENTER','0 15',
    'Clock drawing, 15-point scoring system. Different scoring from HCAP clock items (u603/u604) and from CLOX/HELIAD – item-level criteria may allow re-scoring to a common rule.',None,A,code2='sum_source',sim='u603 u604 c621 c623',waves=W,level='Subtest')
add('c625',S,F,'Q1blocks Q2blocks Q3blocks Q4blocks Q5blocks Q6blocks Q7blocks Q8blocks Q9blocks Q10blocks Q11blocks Q12blocks Q13blocks Q14blocks','0 68',
    'WAIS-III Block Design. Before Jan 2018 testing began at design 5 (basal rules) – handle in recode.',None,A,code2='sum_source',waves=W,level='Subtest')
add('c626',S,F,'Q1benton Q2benton Q3benton Q4benton Q5benton Q6benton Q7benton Q8benton Q9benton Q10benton Q11benton Q12benton Q13benton Q14benton Q15benton Q16benton','0 32','Added Feb 2016. Items coded 1/2/3 (2/1/0 points) – recode needed.',None,A,code2='sum_source',waves=W+' (from 2016)',level='Subtest')

# ---------------- HELIAD ----------------
F='HELIAD A_total_GBD.sav (wave B: HELIAD B_total_GBD.sav, suffix _B)'; S='HELIAD'; W='Baseline (A) + follow-up (B); C file holds domain z-scores only'
A='Greek; in-person; low-education subgroup – functional illiteracy flag available (functionalilliterac)'
add('c901',S,F,'minimental30','0 30','MMSE total only – no item-level MMSE in the files supplied. Request MMSE items to enable item anchors.',None,A,waves=W,level='Total')
add('c260',S,F,'Sum1_5correct1st','0 80','Greek Verbal Learning Test: 16 words from 4 semantic categories, 5 learning trials (CVLT-style). Version A at baseline, version B at follow-up. Not linkable to CERAD lists directly.',None,A,sim='u201 u202',waves=W,level='Subtest')
add('c261',S,F,'ll7cor1','0 16','INFERRED from CVLT-style structure: ll6 = interference list, ll7 = short-delay free recall, ll8 = short-delay cued. The protocol file supplied covers the clinical interview only, so confirm with the HELIAD team.',None,A,waves=W,level='Subtest')
add('c262',S,F,'ll9cor1','0 16','INFERRED: ll9 = long-delay free recall, ll10 = long-delay cued. Confirm with the HELIAD team.',None,A,sim='u210 u211',waves=W,level='Subtest')
add('c263',S,F,'TBC – one of lld1 / lltd1 / llts1 / llta1','TBC','Recognition score – variable not identifiable from labels (Greek transliterations: lld1, llts1, llta1, lltd1, llnp1, llna1, llnf1 look like hit and foil-type counts). Ask the HELIAD team.',None,A,sim='u213 u214',waves=W,level='Subtest')
add('c627',S,F,'figurecopy','0 36','Medical College of Georgia Complex Figure copy.',None,A,sim='u601',waves=W,level='Subtest')
add('c264',S,F,'figureimmediate','0 36','',None,A,sim='u212',waves=W,level='Subtest')
add('c265',S,F,'figuredelayed','0 36','',None,A,sim='u212',waves=W,level='Subtest')
add('c266',S,F,'figurerecognitionSUM','TBC','',None,A,waves=W,level='Subtest')
add('c628',S,F,'jlo1stdiades','0 10','Benton JLO abbreviated to 10 items (every third item); published HELIAD outcome = number of correct pairs. An alternative 0–20 scoring is in jloolesmax20.',None,A,waves=W,level='Subtest')
add('u401',S,F,'TMTA_tmtAtime1','time (s)','Tentative: numeral familiarity/education. Greek standardisation (Vlahou & Kosmidis 2002). Capped version in TMTA_tmtAtime1TR (file label says truncated above 400 s; the norms paper reports a 300 s stop – confirm). HELIAD itself files TMT under Attention/Processing speed.',1,A,waves=W,level='Subtest')
add('u303',S,F,'TMTB_tmitBtime1','time (s)','Greek version – Part B presumably alternates numbers with GREEK letters (script adaptation; confirm); DIF candidate. Capped version TMTB_tmitBtime1TR. HELIAD files TMT-B under Attention/Processing speed, HCAP under Executive – Delphi item.',1,A,waves=W,level='Subtest')
add('c533',S,F,'vfsem1stobj','0 max','Semantic category is "objects", NOT animals – do not link to u501.',None,A,sim='u501',waves=W,level='Subtest')
add('c532',S,F,'vfphon1stalphobj','0 max','Phonemic fluency, Greek letter alpha.',None,A,sim='u714 c530 c531',waves=W,level='Subtest')
add('c536',S,F,'naming1st','0 15','Boston Naming Test 15-item short form from the BDAE short form (Greek). A different 15-item set from the CERAD BNT-15 (c535), so not given the same code.',None,A,sim='u715 c534 c535',waves=W,level='Subtest')
add('c537',S,F,'repetition1st','TBC','BDAE short-form repetition: three multisyllabic words and three short phrases.',None,A,sim='u513',waves=W,level='Subtest')
add('c538',S,F,'comphr1st','TBC','Selected items from BDAE short-form Complex Ideational Material; number of items to confirm.',None,A,waves=W,level='Subtest')
add('c342',S,F,'sentrepeatcorrect1','0 14','Original Greek test: 14 common sayings each containing one incorrect word, repeated verbatim. HELIAD files it under Executive; language vs executive is contested – Delphi item.',None,A,waves=W,level='Subtest')
add('c420',S,F,'MonthsAsec','time (s)','Months forward, completion time (errors in MonthsAerr). HELIAD files the Months test under Executive.',None,A,waves=W,level='Subtest')
add('c421',S,F,'MonthsBsec','time (s)','Months backward, completion time (errors in MonthsBerr). HELIAD files it under Executive; HCAP codes the similar backward day naming (u404) as Attention – Delphi item.',None,A,sim='u404',waves=W,level='Subtest')
add('c621',S,F,'clockA1st','TBC','Free-drawn clock set to 6:45; scoring after Freedman et al. 1994 / Bozikas et al. 2008 – confirm range.',None,A,sim='u603 c620 c623',waves=W,level='Subtest')
add('c622',S,F,'clockcopy','TBC','Clock copy.',None,A,sim='c624',waves=W,level='Subtest')

# ---------------- KLOSCAD ----------------
F='KLOSCAD GBD.sav (also COSMIC_GBD…xlsx)'; S='KLOSCAD'; W='Multiple waves (long format; Waveoftest)'
A='Korean; CERAD-K neuropsychological battery; scores supplied as raw + z (z not used)'
add('c901',S,F,'J3MMSEscores','0 30','MMSE in the Korean CERAD version (MMSE-KC) – content differs from standard MMSE; total only.',None,A,waves=W,level='Total')
add('u501',S,F,'J1CategoricalFluencyTestscore','0 max','Animals, 60 s (CERAD-K).',1,A,waves=W,level='Subtest')
add('c535',S,F,'TotalsumofprimaryresponseofJ2BostonNamingTest','0 15','15-item CERAD-K BNT; secondary/tertiary response totals also supplied.',None,A,sim='u715 c534 c536',waves=W,level='Subtest')
add('u201',S,F,'J4WordListMemoryTestscore','0 30','CERAD-K word list, 3 trials. HRS-HCAP shows each word for 2 s and the participant reads it aloud (HRS 2016 HCAP protocol summary). Standard CERAD is also card-based, but CERAD-K may be read aloud to non-literate participants – confirm; if verbal only, recode to u202.',1,A,waves=W,level='Subtest')
add('u601',S,F,'J5ConstructionalPraxisTestscore','0 11','CERAD constructional praxis (4 figures).',2,A,waves=W,level='Subtest')
add('u210',S,F,'J6WordListRecallTestscore','0 10','As u201 – presentation modality determines u210 vs u211.',1,A,waves=W,level='Subtest')
add('u213',S,F,'J7WordListRecognitionTestscore','0 10','Check whether score is hits only or hits + correct rejections (CERAD convention: 0–10 corrected).',1,A,waves=W,level='Subtest')
add('u212',S,F,'J8ConstructionalMemoryTestscore','0 11','',1,A,waves=W,level='Subtest')
add('c270',S,F,'K2ConstructionalRecognitionTestscore','TBC','',None,A,waves=W,level='Subtest')
add('u401',S,F,'J9TrailMakingTestAscore','TBC','Variable labelled "score" – confirm it is completion time in seconds.',1,A,waves=W,level='Subtest')
add('u303',S,F,'J9TrailMakingTestBscore','TBC','Korean TMT-B alternates numbers with Korean characters – script adaptation; confirm units.',1,A,waves=W,level='Subtest')
add('c340',S,F,'K3DigitSpan_total','TBC','Forward and backward supplied only as z-scores (K3F…Zscore, K3B…Zscore). Request raw forward/backward to link to u309/u310.',None,A,sim='u309 u310',waves=W,level='Subtest')
add('c341',S,F,'K4FrontalAssessmentBatteryscore','0 18','FAB – multi-component executive screen.',None,A,waves=W,level='Total')
add('c623',S,F,'K5_1sumofCLOX1','0 15','CLOX1 free-drawn clock (executive-weighted).',None,A,sim='u603 c620 c621',waves=W,level='Subtest')
add('c624',S,F,'K5_2sumofCLOX2','0 15','CLOX2 copied clock.',None,A,sim='c622',waves=W,level='Subtest')

# ---------------- MAS (Sydney Memory and Ageing Study) ----------------
# No data file yet: rows are drafted from the published baseline battery and must be checked against the data dictionary.
F='No data file yet – battery from Sachdev et al. 2010, Int Psychogeriatr 22(8):1248–64, Table 1'; S='MAS'
W='Wave 1 2005–07; face-to-face every 2 years; telephone TICS in between'
A='Australian English; face-to-face assessment by trained research psychologists in one or two sessions; participants had to speak and write English'
N='NO DATA YET – awaiting data access'
add('c901',S,F,N,'0 30','Standard MMSE; adjusted score <24 excluded at entry. If item scores are held, they give direct anchors with MYHAT and SPAH.',None,A,waves=W,level='Total')
add('u401',S,F,N,'time (s)','Standard Trail Making A in English, as HRS-HCAP. Check the time cap and how incompletes are scored.',2,A,waves=W,level='Subtest')
add('u303',S,F,N,'time (s)','Standard Trail Making B in English. MAS classes it as executive, as HCAP does. Check the time cap.',2,A,waves=W,level='Subtest')
add('c422',S,F,N,'0 133','WAIS-III Digit Symbol-Coding: the participant writes the symbol for each digit. HRS-HCAP SDMT (u402) is the reverse: the participant writes the digit for each symbol. Similar demands, different format – link to be decided by the panel.',None,A,sim='u402',waves=W,level='Subtest')
add('u207',S,F,N,'0 25','WMS-III Logical Memory Story A (the Anna Thompson story), delayed recall. HCAP already gives this story the same code as HRS-HCAP Logical Memory (HAALSI-HCAP, u207), and MYHAT used the same story (WMS-R). Scoring criteria differ between WMS editions, so tentative.',1,A,waves=W,level='Subtest')
add('c257',S,F,N,'0 75','RAVLT: 15 words, 5 learning trials. Different list and length from CERAD (10 words, 3 trials), Fuld and the Greek VLT, so no direct anchor.',None,A,sim='u201 u202 c260',waves=W,level='Subtest')
add('c258',S,F,N,'0 15','Recall after the interference list (trial 6).',None,A,sim='c261',waves=W,level='Subtest')
add('c259',S,F,N,'0 15','Delayed recall (trial 7).',None,A,sim='u210 u211 c262',waves=W,level='Subtest')
add('c267',S,F,N,'TBC','Benton Visual Retention Test, multiple-choice recognition. Visual memory; no counterpart in the other pilot cohorts.',None,A,sim='c266',waves=W,level='Subtest')
add('c547',S,F,N,'0 30','Boston Naming Test, 30-item form (Kaplan et al. 2001). MYHAT scored all 60 items separately, so if MAS item scores are held the shared items can link at item level. Compare the 15-item forms in KLOSCAD (c535) and HELIAD (c536).',None,A,sim='u715 c534 c535 c536',waves=W,level='Subtest')
add('u501',S,F,N,'0 max','Animals, 60 s, English, as HRS-HCAP. Links MAS directly to MYHAT, KLOSCAD and SPAH.',2,A,waves=W,level='Subtest')
add('c629',S,F,N,'0 51','WAIS-R Block Design; MYHAT used WAIS-III (c625). The editions share some designs but differ in items and scoring – link to be decided by the panel.',None,A,sim='c625',waves=W,level='Subtest')
add('c548',S,F,N,'0 max','Controlled Oral Word Association Test: letters F, A and S, 60 s each. MAS classes it as executive; HCAP precedent (HAALSI phonemic fluency, u714) is language, so the domain is contested. If letters are scored separately, S could link to MYHAT letter S (c531).',None,A,sim='u714 c530 c531 c532',waves=W,level='Subtest')
add('u502',S,F,N,'0 1','TICS by telephone between face-to-face waves (the paper cites de Jager et al. 2003, i.e. TICS-m). Check whether item scores are held. Telephone administration – DIF candidate.',1,A,waves='Telephone waves only')
add('u504',S,F,N,'0 1','As u502.',1,A,waves='Telephone waves only')
add('u701',S,F,N,'0 1','As u502. Presumably asks for the prime minister, as ELSA-HCAP does – confirm.',1,A,waves='Telephone waves only')

# ---------------- SPAH (10/66 protocol) ----------------
# MYNAH (India) used the same protocol; it moved to the first expansion batch on 23 Nov 2026, and its rows can be restored from v0.2.
for S,F,A,W,fu in [('SPAH','CSI-D.sav','Brazil (São Paulo); 10/66 DRG protocol; Brazilian Portuguese; CSI-D + CERAD 10-word list read aloud','Baseline + 2-year follow-up (follow-up variables prefixed f)',True)]:
    def fu_(v): return v+(' | FU: '+' '.join('f'+x for x in v.split()) if fu else '')
    add('u202',S,F,fu_('learn1 learn2 learn3'),'0 30','10/66 CERAD list read ALOUD by interviewer (not visual) – matches the HCAP verbal-presentation code u202 (LASI-DAD, HAALSI, MexCog, ChileCog), not HRS-HCAP u201.',-1,A,code2='sum_source',coding='Total also supplied as immed.',waves=W,level='Subtest')
    add('u211',S,F,fu_('recall'),'0 10','Verbal-presentation CERAD delayed recall.',-1,A,waves=W,level='Subtest')
    add('u501',S,F,fu_('animals'),'0 max','Animals, 60 s, translated.',1,A,waves=W,level='Subtest')
    add('u506',S,F,fu_('pencil'),'0 1','Real object shown (CSI-D).',1,A,waves=W)
    add('u505',S,F,fu_('watch'),'0 1','',1,A,waves=W)
    add('c540',S,F,fu_('chair'),'0 1','',None,A,waves=W)
    add('c541',S,F,fu_('shoes'),'0 1','',None,A,waves=W)
    add('c542',S,F,fu_('knuckle'),'0 1','',None,A,waves=W)
    add('u508',S,F,fu_('elbow'),'0 1','HRS-HCAP took this item from the CSI-D (10/66) – HCAP rates confident across all its studies.',2,A,waves=W)
    add('c543',S,F,fu_('should'),'0 1','',None,A,waves=W)
    add('u516',S,F,fu_('bridge'),'0 1','HCAP u516 exists in MexCog/ChileCog only; note ChileCog specifies bridge type.',-1,A,waves=W)
    add('u515',S,F,fu_('hammer'),'0 1','Acceptable answers differ by language (HCAP note).',1,A,waves=W)
    add('c545',S,F,fu_('pray'),'0 1','"What do you do in a church/temple?" Religious-context item; DIF candidate across faith settings.',None,A,waves=W)
    add('c546',S,F,fu_('chemist'),'0 1','"Where do you buy medicine?"',None,A,waves=W)
    add('u513',S,F,fu_('repeat'),'0 1','Translated phrase – HCAP rates repetition tentative across languages.',1,A,waves=W)
    add('c544',S,F,fu_('nod'),'0 1','',None,A,waves=W)
    add('u517',S,F,fu_('point'),'0 1','10/66 wording is "point to ceiling then to floor", NOT window then door (HRS-HCAP). HCAP precedent: MexCog/ChileCog use sky/floor and still share u517. Two-step pointing command; DIF candidate.',1,A,waves=W)
    add('u523',S,F,fu_('paper'),'0 3','CSI-D paper-folding command; check scoring matches MMSE 3-step.',1,A,waves=W)
    add('c243',S,F,fu_('nrecall'),'0 1',"Recall of interviewer's name.",None,A,waves=W)
    add('c240',S,F,fu_('wordimm'),'0 3','CSI-D 3-word set – differs from MMSE words, so not u258. Other CSI-D cohorts (MYNAH, Uganda) use the same set, so this will link them when they are added.',None,A,sim='u258',waves=W)
    add('c241',S,F,fu_('worddel'),'0 3','CSI-D 3-word delayed recall. A strong link to other CSI-D cohorts (MYNAH, Uganda) when they are added.',None,A,sim='u209',waves=W)
    add('c242',S,F,fu_('story'),'TBC','CSI-D story recall – confirm immediate vs delayed and scoring range.',None,A,sim='u203 u205',waves=W)
    add('u115',S,F,fu_('town'),'0 1','Name of town.',1,A,waves=W)
    add('u701',S,F,fu_('chief'),'0 1','Local/national political leader (not necessarily president) – tentative link to TICS "name president".',1,A,waves=W)
    add('c120',S,F,fu_('street'),'0 1','',None,A,waves=W)
    add('u518',S,F,fu_('store'),'0 1','HRS-HCAP took this item from the CSI-D (1066 "local market").',1,A,waves=W)
    add('u118',S,F,fu_('address'),'0 1','Own address – HCAP notes HRS requires street number AND name; scoring may differ.',1,A,waves=W)
    add('c244',S,F,fu_('longmen'),'0 1','Content of item 27 to confirm.',None,A,waves=W)
    add('u106',S,F,fu_('month'),'0 1','',2,A,waves=W)
    add('u108',S,F,fu_('day'),'0 1','',2,A,waves=W)
    add('u107',S,F,fu_('year'),'0 1','',2,A,waves=W)
    add('u116',S,F,fu_('season'),'0 1','São Paulo is subtropical, where seasons are less distinct – DIF candidate.',1,A,waves=W)
    add('u605',S,F,fu_('circle'),'0 1','Circle copy – HCAP code exists for ChileCog only.',-1,A,waves=W)
    add('u602',S,F,fu_('pentag'),'0 1','Intersecting pentagons as in MMSE.',1,A,waves=W)

# ---------- write workbook ----------
out=openpyxl.Workbook()
HDR=Font(bold=True,color='FFFFFF'); FILL=PatternFill('solid',fgColor='1F4E78'); WRAP=Alignment(wrap_text=True,vertical='top')
thin=Side(style='thin',color='D9D9D9'); BOR=Border(bottom=thin)
def sheet(ws,headers,data,widths):
    ws.append(headers)
    for i,c in enumerate(ws[1],1):
        c.font=HDR; c.fill=FILL; c.alignment=Alignment(wrap_text=True,vertical='center')
    for r in data: ws.append(r)
    for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment=WRAP; c.border=BOR
    ws.freeze_panes='D2' if len(headers)>6 else 'A2'
    ws.auto_filter.ref=ws.dimensions
    ws.row_dimensions[1].height=45

# ReadMe
rm=out.active; rm.title='ReadMe'
txt=[
('COSMIC Item-Level Cognitive Mapping – pilot cohorts (v0.3, 23 Nov 2026)',True),
('Purpose: pre-statistical harmonisation of cognitive items for five COSMIC pilot cohorts – MYHAT (USA), MAS (Australia), KLOSCAD (South Korea), HELIAD (Greece) and SPAH (Brazil) – following the HCAP Prestatistical Harmonization Resource (Jones et al.).',False),
('Pilot cohorts revised 23 Nov 2026: Sydney MAS added; MYNAH and Uganda moved to the first expansion batch. MAS rows are drafted from the published baseline battery (Sachdev et al., 2010) and will be checked against the MAS data dictionary when access is approved.',False),
('',False),
('How this sheet follows the HCAP curation system',True),
('• Items tab mirrors HCAP\'s Items tab columns (item, item_label, study, domain, subdomain, curator, source_file, source_item, code1, code2, possible_range, coding_notes, notes_comparability, Linking Confidence, similar_items) plus COSMIC columns at the right.',False),
('• Item codes: where a COSMIC item appears equivalent to an HCAP item, the HCAP u-code is REUSED. Same code = proposed anchor (HCAP convention). All such links are flagged "Proposed anchor – for Delphi" and are untested assumptions.',False),
('• COSMIC-new items use c### codes. The first digit follows HCAP: 1 orientation, 2 memory, 3 executive, 4 attention/speed, 5 language/fluency, 6 visuospatial; 9 = global/total. Two cohorts sharing a c-code is a proposed within-COSMIC anchor (e.g. c901, the MMSE total, in MYHAT, MAS, KLOSCAD and HELIAD).',False),
('• Domains/subdomains use HCAP\'s Domains_and_subdomains list. For reused u-codes the HCAP domain is inherited unchanged (even where contested – see notes); for c-codes the domain is a COSMIC a-priori proposal for the Delphi.',False),
('• Linking Confidence to HRS-HCAP: 2 = confident, 1 = tentative, −1 = HCAP item not in HRS-HCAP (link is to another HCAP study – see "HCAP studies with this code"); blank = COSMIC-new item.',False),
('• code2 "sum_source" = analytic variable is the sum of the listed source items (HCAP convention). code1 recodes and missing-value codes are deliberately left for a second pass.',False),
('• No copyrighted item content (word lists, story text) is recorded – HCAP rule.',False),
('',False),
('Scope decisions (agreed 4 Nov 2026)',True),
('• Primary scores only for test-level cohorts (KLOSCAD, HELIAD, and MAS until its data are seen): process scores (intrusions, perseverations, clustering), cohort z-scores and derived domain scores are listed on the Excluded tab.',False),
('• Item level used where the data allow (MYHAT, SPAH); test totals elsewhere. Level column records which.',False),
('• Source variables were identified from variable names/labels in the cohort files held by COSMIC; no data values were used. On 13 Nov 2026 every source variable was re-checked against the file headers (see the Source verified column and the Changelog tab). Entries marked TBC / INFERRED still need the study team. MAS entries are marked NO DATA YET.',False),
('',False),
('Tabs',True),
('Changelog – what changed between versions. Items – one row per analytic variable per study. Coverage – code × cohort matrix (the linkage map). Code_registry – every code, its label and which cohorts carry it. Studies, Domains_and_subdomains – as HCAP. Excluded – variables reviewed but not mapped. Open_questions – items to resolve before the Delphi.',False),
]
for t,b in txt:
    rm.append([t]); rm.cell(rm.max_row,1).font=Font(bold=b,size=13 if b and rm.max_row==1 else 11)
    rm.cell(rm.max_row,1).alignment=Alignment(wrap_text=True,vertical='top')
rm.column_dimensions['A'].width=140

# Items
cols=['item','item_label','study','domain','subdomain','curator','source_file','source_item','source_labels','code1','code2','possible_range','coding_notes','notes_comparability',
      'Linking Confidence to HRS-HCAP (2=confident; 1=tentative; -1 NOT IN HRSHCAP)','similar_items','original_question_text',
      'HCAP studies with this code','Link status','Administration / language notes','Waves','Level (Item/Subtest/Total)','Delphi priority','Source verified']
def prio(r):
    t=(r['notes_comparability']+r['item_label']).lower()
    if any(k in t for k in ['contested','delphi item','dif candidate','adaptation','not animals','not an address']): return 'High'
    if r['conf']==1 or r['item'].startswith('c'): return 'Medium'
    return 'Low'
def ver(r):
    s=r['source_item']
    if s.startswith('NO DATA YET'): return 'Not yet – no data file (from cohort paper)'
    if 'NOT IN FILE' in s: return 'No – variable not in file'
    if s.startswith('TBC'): return 'No – variable not identified'
    if 'INFERRED' in r['notes_comparability']: return 'Variable exists; meaning inferred'
    return 'Yes – variable exists in file'
# integrity checks
DIG={'Orientation':'1','Memory':'2','Executive':'3','Attention':'4','Attention_speed':'4','Speed':'4','Language_fluency':'5','Visuospatial':'6','(not specified)':'9'}
for c,(l,d,sd) in NEW.items(): assert c[1]==DIG[d],(c,d)
for r in R:
    if r['item'].startswith('u'): assert r['item'] in hc and hc[r['item']]['lab'],r['item']
order={'MYHAT':0,'MAS':1,'KLOSCAD':2,'HELIAD':3,'SPAH':4}
R.sort(key=lambda r:(order[r['study']],r['item']))
data=[[r['item'],r['item_label'],r['study'],r['domain'],r['subdomain'],r['curator'],r['source_file'],r['source_item'],'', '',r['code2'],r['possible_range'],r['coding_notes'],r['notes_comparability'],
       r['conf'],r['similar_items'],'',r['hcap_studies'],r['status'],r['admin'],r['waves'],r['level'],prio(r),ver(r)] for r in R]
ws=out.create_sheet('Items')
sheet(ws,cols,data,[8,38,10,16,22,8,26,40,10,8,10,10,30,55,14,14,10,30,24,40,24,12,10,22])
dv=DataValidation(type='list',formula1='"Proposed anchor – for Delphi,New COSMIC item – link to be decided,Agreed anchor,Rejected – not an anchor"',allow_blank=True); ws.add_data_validation(dv); dv.add(f'S2:S{ws.max_row}')
pf={'High':'F8CBAD','Medium':'FFE699','Low':'C6EFCE'}
for row in ws.iter_rows(min_row=2):
    c=row[22]; c.fill=PatternFill('solid',fgColor=pf[c.value])
    if row[0].value.startswith('u'): row[0].font=Font(bold=True,color='1F4E78')

# Coverage
studies=['MYHAT','MAS','KLOSCAD','HELIAD','SPAH']
codes=sorted({r['item'] for r in R},key=lambda c:(c[1],c))
cov=out.create_sheet('Coverage')
hdr=['item','item_label','domain','HCAP code?','HRS-HCAP conf (max)']+studies+['n cohorts']
rowsC=[]
for c in codes:
    rr=[r for r in R if r['item']==c]
    confs=[r['conf'] for r in rr if r['conf'] is not None]
    line=[c,lab(c),dom(c)[0],'HCAP' if c.startswith('u') else 'COSMIC-new',(max(confs) if confs else '')]
    for s in studies:
        hit=[r for r in rr if r['study']==s]
        line.append(('✓' if hit[0]['level']=='Item' else '◐') if hit else '')
    line.append(len({r['study'] for r in rr})); rowsC.append(line)
sheet(cov,hdr,rowsC,[8,48,18,12,10]+[10]*len(studies)+[10])
for row in cov.iter_rows(min_row=2):
    n=row[-1].value
    row[-1].fill=PatternFill('solid',fgColor='C6EFCE' if n>=3 else ('FFE699' if n==2 else 'FFFFFF'))
cov.append([]); cov.append(['✓ = item-level source; ◐ = subtest/total score. Rows with ≥2 cohorts are candidate within-COSMIC links; HCAP codes also link out to HCAP studies.'])

# Code registry
reg=out.create_sheet('Code_registry')
rr=[]
for c in codes:
    rr.append([c,lab(c),*dom(c),'HCAP (reused)' if c.startswith('u') else 'COSMIC-new',', '.join(sorted({r['study'] for r in R if r['item']==c},key=lambda s:order[s])),hstud(c) if c.startswith('u') else '',
               ' '.join(sorted({x for r in R if r['item']==c for x in r['similar_items'].split()}))])
sheet(reg,['item','label','domain','subdomain','origin','COSMIC pilot cohorts','HCAP studies with code','similar_items'],rr,[8,50,18,26,14,36,50,20])

# Studies
st=out.create_sheet('Studies')
sheet(st,['study','Title','Country','Battery / instruments mapped','Level of data','Files used','Notes'],[
 ['MYHAT','Monongahela-Youghiogheny Healthy Aging Team','USA','MMSE (items), WMS-R Logical Memory (lines), Fuld OME, Face-Name, WMS-R Visual Reproduction, TMT A/B, Digit span forward, animal + P/S fluency, Boston Naming, IU Token Test, Block Design, Benton VFD, clock (15-pt), RMET','Item','COSMIC_CogHarmo_MYHAT.csv; MYHAT_CogHarmonization_DataDictionary.xlsx','Supplied for cognitive harmonisation'],
 ['HELIAD','Hellenic Longitudinal Investigation of Aging and Diet','Greece','MMSE total, Greek VLT, MCG Complex Figure, JLO, TMT A/B, semantic (objects) + phonemic (alpha) fluency, naming, repetition, comprehension, anomalous sentences, months F/B, clock','Subtest/total','HELIAD A_total_GBD.sav; HELIAD B_total_GBD.sav','Supplied for GBD project; protocol HELIAD_protocol_eng.doc in folder. ALBION (same group/battery) is a candidate addition.'],
 ['MAS','Sydney Memory and Ageing Study','Australia','MMSE, Digit Symbol-Coding, TMT A/B, WMS-III Logical Memory Story A, RAVLT, Benton Visual Retention (recognition), BNT-30, animal and F-A-S fluency, Block Design (WAIS-R); TICS by telephone between waves; NART and Grooved Pegboard not mapped','Not yet known','None yet – battery from Sachdev et al. 2010, Int Psychogeriatr 22(8):1248–64','Data access pending. CHeBA cohort; participants aged 70–90 at entry, English-speaking.'],
 ['KLOSCAD','Korean Longitudinal Study on Cognitive Aging and Dementia','South Korea','CERAD-K (MMSE-KC, fluency, BNT-15, word list, praxis, TMT A/B), digit span, FAB, CLOX','Subtest/total','KLOSCAD GBD.sav','LOSHAK (Korean HCAP) is the regional HCAP bridge'],
 ['SPAH','São Paulo Ageing & Health Study','Brazil','10/66 CSI-D cognitive items + CERAD 10-word list + animals + story','Item','CSI-D.sav','MexCog/ChileCog are regional HCAP bridges. MYNAH (India) used the same protocol and is in the first expansion batch.'],
],[10,40,12,60,12,40,40])

# Domains
dm=out.create_sheet('Domains_and_subdomains')
sheet(dm,['Domain_or_Broad_ability','Subdomain_or_Narrow_ability','Notes'],[[a,b,''] for a,b in [
 ('Orientation','Orientation_time'),('Orientation','Orientation_place'),('Orientation','Orientation'),('Memory','Memory_episodic_immediate'),('Memory','Memory_episodic_delayed'),('Memory','Memory_recognition'),
 ('Language_fluency','Language_fluency'),('Attention','Attention'),('Speed','Speed'),('Attention_speed','Attention_speed'),('Executive','Executive_set_shifting'),('Executive','Executive_sustained_attention'),
 ('Visuospatial','Visuospatial'),('(not specified)','(not specified)')]]+[['','','Copied from the HCAP resource. Global/total scores (c9xx) are coded (not specified).']],[24,32,60])

# Excluded
ex=out.create_sheet('Excluded')
sheet(ex,['study','variables','reason'],[
 ['MYHAT','CDR MEM ORI JPS CA HH PC CDRBOXTOT','Clinical rating, not a cognitive test'],
 ['MYHAT','NPTRAILA_ERR NPTRAILA_PTS NPTRAILB_ERR NPTRAILB_PTS traila trailb NPDIGIT_BAS NPDIGIT_MAX NPFuld_T123Intr NPFuld_IntrDel INTRUSIONS_T1-3 NPBOSTON_C TOTAL_FACIAL_REC TOTAL_CFL TOTAL_MCN','Process/secondary scores (primary-score scope); keep for recode pass'],
 ['MYHAT','NPRMET_TOT Q1RMET–Q10RMET','Reading the Mind in the Eyes – social cognition, outside HCAP domains'],
 ['HELIAD','ll1–ll10 int/per/sim; Encodingdefindex1 Consolidationdefin Retrievaldefindex ISDAforgetting Recognrecalldiscr; vf* related/cluster/switch/err/per; ST_D_2_* percentiles; MonthsRatio TMTratio; *TR truncated times','Process / derived scores'],
 ['HELIAD','z* variables; ZME ZEX ZVS ZAS; MCI* ; G16psy–G20psy; Standardized_MMSE','Cohort-derived z/domain scores – useful later as a comparator for Delphi domain assignments'],
 ['HELIAD','functionalilliterac Readletters1 Readwords1 Readingsyllables1 Read_matchsentence','Literacy measures – keep as covariates for DIF, not cognitive indicators'],
 ['HELIAD','G1 G2 G3 (CDR)','Clinical rating'],
 ['KLOSCAD','*_Zscore; K3F/K3B z-scores; secondary/tertiary BNT totals','Derived scores'],
 ['KLOSCAD','K1SevereCognitiveImpairmentRatingScale_SCIRSscore','Severe-impairment scale administered selectively – not a population indicator'],
 ['KLOSCAD','CDR SumofboxesofCDR DAD*','Clinical/functional ratings'],
 ['SPAH','cogscore immed orientti orientsp objname mem langexpr langcomp language orientat dfscore cogcase dfcase imp* infmem* relscore trialno name(registration) and informant items','CSI-D derived subscales, algorithm outputs, informant interview'],
 ['MAS','National Adult Reading Test (NART)','Estimate of premorbid ability, not a current cognitive domain – keep as a covariate'],
 ['MAS','Grooved Pegboard','Fine motor speed, outside HCAP domains'],
],[14,80,60])

# Open questions
oq=out.create_sheet('Open_questions')
sheet(oq,['#','study','question','why it matters','owner'],[
 [1,'MYHAT','HRS-HCAP used WMS-IV Logical Memory Story B (confirmed from the HCAP literature). Is MYHAT WMS-R Story A equivalent enough in wording and scoring to anchor?','Decides whether u203/u207 are anchors or new codes','Neuropsychologist'],
 [2,'MYHAT / HRS-HCAP','Are the MMSE 3-word sets the same in MYHAT and HRS-HCAP?','u258/u209 confidence',''],
 [3,'KLOSCAD','Are CERAD-K words shown on cards (visual) or read aloud?','u201/u210 vs u202/u211',''],
 [4,'KLOSCAD','Units of J9 TMT A/B "score" (seconds?) and the TMT-B script used','u401/u303 recode',''],
 [5,'KLOSCAD','Can raw digit span forward/backward be supplied?','Link to u309/u310',''],
 [6,'HELIAD','Confirm list-learning variable meanings (ll6–ll10, lld1, lltd1, llts1, llta1). The protocol file supplied covers only the clinical interview, so this needs the HELIAD team.','c261–c263','HELIAD team'],
 [7,'HELIAD','Can item-level MMSE be supplied?','Would add ~20 HCAP anchors for Greece',''],
 [8,'HELIAD','Score ranges for repetition and comprehension; where are the Graphical Sequence, Motor Programming (go/no-go) and Vocabulary tests? They are in the published battery but not in the files supplied.','c537–c538; missing executive tests',''],
 [9,'SPAH','Is CSI-D story recall immediate or delayed, and its range?','c242 subdomain',''],
 [10,'SPAH','Season item in a subtropical site – keep as an anchor?','u116 DIF',''],
 [11,'MAS','Is the MMSE held at item level?','Would add about 20 HCAP anchors and direct links with MYHAT and SPAH','MAS team'],
 [12,'MAS','Was Logical Memory immediate recall also recorded? The paper reports delayed recall only.','u203','MAS team'],
 [13,'MAS','Which 30 Boston Naming items were used, and are item scores held?','Item-level link to MYHAT (60 items scored separately)','MAS team'],
 [14,'MAS','Are the F, A and S fluency scores held separately?','Letter S could link to MYHAT','MAS team'],
 [15,'MAS','Which TICS version was used by telephone, and are item scores held?','u502, u504, u701','MAS team'],
 [16,'MAS','Which tests were added or dropped in later waves?','The paper describes wave 1 only','MAS team'],
 [17,'All','Should ALBION (same battery as HELIAD) be added?','More Greek data; same codes',''],
],[5,16,70,40,12])

cl=out.create_sheet('Changelog')
sheet(cl,['version','date','change'],[
 ['v0.1','4 Nov 2026','First build: 152 rows, 95 codes.'],
 ['v0.2','13 Nov 2026','All source variables re-checked against file headers (MYHAT csv, HELIAD A/B, KLOSCAD, MYNAH, SPAH CSI-D, Uganda xls). Added Source verified column.'],
 ['v0.2','13 Nov 2026','FIX MYNAH u115: variable is city, not town (town does not exist in MYNAH.sav).'],
 ['v0.2','13 Nov 2026','ADD MYNAH c545 (pray) and c546 (chemist): both exist in MYNAH and were missed in v0.1.'],
 ['v0.2','13 Nov 2026','FIX u517 in MYNAH/SPAH: command is point to ceiling then floor, not window then door. Kept as u517 on HCAP precedent (MexCog/ChileCog), flagged High priority.'],
 ['v0.2','13 Nov 2026','FIX Uganda u508: elbow has no column in the data file. Marked NOT IN FILE.'],
 ['v0.2','13 Nov 2026','UPDATE MYHAT u203/u207: HRS-HCAP story confirmed as WMS-IV Story B; remaining question is equivalence with WMS-R Story A.'],
 ['v0.2','13 Nov 2026','UPDATE HELIAD from the published battery description: GVLT structure, BNT-15 (BDAE short form), JLO 10-item primary score (source changed to jlo1stdiades), repetition/comprehension sources, HELIAD own domain assignments noted where they differ from HCAP.'],
 ['v0.2','13 Nov 2026','UPDATE CERAD and TMT notes with HRS-HCAP administration details from the HRS 2016 HCAP protocol summary.'],
 ['v0.3','23 Nov 2026','Pilot cohorts revised: MYNAH and Uganda removed (moved to the first expansion batch); Sydney MAS added.'],
 ['v0.3','23 Nov 2026','ADD MAS: 16 rows drafted from the published baseline battery (Sachdev et al. 2010); marked NO DATA YET until the data dictionary is available.'],
 ['v0.3','23 Nov 2026','ADD codes c257–c259 (RAVLT), c267 (Benton recognition), c422 (Digit Symbol-Coding), c547 (BNT-30), c548 (F-A-S fluency), c629 (Block Design WAIS-R). REMOVE c121 (MYNAH only).'],
 ['v0.3','23 Nov 2026','UPDATE SPAH notes that referred to MYNAH and Uganda.'],
],[8,14,120])
out._sheets=[out[n] for n in ['ReadMe','Items','Coverage','Code_registry','Studies','Domains_and_subdomains','Excluded','Open_questions','Changelog']]
out.save(OUT)
print(len(R),'rows;',len(codes),'codes;',sum(c.startswith('u') for c in codes),'HCAP codes')
print(collections.Counter(r['study'] for r in R))

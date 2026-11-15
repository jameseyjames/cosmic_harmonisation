"""Builds (1) the REDCap data dictionary for the pilot Delphi Round 1 (v2) and (2) the rater-view preview page.
Usage: python delphi/build_redcap.py"""
import csv,json,os,html
from cards import *
HERE=os.path.dirname(os.path.abspath(__file__)); OUT=HERE
HEAD=["Variable / Field Name","Form Name","Section Header","Field Type","Field Label","Choices, Calculations, OR Slider Labels","Field Note",
"Text Validation Type OR Show Slider Number","Text Validation Min","Text Validation Max","Identifier?","Branching Logic (Show field only if...)",
"Required Field?","Custom Alignment","Question Number (surveys only)","Matrix Group Name","Matrix Ranking?","Field Annotation"]
FORM="delphi_round_1"; rows=[]
def f(name,ftype,label,choices="",section="",note="",req="",align="",valid="",vmin="",vmax="",branch="",annot=""):
    rows.append([name,FORM,section,ftype,label,choices,note,valid,vmin,vmax,"",branch,req,align,"","","",annot])
ch=lambda opts:" | ".join(f"{c}, {l}" for c,l in opts)
seq=lambda labels:[(i,l) for i,l in enumerate(labels,1)]
E=html.escape
def tr(k,v,color=""): return f'<tr><td style="vertical-align:top;padding:4px 14px 4px 0;color:#4a5a66;"><b>{k}</b></td><td style="vertical-align:top;padding:4px 0;{color}">{E(v)}</td></tr>'
def panel(c):
    r=tr("Study",f"{c['cohort']}, {c['place']}")+tr("Participants",c['people'])+tr("Language",c['lang'])+tr("What the participant does",c['task'])+tr("How it is given",c['admin'])+tr("Format",c['fmt'])+tr("Scoring",c['score'])
    if c['unconf']: r+=tr("Not yet confirmed",c['unconf'],"color:#8a5a00;")
    r+=tr("Source",c['src'],"color:#4a5a66;font-size:13px;")
    return ('<div style="background:#f2f5f7;border:1px solid #c5d0d8;border-radius:6px;padding:14px 16px;font-weight:normal;">'
            '<div style="font-size:11px;letter-spacing:0.08em;text-transform:uppercase;color:#4a5a66;">Reference panel: the test you are judging</div>'
            f'<div style="font-size:18px;font-weight:bold;margin:2px 0 8px 0;">{E(c["test"])}</div><table style="border-collapse:collapse;">{r}</table></div>')
def refpanel(r):
    return ('<div style="background:#fbf6ea;border:1px solid #dccfa8;border-radius:6px;padding:12px 16px;font-weight:normal;">'
            '<div style="font-size:11px;letter-spacing:0.08em;text-transform:uppercase;color:#6b5a2a;">Comparison item</div>'
            f'<div style="font-weight:bold;margin:2px 0 4px 0;">{E(r["name"])}</div>{E(r["desc"])}</div>')
DEFS="<br>".join(f"<b>{l}:</b> {d}." for _,l,d in DOMAINS)
DOM=[(c,l) for c,l,_ in DOMAINS]
f("record_id","text","Record ID")
f("intro","descriptive",INTRO,section="Before you start")
f("consent","radio","I have read the information above and agree to take part.",ch([(1,"Yes")]),req="y")
f("panel_code","text","Your panellist code",note="Sent to you by email. Please do not enter your name.",req="y")
f("discipline","radio","Your main discipline",ch(seq(["Clinical neuropsychology","Psychometrics / biostatistics","Epidemiology","Psychiatry, neurology or geriatric medicine","Speech and language pathology","Other"])),req="y")
f("years_exp","radio","Years working with cognitive assessment of older adults",ch(seq(["Less than 5","5 to 10","11 to 20","More than 20"])),req="y",align="LH")
f("settings_exp","notes","Countries, languages or cultural settings in which you have direct experience of cognitive assessment",note="Optional")
f("domain_defs","descriptive",'<div style="font-weight:normal;"><b>The six domains used in this questionnaire</b><br>'+DEFS+'<br><i>These definitions are repeated under the first question on every page.</i></div>')
n=len(CARDS)
for i,c in enumerate(CARDS,1):
    p=f"c{i:02d}"
    f(p+"_panel","descriptive",panel(c),section=f"Test {i} of {n}")
    f(p+"_domain","radio","Which cognitive domain does this version of the test <u>mainly</u> measure?",ch(DOM+DOMAIN_EXTRA),note=DEFS,req="y")
    f(p+"_domain_oth","text","Which domain?",branch=f"[{p}_domain] = '8'",req="y")
    f(p+"_second","checkbox","Does it also measure any other domain to a substantial degree?",ch(DOM+[(0,"No other domain")]),note="Tick all that apply.",req="y",annot="@NONEOFTHEABOVE=0")
    f(p+"_conf","radio","How confident are you in your choice of main domain?",ch(CONF),req="y",align="LH")
    f(p+"_bias","checkbox","Apart from the ability being measured, is a person's score on this version likely to be noticeably affected by any of these?",ch(BIAS),
      note="Tick all that apply. This tells us where to check for bias between studies.",req="y",annot="@NONEOFTHEABOVE=0")
    for k,r in enumerate(c['refs'],1):
        s=f"{p}_link{k}"
        f(f"{p}_refpanel{k}","descriptive",refpanel(r))
        f(s,"radio","Could the test in the reference panel be linked to this comparison item? In other words, would two people of the same ability be expected to get the same score on both?",ch(LINK),req="y")
        f(s+"_why","checkbox","What differs?",ch(REASONS),note="Tick all that apply.",branch=f"[{s}] = '2' or [{s}] = '3'")
    f(p+"_comment","notes","Comments",note="Optional. For example: what further information would change your answer?")
f("fb_minutes","text","About how many minutes did this take you?",section="About this questionnaire",valid="integer",vmin="1",vmax="600",req="y")
f("fb_info","notes","Did each reference panel give you enough information to judge? What was missing?")
f("fb_domains","notes","Were the domains and their definitions adequate? Would you add, split or merge any?")
f("fb_link","notes","Was the question about linking to a comparison item clear? How would you reword it?")
f("fb_other","notes","Any other comments")
os.makedirs(OUT,exist_ok=True)
with open(os.path.join(OUT,'COSMIC_Delphi_R1_REDCap_DataDictionary_v2.csv'),'w',newline='',encoding='utf-8-sig') as fh:
    w=csv.writer(fh); w.writerow(HEAD); w.writerows(rows)
names=[r[0] for r in rows]; assert len(names)==len(set(names)); assert all(len(x)<=26 and x==x.lower() for x in names),[x for x in names if len(x)>26]
for opts in (DOM,DOMAIN_EXTRA,CONF,BIAS,LINK,REASONS): assert all('|' not in l for _,l in opts)
nq=sum(1 for r in rows if r[3]!='descriptive')-1; nlink=sum(len(c['refs']) for c in CARDS)
print(len(rows),'fields;',nq,'questions; link questions',nlink,'; required per card 4 +links')
data=json.dumps(dict(cards=CARDS,domains=DOMAINS,extra=DOMAIN_EXTRA,conf=CONF,bias=BIAS,link=LINK,reasons=REASONS,intro=INTRO),ensure_ascii=False).replace('</','<\\/')
tpl=open(os.path.join(HERE,'preview_template.html'),encoding='utf-8').read()
WRAP='<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{margin:0}[hidden]{display:none!important}</style></head><body>\n%s\n</body></html>\n'
open(os.path.join(OUT,'rater_preview.html'),'w',encoding='utf-8').write(WRAP%tpl.replace('/*DATA*/null',data))

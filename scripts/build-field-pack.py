from pathlib import Path
import json, hashlib, shutil, math
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, A4, landscape
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, Color
from xml.sax.saxutils import escape

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'output/pdf'; OUT.mkdir(parents=True,exist_ok=True)
PUBLIC=ROOT/'public/field-pack'; PUBLIC.mkdir(parents=True,exist_ok=True)

tasks_data=json.loads((ROOT/'data/field-tasks.json').read_text())
tasks=tasks_data['tasks']
task_by_id={t['task_id']:t for t in tasks}
guides_data=json.loads((ROOT/'data/visual-guides.json').read_text())
guides=guides_data['guides']
guide_by_id={g['id']:g for g in guides}
conflicts=json.loads((ROOT/'data/field-language.json').read_text())['conflicts']

font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('KS',font)); pdfmetrics.registerFont(TTFont('KSB',bold))

INK=HexColor('#172b25'); MUTED=HexColor('#5b6962'); GREEN=HexColor('#193e35')
LINE=HexColor('#cdd5cf'); AMBER=HexColor('#b06f22'); WARN=HexColor('#fff3d8')
SOFT=HexColor('#edf1e7'); WATER=HexColor('#7396a4')

W,H=landscape(A3); M=13*mm
manifest_pages=[]; page_no=0
c=canvas.Canvas(str(OUT/'KS-Field-Pack-A3.pdf'),pagesize=(W,H),invariant=1)
c.setTitle('Kleines Schäferrad - Werkstatt- und Aufnahmeplan V2')
c.setAuthor('Kleines Schäferrad - gemeinsam dokumentiert')

def txt(s,x,y,size=12,b=False,color=INK):
    c.setFillColor(color); c.setFont('KSB' if b else 'KS',size); c.drawString(x,y,str(s))

def para(s,x,y,w,size=11,b=False,color=INK,leading=None):
    p=Paragraph(escape(str(s)),ParagraphStyle('p',fontName='KSB' if b else 'KS',fontSize=size,leading=leading or size*1.35,textColor=color))
    _,h=p.wrap(w,H); p.drawOn(c,x,y-h); return y-h

def header(code,title,subtitle='Arbeitsunterlage · offene Maße bleiben offen'):
    global page_no
    if page_no: c.showPage()
    page_no+=1
    manifest_pages.append({'page':page_no,'code':code,'title':title})
    c.setFillColor(HexColor('#fafbf7')); c.rect(0,0,W,H,fill=1,stroke=0)
    c.setStrokeColor(LINE); c.setLineWidth(.25*mm); c.line(M,H-25*mm,W-M,H-25*mm)
    txt('KLEINES SCHÄFERRAD',M,H-15*mm,10,True,GREEN)
    txt(code,W-M-35*mm,H-15*mm,9,True,MUTED)
    txt(title,M,H-39*mm,23,True,INK)
    txt(subtitle,M,H-48*mm,10,False,MUTED)
    c.line(M,21*mm,W-M,21*mm)
    txt(f'V2 · Blatt {page_no} · A3 quer · 07.10.2026',M,12*mm,8,False,MUTED)
    c.line(W-86*mm,13*mm,W-36*mm,13*mm); c.line(W-86*mm,11*mm,W-86*mm,15*mm); c.line(W-36*mm,11*mm,W-36*mm,15*mm)
    txt('50 mm · 100 %',W-87*mm,8*mm,7,False,MUTED)

def pt(panel,x,y):
    px,py,pw,ph=panel
    return px+x/100*pw, py+(100-y)/100*ph

def arrow(x1,y1,x2,y2,color=AMBER):
    c.setStrokeColor(color); c.setFillColor(color); c.setLineWidth(.55*mm); c.line(x1,y1,x2,y2)
    for xa,ya,xb,yb in [(x1,y1,x2,y2),(x2,y2,x1,y1)]:
        ang=math.atan2(yb-ya,xb-xa); L=3.2*mm
        p1=(xa+math.cos(ang+.48)*L,ya+math.sin(ang+.48)*L)
        p2=(xa+math.cos(ang-.48)*L,ya+math.sin(ang-.48)*L)
        c.line(xa,ya,*p1); c.line(xa,ya,*p2)

def draw_primitive(p,panel):
    style=p.get('style','solid')
    color={'solid':INK,'ghost':HexColor('#8b918b'),'unknown':AMBER,'water':WATER}.get(style,INK)
    c.setStrokeColor(color); c.setFillColor(Color(color.red,color.green,color.blue,alpha=.08) if style in ['ghost','unknown'] else Color(1,1,1,alpha=0))
    c.setLineWidth(.45*mm if style=='solid' else .3*mm)
    c.setDash(2.5,2) if style in ['ghost','unknown'] else c.setDash()
    typ=p['type']
    if typ=='line':
        a=pt(panel,p['x1'],p['y1']); b=pt(panel,p['x2'],p['y2']); c.line(*a,*b)
    elif typ=='rect':
        x1,y1=pt(panel,p['x'],p['y']); x2,y2=pt(panel,p['x']+p['w'],p['y']+p['h'])
        c.rect(x1,y2,x2-x1,y1-y2,fill=0,stroke=1)
    elif typ=='circle':
        x,y=pt(panel,p['cx'],p['cy']); _,yr=pt(panel,p['cx'],p['cy']+p['r']); xr,_=pt(panel,p['cx']+p['r'],p['cy'])
        c.ellipse(x-(xr-x),y-(y-yr),x+(xr-x),y+(y-yr),fill=0,stroke=1)
    elif typ in ['polyline','trapezoid']:
        points=p['points']; path=c.beginPath(); x,y=pt(panel,*points[0]); path.moveTo(x,y)
        for q in points[1:]: x,y=pt(panel,*q); path.lineTo(x,y)
        if typ=='trapezoid': path.close()
        c.drawPath(path,fill=0,stroke=1)
    elif typ=='arc':
        x,y=pt(panel,p['cx'],p['cy']); xr,_=pt(panel,p['cx']+p['r'],p['cy']); _,yr=pt(panel,p['cx'],p['cy']+p['r'])
        rX=xr-x; rY=y-yr
        c.arc(x-rX,y-rY,x+rX,y+rY,startAng=360-p['a1'],extent=p['a1']-p['a0'])
    c.setDash()

def draw_callout(q,panel):
    typ=q['type']; c.setFont('KSB',8)
    if typ=='measure':
        a=pt(panel,q['x1'],q['y1']); b=pt(panel,q['x2'],q['y2']); arrow(*a,*b)
        mx=(a[0]+b[0])/2; my=(a[1]+b[1])/2+3*mm
        c.setFillColor(WARN); c.roundRect(mx-9*mm,my-3.2*mm,18*mm,6.4*mm,2*mm,fill=1,stroke=0); txt(q['id'],mx-5*mm,my-1.7*mm,7,True,INK)
    elif typ=='photo':
        a=pt(panel,q['x'],q['y']); b=pt(panel,q['tx'],q['ty']); c.setStrokeColor(GREEN); c.setLineWidth(.4*mm); c.line(*a,*b)
        c.setFillColor(HexColor('#fafbf7')); c.setStrokeColor(GREEN); c.roundRect(a[0]-4*mm,a[1]-3*mm,8*mm,6*mm,1.2*mm,fill=1,stroke=1)
        c.circle(a[0],a[1],1.4*mm,fill=0,stroke=1); txt(q['id'],a[0]+5*mm,a[1]+1.5*mm,7,True,GREEN)
    elif typ in ['scan','datum']:
        a=pt(panel,q['x'],q['y']); c.setStrokeColor(GREEN); c.circle(*a,3*mm,fill=0,stroke=1); c.line(a[0]-4*mm,a[1],a[0]+4*mm,a[1]); c.line(a[0],a[1]-4*mm,a[0],a[1]+4*mm); txt(q['id'],a[0]+4*mm,a[1]+2*mm,7,True,GREEN)
    elif typ=='unknown':
        a=pt(panel,q['x'],q['y']); c.setStrokeColor(AMBER); c.setFillColor(WARN); c.circle(*a,4*mm,fill=1,stroke=1); txt('?',a[0]-1.5*mm,a[1]-2.4*mm,10,True,AMBER)

def draw_guide(g):
    ytop=H-60*mm; bottom=32*mm
    drawing=(M,bottom,238*mm,ytop-bottom)
    info=(M+248*mm,bottom,135*mm,ytop-bottom)
    c.setFillColor(HexColor('#fffdf8')); c.setStrokeColor(LINE); c.roundRect(drawing[0],drawing[1],drawing[2],drawing[3],4*mm,fill=1,stroke=1)
    for p in g['primitives']: draw_primitive(p,drawing)
    for q in g['callouts']: draw_callout(q,drawing)

    c.setStrokeColor(LINE); c.line(info[0],info[1],info[0],info[1]+info[3])
    x=info[0]+8*mm; y=info[1]+info[3]-2*mm; width=info[2]-12*mm
    txt('AUF DER ZEICHNUNG',x,y,8,True,MUTED); y-=7*mm
    for q in g['callouts']:
        color=AMBER if q['type'] in ['measure','unknown'] else GREEN
        txt(q['id'],x,y,8,True,color); y=para(q['label'],x+13*mm,y+2*mm,width-13*mm,8,False,INK)-3*mm
    y-=2*mm; c.setStrokeColor(LINE); c.line(x,y,width+x,y); y-=8*mm
    txt('NICHT VERGESSEN',x,y,8,True,MUTED); y-=6*mm
    for tid in g['tasks']:
        t=task_by_id[tid]
        bullet=t['title'].replace('STOPP: ','')
        y=para('• '+bullet,x,y,width,8,False,INK)-2*mm
    y-=3*mm
    txt('NOCH OFFEN',x,y,8,True,AMBER); y-=6*mm
    para(g['note'],x,y,width,8,False,MUTED)

def route_page():
    header('KS-A00','Werkstatt- und Aufnahmeplan','Die rote Linie: orientieren → aufnehmen → lösen → zuordnen → sichern')
    x=M; y=H-67*mm; width=W-2*M
    para('Dieser Plan ist keine Demontageanweisung. Er zeigt, welche Informationen verloren gehen können und wo sie vor, während oder nach dem Öffnen aufgenommen werden sollen.',x,y,width,12,False,INK)
    y-=25*mm
    phases=[
      ('1','VOR DEM LÖSEN','Orientierung, Referenzpunkte, Einbaulage, sichtbare Verbindungen.'),
      ('2','BEIM ÖFFNEN','Keil/Partner vorher, Kontaktflächen direkt danach.'),
      ('3','NACH DEM ÖFFNEN','Innenflächen, Tiefen, reale Paarungen und Varianten.'),
      ('4','NACH DEM AUSBAU','Teil-ID, Profil, Lagerplatz, Sicherung und offene Fragen.')
    ]
    cell=(width-3*8*mm)/4
    for i,(n,h,t) in enumerate(phases):
        xx=x+i*(cell+8*mm); c.setFillColor(HexColor('#fffdf8')); c.setStrokeColor(LINE); c.roundRect(xx,y-55*mm,cell,55*mm,4*mm,fill=1,stroke=1)
        txt(n,xx+6*mm,y-11*mm,18,True,AMBER); txt(h,xx+6*mm,y-23*mm,9,True,INK); para(t,xx+6*mm,y-29*mm,cell-12*mm,8,False,MUTED)
    y-=78*mm
    txt('ARBEITSBLÄTTER',x,y,9,True,MUTED); y-=9*mm
    for i,g in enumerate(guides):
        col=i%2; row=i//2; xx=x+col*(width/2); yy=y-row*17*mm
        txt(g['sheet'],xx,yy,9,True,GREEN); txt(g['title'],xx+25*mm,yy,9,False,INK)
    para('Regel: Erst fotografieren und Bezug markieren, dann lösen. Rohbilder unverändert behalten. Offene Stellen ausdrücklich offen lassen.',x,42*mm,width,10,True,INK)

def register_page():
    header('KS-A09','Teile, Ereignisse und Lagerorte','Reale IDs erst vergeben, wenn ein Teil wirklich gesehen und beschriftet wurde')
    cols=[('KS-ID / alte Marke',38),('so nennt ihr das Teil',58),('Einbaulage / Partner',82),('Ereignis / Lagerplatz',92),('Foto / Person',72)]
    x=M; y=H-66*mm; total=sum(w for _,w in cols)*mm
    xx=x
    for name,w in cols:
        para(name,xx+2*mm,y,w*mm-4*mm,8,True,INK); xx+=w*mm
    top=y-10*mm; bottom=42*mm
    c.setStrokeColor(LINE); xx=x
    for _,w in cols: c.line(xx,bottom,xx,top); xx+=w*mm
    c.line(xx,bottom,xx,top)
    for i in range(9):
        yy=top-i*(top-bottom)/8; c.line(x,yy,x+total,yy)
    para('Keile und Kleinteile bleiben bei ihrem Partner. Historische Marken nicht ersetzen, sondern zusätzlich zur neuen KS-ID notieren.',x,33*mm,total,9,False,MUTED)

def conflicts_page():
    header('KS-A10','Alte Angaben und offene Varianten','Nicht mitteln. Am realen Teil entscheiden – oder ausdrücklich offen lassen.')
    items=list(conflicts.items())
    x=M; y=H-66*mm; colw=(W-2*M-10*mm)/2
    for i,(cid,textv) in enumerate(items):
        col=i%2; row=i//2; xx=x+col*(colw+10*mm); yy=y-row*31*mm
        txt(cid,xx,yy,8,True,AMBER); para(textv,xx+20*mm,yy+2*mm,colw-20*mm,8,False,INK)
        c.setStrokeColor(LINE); c.line(xx,yy-19*mm,xx+colw,yy-19*mm)
        txt('Befund / Foto / Teil-ID: _______________________________',xx,yy-26*mm,7,False,MUTED)

def final_page():
    header('KS-A11','Vor dem Verlassen gemeinsam prüfen','Kein unbekanntes Restteil verschweigen · Sicherung wirklich öffnen')
    checks=[
      'Alle STOPP-Punkte entweder aufgenommen oder ausdrücklich blockiert.',
      'Reale Teile tragen ID, alte Marke, Partner und Lagerort.',
      'Keile und Befestiger sind keinem falschen Partner zugeordnet.',
      'Neue Innenflächen und Kontaktpaare sind fotografiert.',
      'Messwerte besitzen Endpunkte, Einheit, Werkzeug und Unsicherheit.',
      'Datumspunkte und Kontrollstrecken sind gesichert.',
      'Originalfotos und Scans liegen unverändert vor.',
      'Feldsicherung wurde auf einem zweiten Gerät geöffnet.',
      'Offene Fragen haben eine Person oder einen nächsten Termin.'
    ]
    x=M; y=H-67*mm; width=W-2*M
    for i,t in enumerate(checks):
        c.rect(x,y-3*mm,5*mm,5*mm,fill=0,stroke=1); txt(f'{i+1:02}',x+9*mm,y,8,True,AMBER); y=para(t,x+23*mm,y+2*mm,width-23*mm,11,False,INK)-9*mm
    txt('Was können wir später nicht mehr nachholen?',x,52*mm,11,True,INK); c.line(x,42*mm,W-M,42*mm); c.line(x,32*mm,W-M,32*mm)

route_page()
for g in guides:
    header(g['sheet'],g['title'],'Skizze und Aufnahmepunkte · keine Fertigungszeichnung')
    draw_guide(g)
register_page()
conflicts_page()
final_page()
c.save()

# compact A4 running plan: two pages maximum
aw,ah=landscape(A4)
a=canvas.Canvas(str(OUT/'KS-Einsatzleitung-A4.pdf'),pagesize=(aw,ah),invariant=1)
def aheader(title):
    a.setFillColor(HexColor('#fafbf7')); a.rect(0,0,aw,ah,fill=1,stroke=0)
    a.setFont('KSB',18); a.setFillColor(INK); a.drawString(12*mm,ah-18*mm,title)
    a.setFont('KS',8); a.setFillColor(MUTED); a.drawString(12*mm,ah-25*mm,'gleiche Aufgaben-IDs wie Web und A3-Plan · keine Demontagefreigabe')
aheader('Kleines Schäferrad · Ablauf vor Ort')
y=ah-37*mm
for i,t in enumerate(tasks[:12]):
    a.setFont('KSB',8); a.setFillColor(AMBER if t['stop_before_release'] else GREEN); a.drawString(12*mm,y,f"{i+1:02}")
    a.setFillColor(INK); a.drawString(24*mm,y,t['title'][:68])
    a.setFont('KS',7); a.setFillColor(MUTED); a.drawRightString(282*mm,y,tasks_data['timing_labels'][t['timing']])
    y-=10*mm
a.showPage(); aheader('Kleines Schäferrad · Fortsetzung und Abschluss')
y=ah-37*mm
for i,t in enumerate(tasks[12:],start=13):
    a.setFont('KSB',8); a.setFillColor(AMBER if t['stop_before_release'] else GREEN); a.drawString(12*mm,y,f"{i:02}")
    a.setFillColor(INK); a.drawString(24*mm,y,t['title'][:68])
    a.setFont('KS',7); a.setFillColor(MUTED); a.drawRightString(282*mm,y,tasks_data['timing_labels'][t['timing']])
    y-=10*mm
a.setFont('KSB',8); a.setFillColor(INK); a.drawString(12*mm,24*mm,'Abschluss: Sicherung auf zweitem Gerät geöffnet · Papier/Originalmedien mitgenommen · offene Punkte benannt')
a.save()

task_hash=hashlib.sha256((ROOT/'data/field-tasks.json').read_bytes()).hexdigest()
guide_hash=hashlib.sha256((ROOT/'data/visual-guides.json').read_bytes()).hexdigest()
manifest={
  'schema':'ks-field-pack/v2',
  'task_source':'data/field-tasks.json',
  'task_source_sha256':task_hash,
  'visual_source':'data/visual-guides.json',
  'visual_source_sha256':guide_hash,
  'task_ids':[t['task_id'] for t in tasks],
  'task_to_sheet':{tid:guide_by_id[gid]['sheet'] for tid,gid in guides_data['task_visual_map'].items()},
  'pages':manifest_pages,
  'format':'A3 landscape',
  'physical_instances_precreated':0
}
(ROOT/'docs/field-kit/field-pack-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
for p in OUT.glob('*.pdf'): shutil.copyfile(p,PUBLIC/p.name)
print('Generated',page_no,'A3 pages and 2 A4 pages from',len(guides),'visual guides /',len(tasks),'canonical tasks')

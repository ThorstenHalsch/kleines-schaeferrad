from pathlib import Path
import json,hashlib,shutil
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3,A4,landscape
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from xml.sax.saxutils import escape
ROOT=Path(__file__).resolve().parent.parent
out=ROOT/'output/pdf';out.mkdir(parents=True,exist_ok=True)
data=json.loads((ROOT/'data/field-tasks.json').read_text());tasks=data['tasks'];conflicts=json.loads((ROOT/'data/conflicts.json').read_text())['conflicts'];sketches=json.loads((ROOT/'docs/field-kit/model-projections.json').read_text())['views']
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('Field',font));pdfmetrics.registerFont(TTFont('FieldBold',bold))
W,H=landscape(A3);margin=14*mm; page=0; manifest=[];c=canvas.Canvas(str(out/'KS-Field-Pack-A3.pdf'),pagesize=(W,H),invariant=1);c.setTitle('Kleines Schäferrad - Field Pack FK-01');c.setAuthor('Kleines Schäferrad - gemeinsam dokumentiert')
def text(s,x,y,size=16,bold=False):c.setFont('FieldBold' if bold else 'Field',size);c.drawString(x,y,str(s).replace('–','-').replace('—','-'))
def para(s,x,y,width,size=16):
 p=Paragraph(escape(str(s).replace('–','-').replace('—','-')),ParagraphStyle('p',fontName='Field',fontSize=size,leading=size*1.4));_,h=p.wrap(width,H);p.drawOn(c,x,y-h);return y-h-6

def begin(title,code,subtitle='Arbeitsunterlage vor der Demontage - keine Fertigungsfreigabe'):
 global page
 if page:c.showPage()
 page+=1;manifest.append({'page':page,'code':code,'title':title});c.setStrokeColorRGB(0,0,0);c.setFillColorRGB(0,0,0);c.setLineWidth(.5*mm);c.rect(8*mm,8*mm,W-16*mm,H-16*mm);text('KLEINES SCHÄFERRAD / FIELD PACK',margin,H-22*mm,14,True);text(title,margin,H-37*mm,24,True);text(subtitle,margin,H-48*mm,13);c.setLineWidth(.25*mm);c.line(margin,H-54*mm,W-margin,H-54*mm);c.line(8*mm,24*mm,W-8*mm,24*mm);text(f'{code} | FK-01 | Blatt {page} | A3 quer | 07.10.2026',margin,15*mm,12);c.line(W-90*mm,16*mm,W-40*mm,16*mm);c.line(W-90*mm,14*mm,W-90*mm,18*mm);c.line(W-40*mm,14*mm,W-40*mm,18*mm);text('50 mm - 100 % drucken',W-91*mm,10*mm,9);return H-65*mm

def lines(x,y,width,n=4,gap=15*mm,label=None):
 if label:text(label,x,y,15,True);y-=8*mm
 c.setLineWidth(.18*mm)
 for _ in range(n):c.line(x,y,width+x,y);y-=gap
 return y

def draw_sketch(view,x,y,w,h):
 pts=[p for line in view['lines'] for p in line['points']];xmin=min(p[0] for p in pts);xmax=max(p[0] for p in pts);ymin=min(p[1] for p in pts);ymax=max(p[1] for p in pts);scale=min(w/(xmax-xmin),h/(ymax-ymin));c.saveState()
 for line in view['lines']:
  c.setDash(3,3) if line['unknown'] else c.setDash();c.setLineWidth(.18*mm if line['unknown'] else .45*mm);a,b=line['points'];c.line(x+(a[0]-xmin)*scale,y+(a[1]-ymin)*scale,x+(b[0]-xmin)*scale,y+(b[1]-ymin)*scale)
 c.restoreState()
y=begin('Wissen erhalten. Gemeinsam weitergeben.','FK-00')
y=para('Ihr habt dieses Rad erhalten. Diese Mappe hilft, Einbaulagen, Handgriffe und Erfahrungen so festzuhalten, dass sie weitergegeben werden können.',margin,y,W-2*margin,23)
y=para('Alte Zeichnungen und Arbeitsmodelle helfen beim Fragen. Entscheidend ist, was am echten Rad zu sehen, zu messen und aus Erfahrung bekannt ist. Offene Maße bleiben offen.',margin,y,W-2*margin,18)
y=lines(margin,y-12*mm,W-2*margin,3,22*mm,'Datum / Team / verantwortliche Person / Ort:')
para('Papier und Web verwenden dieselben TASK-, KS- und Ereignis-IDs. Aufnahmen in der App bleiben ungeprüfte Feldangaben. Keine Aufgabe ist eine Anweisung für eine sichere Demontagemethode: Ablauf und Freigabe bestimmen die fachkundigen Personen vor Ort.',margin,y+3*mm,W-2*margin,16)
y=begin('Rollen und gemeinsamer Ablauf','FK-01')
for head,body in [('1 / Ablauf bestimmen','Erfahrene Monteure bestimmen die tatsächliche Reihenfolge und benennen die Teile. Niemand löst für eine Modellannahme zusätzliche Verbindungen.'),('2 / Vor dem Lösen aufnehmen','Zweite Rolle führt Fotos, Maße und Ereignislog. STOPP-Aufträge vor jedem irreversiblen Schritt auf Vollständigkeit prüfen.'),('3 / Beim Öffnen zuordnen','Vorher und nachher dokumentieren. Beide Partnerflächen mit IDs zeigen. Historische Marken erhalten.'),('4 / Beschriften und sichern','Teil, Partner und Lagerplatz verbinden. Am Ende Export auf zweitem Gerät öffnen; Papier und Originalmedien mitnehmen.')]:
 text(head,margin,y,19,True);y=para(body,margin,y-9*mm,W-2*margin,17)-9*mm
lines(margin,y,W-2*margin,2,18*mm,'Rollen / Kürzel / Zuständigkeit:')
y=begin('Orientierung: Seite A / B bleiben vorläufig','FK-02')
left=margin;right=W/2+8*mm;cw=W/2-margin-16*mm
yl=para('X entlang der Welle, Z nach oben, Y rechtshändig quer: X × Y = Z. Land/Wasser, Fluss und Drehrichtung erst nach gemeinsamer Bestätigung eintragen.',left,y,cw,18)
for label in ['Seite A heißt vor Ort:','Seite B heißt vor Ort:','Bestätigt durch / Datum:','Fließrichtung / Rad steht oder dreht:']:yl=lines(left,yl-6*mm,cw,1,17*mm,label)
text('Lageskizze mit Blickpfeilen und Datum',right,y,17,True);c.rect(right,80*mm,cw,y-90*mm);text('KEIN MASSSTAB / keine Ist-Geometrie',right,68*mm,13)
# One canonical task per sheet. No task instructions are retyped in the PDF template.
for t in tasks:
 y=begin(t['title'],t['task_id'],data['timing_labels'][t['timing']]+' | '+t['priority']+' | '+t['family'])
 if t['stop_before_release']:
  c.setLineWidth(.7*mm);c.rect(margin,y-13*mm,W-2*margin,18*mm);text('STOPP - NOCH NICHT LÖSEN. Erst die Aufnahmen sichern.',margin+4*mm,y-7*mm,20,True);y-=25*mm
 cw=(W-3*margin)/2;right=2*margin+cw;yl=y;yr=y
 for heading,body in [('Warum jetzt?',t['irreversible_loss']),('So aufnehmen',t['instruction']),('Fotoansichten',' / '.join(t['photo_views'])),('Messendpunkte',' → '.join(t['measurement_endpoints'])),('Werkzeug',', '.join(t['tools']))]:
  text(heading,margin,yl,16,True);yl=para(body,margin,yl-6*mm,cw,16)-1*mm
 text('Teil-ID / alte Marke / Person / Ereignis',right,yr,16,True);yr=lines(right,yr-12*mm,cw,2,14*mm)
 text('Ergebnis / Bildnamen / Messskizze',right,yr,16,True);yr=lines(right,yr-12*mm,cw,3,14*mm)
 yr=para('Messwert: ________ Einheit: ____  ± ________',right,yr+5*mm,cw,15);yr=para('Endpunkte / Werkzeug: ____________________',right,yr,cw,15)
 bottom=min(yl,yr)-3*mm
 # Questions and acceptance in full-width dedicated low strip.
 bottom=min(bottom,105*mm)
 if bottom<74*mm: raise RuntimeError('Task layout overflow '+t['task_id']+' '+str(bottom/mm))
 c.line(margin,bottom,W-margin,bottom)
 by=para('Fragen: '+' / '.join(t['questions']),margin,bottom-5*mm,W-2*margin,16)
 by=para('Fertig, wenn: '+t['acceptance_evidence'],margin,by,W-2*margin,16)
 text('Status:  OFFEN / IN ARBEIT / AUFGENOMMEN, UNGEPRÜFT / BLOCKIERT, UNBEKANNT',margin,33*mm,12)
 # Internal evidence remains traceable, not printed as current dimensional truth.
 text('Bezug: '+', '.join(t['source_refs']),margin,27*mm,10)
for view in sketches:
 y=begin('Arm / Welle - alternative Arbeitsdarstellung','FK-H-'+view['id'],'UNGEPRÜFT | Form: '+view['shape']+' | axiale Lage: '+view['layers'])
 draw_sketch(view,margin+10*mm,95*mm,W*.55,130*mm)
 x=W*.63;cw=W-x-margin
 yy=para('Die gestrichelten Innenzonen bleiben unbekannt. Kein Zapfen und keine Mortise ist erfunden. Abstände und Kröpfung sind reine Darstellungswerte.',x,y,cw,18)
 yy=para('TASK-ARM-BEFORE / TASK-ARM-RELEASE / TASK-MORTISE / TASK-ARM-PROFILE',x,yy,cw,16)
 lines(x,yy-9*mm,cw,4,20*mm,'So sieht es wirklich aus:')
 para('Drei durchgehende Hölzer / sechs Enden je Kranz sind die historische Arbeitshypothese. Reale Endpaare und axialer Verlauf bleiben bis zur Aufnahme offen. Perspektivische Drahtprojektion aus derselben Geometrie wie die Werkstatt; keine Fertigungszeichnung.',margin,83*mm,W-2*margin,17)
# Preserve all conflicts; one comparison sheet per group of three.
for start in range(0,len(conflicts),3):
 y=begin('Alte Angaben vergleichen - offen lassen','FK-V-'+str(start//3+1))
 for item in conflicts[start:start+3]:
  text(item['id']+' / '+item['resolution_capture'],margin,y,16,True);y=para(json.loads((ROOT/'data/field-language.json').read_text())['conflicts'][item['id']],margin,y-7*mm,W-2*margin,18);y=para('Quellen: '+', '.join(item['sources'])+' | Keine ausgewählte Ist-Variante.',margin,y,W-2*margin,12);y=lines(margin,y-6*mm,W-2*margin,1,16*mm,'Reales Teil / Befund / Bild / Person:')-7*mm
# Blank physical registers - no verified instances seeded.
for code,title,heads in [('FK-R1','Reale Teile / historische Marken',['KS-ID / alte Marke','Lokaler Name / Zustand','Einbauposition / Partner','Person / Foto']),('FK-R2','Ereignisse beim Öffnen',['Event / Uhrzeit','Teil / Partner / Richtung','Vorher / nachher / Kontaktfoto','Person / nächster freier Teil']),('FK-R3','Lagerorte / bleibende Zuordnung',['KS-ID / Befestiger','Ausbauereignis','Lagerort / Behälter','Kontrolle / Person']),('FK-R4','Offene Punkte / nächste Verantwortung',['Aufgabe / reales Teil','Was fehlt oder widerspricht?','Wer klärt es / wann?','Foto / Ablage / Bemerkung'])]:
 y=begin(title,code);cw=(W-2*margin)/4
 for i,h in enumerate(heads):para(h,margin+i*cw+3*mm,y,cw-6*mm,15)
 top=y-20*mm;bottom=45*mm;c.setLineWidth(.25*mm)
 for i in range(5):c.line(margin+i*cw,bottom,margin+i*cw,top)
 for j in range(7):yy=top-j*(top-bottom)/6;c.line(margin,yy,W-margin,yy)
 text('KS-ARM / KS-KRU / KS-KUM / KS-PAD / KS-KEI-NNN | Reale IDs erst am Teil vergeben.',margin,33*mm,13)
y=begin('Aufgabenstand am Ende gemeinsam abgleichen','FK-END')
for t in tasks:
 if y<42*mm:y=begin('Aufgabenstand - Fortsetzung','FK-END-2')
 c.rect(margin,y-3*mm,4*mm,4*mm);text(t['task_id']+'  '+t['title'],margin+8*mm,y,14);y-=9*mm
c.save()
# A4 compact leadership sheet derived from the same ordered task dataset.
w,h=landscape(A4);a=canvas.Canvas(str(out/'KS-Einsatzleitung-A4.pdf'),pagesize=(w,h),invariant=1);a.setTitle('Einsatzleitung - Kleines Schäferrad');a.setFont('FieldBold',20);a.drawString(12*mm,h-18*mm,'Kleines Schäferrad / Einsatzleitung');a.setFont('Field',11);a.drawString(12*mm,h-26*mm,'FK-01 | gleiche Aufgaben-IDs wie Web und A3-Mappe | keine Demontage- oder Fertigungsfreigabe')
y=h-38*mm
for t in tasks:
 a.setFont('FieldBold',10);a.drawString(12*mm,y,t['task_id']);a.setFont('Field',10);a.drawString(55*mm,y,t['title']);a.setFont('Field',8);a.drawString(224*mm,y,data['timing_labels'][t['timing']]);y-=6.6*mm
a.setFont('Field',10);a.drawString(12*mm,17*mm,'Rollen: ____________________ / ____________________   Datum: __________   Export geöffnet / Papier mitgenommen: ______');a.save()
manifest={'schema':'ks-field-pack/v1','task_source':'data/field-tasks.json','task_source_sha256':hashlib.sha256((ROOT/'data/field-tasks.json').read_bytes()).hexdigest(),'model_source':'src/workbench/geometry.mjs','task_ids':[t['task_id'] for t in tasks],'pages':manifest,'format':'A3 landscape','minimum_task_body_pt':16,'physical_instances_precreated':0}
(ROOT/'docs/field-kit/field-pack-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
public=ROOT/'public/field-pack';public.mkdir(exist_ok=True)
for f in out.glob('*.pdf'):shutil.copyfile(f,public/f.name)
print('Generated',page,'A3 pages and one A4 leadership sheet from',len(tasks),'canonical tasks')

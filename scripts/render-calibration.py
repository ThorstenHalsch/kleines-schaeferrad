"""Deterministic offscreen EGL renders of the exported Three.js triangles; no artist redraws."""
import os,json,hashlib,math
from pathlib import Path
import numpy as np
import moderngl
from PIL import Image,ImageDraw,ImageFont
exec((Path(__file__).parent/'safe-image-write.py').read_text())
ROOT=Path(__file__).resolve().parents[1];TMP=Path('/tmp/ks-calibration');OUT=ROOT/'output/calibration/ITER-001';OUT.mkdir(exist_ok=True,parents=True)
W,H=1440,860
ctx=moderngl.create_standalone_context(backend='egl');ctx.enable(moderngl.DEPTH_TEST)
prog=ctx.program(vertex_shader='''#version 330
in vec3 position;in vec3 normal;in vec3 color;uniform mat4 vp;uniform mat4 model;out vec3 n;out vec3 c;out vec3 p;
void main(){vec4 w=model*vec4(position,1);p=w.xyz;n=mat3(model)*normal;c=color;gl_Position=vp*w;}
''',fragment_shader='''#version 330
in vec3 n;in vec3 c;in vec3 p;out vec4 frag;uniform vec4 clip;uniform int truth;uniform int water;uniform vec3 eye;
void main(){if(dot(clip.xyz,p)+clip.w>0.00001)discard;vec3 nn=normalize(n);if(!gl_FrontFacing)nn=-nn;
float diffuse=max(dot(nn,normalize(vec3(-3,-4,8))),0.0);float rim=max(dot(nn,normalize(vec3(4,2,3))),0.0);
float grain=truth==1?1.0:0.94+0.05*sin(320.0*p.x+4.0*sin(14.0*p.z))+0.015*sin(1040.0*p.x+7.0*p.y);
vec3 col=c*(0.48+0.48*diffuse+0.14*rim)*grain;
if(water==1){float ripple=sin(p.y*23+p.x*8)*sin(p.x*4-p.y*7);col=vec3(.34,.52,.58)*(0.90+.08*ripple);}
if(truth==0&&water==0&&p.z < -1.95)col*=.70;
frag=vec4(pow(max(col,vec3(0)),vec3(.85)),1);}
''')
fbo=ctx.simple_framebuffer((W,H),components=3,samples=4);resolved=ctx.simple_framebuffer((W,H),components=3)
fontpath='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
font=lambda n:ImageFont.truetype(fontpath,n)
cache={}
def load(name):
 if name not in cache:
  data=np.fromfile(TMP/f'{name}.bin',dtype='f4').reshape(-1,9);buf=ctx.buffer(data.tobytes());vao=ctx.vertex_array(prog,[(buf,'3f 3f 3f','position','normal','color')]);meta=json.loads((TMP/f'{name}.json').read_text());cache[name]=(vao,meta,data,buf)
 return cache[name]
def normalize(x):return x/np.linalg.norm(x)
def matrix(cam):
 eye=np.array(cam['eye'],float);target=np.array(cam['target'],float);f=normalize(target-eye);up=np.array([0.,0,1.]);
 if abs(np.dot(f,up))>.999:up=np.array([0.,1.,0.])
 right=normalize(np.cross(f,up));up=np.cross(right,f);v=np.eye(4);v[0,:3]=right;v[1,:3]=up;v[2,:3]=-f;v[:3,3]=-v[:3,:3]@eye
 h=cam['height'];w=h*W/H;p=np.diag([2/w,2/h,-2/100,1.]);p[2,3]=-1
 return (p@v).astype('f4')
def select(m,f):
 fam=m.get('family','');name=m['name'];slot=m.get('slot',-1)
 if f=='all':return True
 if f=='moving':return not m.get('stationary')
 if f=='shaft-arms':return fam in ['COMP-SHAFT','COMP-ARMS']
 if f.startswith('bearing'):return (fam in ['COMP-SHAFT','COMP-BEARINGS','COMP-BEARING-STANDS']) and (fam=='COMP-SHAFT' or ('-1' in name if f.endswith('land') else '-1' not in name))
 if f=='rim-detail':return (fam=='COMP-KRUEMMLINGE' and 'LAND' in name) or ('RIM-PIN-LAND' in name)
 if f=='local':return slot==0 or fam=='COMP-KRUEMMLINGE' and 'LAND' in name
 if f=='cluster':return 0<=slot<=2 or fam=='COMP-KRUEMMLINGE' and 'LAND' in name
 if f=='frame':return m.get('stationary') and fam!='COMP-TROUGH'
 if f=='trough':return fam=='COMP-TROUGH' or 0<=slot<=2
 if f=='reference':return True
 return False
waterdata=np.array([[-7,-8,-1.95,0,0,1,.4,.6,.7],[7,-8,-1.95,0,0,1,.4,.6,.7],[7,8,-1.95,0,0,1,.4,.6,.7],[-7,-8,-1.95,0,0,1,.4,.6,.7],[7,8,-1.95,0,0,1,.4,.6,.7],[-7,8,-1.95,0,0,1,.4,.6,.7]],dtype='f4')
wb=ctx.buffer(waterdata.tobytes());wv=ctx.vertex_array(prog,[(wb,'3f 3f 3f','position','normal','color')])
def render(name,cam,truth=False,angle=0,operation=False):
 vao,meta,data,buf=load(name);fbo.use();fbo.clear(.951,.946,.928,1,depth=1);prog['vp'].write(matrix(cam).T.tobytes());prog['model'].write(np.eye(4,dtype='f4').T.tobytes());prog['clip'].value=tuple(cam.get('clip',[0,0,0,0]));prog['truth'].value=int(truth);prog['water'].value=0
 # eye is optimized out on some GL implementations.
 spin=np.eye(4,dtype='f4');spin[1:3,1:3]=[[math.cos(angle),-math.sin(angle)],[math.sin(angle),math.cos(angle)]]
 for m in meta:
  if not select(m,cam.get('filter','all')):continue
  prog['model'].write((np.eye(4,dtype='f4') if m.get('stationary') else spin).T.tobytes());ctx.wireframe=bool(truth and m.get('pitchStatus')=='candidate-not-truth');vao.render(vertices=m['count'],first=m['first']);ctx.wireframe=False
 if operation and not truth:
  prog['model'].write(np.eye(4,dtype='f4').T.tobytes());prog['water'].value=1;wv.render();prog['water'].value=0
 ctx.copy_framebuffer(resolved,fbo);im=Image.frombytes('RGB',(W,H),resolved.read(components=3,alignment=1)).transpose(Image.Transpose.FLIP_TOP_BOTTOM);return im

def plate(im,title,subtitle,truth=False,note='',footer=''):
 page=Image.new('RGB',(1440,1040),'#faf9f5');page.paste(im,(0,110));d=ImageDraw.Draw(page)
 d.text((38,20),title,font=font(27),fill='#24333b');d.text((38,61),subtitle,font=font(17),fill='#52646b')
 d.text((38,978),note,font=font(16),fill='#35434b');d.text((38,1009),footer or 'ITER-001 | Baseline V3 | Rekonstruktionskoordinaten, kein bestätigtes Ist-Aufmaß',font=font(14),fill='#66757b')
 if truth:
  d.rectangle((1010,26,1030,46),fill='#668e94');d.text((1042,27),'Experten-Topologie',font=font(15),fill='#35434b');d.rectangle((1010,57,1030,77),fill='#aeb6c1');d.text((1042,58),'historische / beobachtete Form',font=font(15),fill='#35434b')
 else:
  d.rectangle((1050,28,1070,48),fill='#ab8962');d.text((1082,27),'Holz · Kandidat',font=font(15),fill='#35434b');d.rectangle((1050,59,1070,79),fill='#656b69');d.text((1082,58),'Metall · Kandidat',font=font(15),fill='#35434b')
 return page

def canonical():
 cameras=json.loads((ROOT/'data/canonical-cameras.json').read_text());directory=OUT/'canonical';directory.mkdir(exist_ok=True);manifest=[]
 for cam in cameras['views']:
  for mode in ['truth','brute']:
   name=mode+('-exploded' if cam.get('exploded') else '');im=render(name,cam,mode=='truth',cam.get('angle',0),cam.get('operation',False))
   note='Referenzdarstellung; Einbaupose und alle aktuellen Maße offen. Fehlende Geometrie bleibt leer.' if mode=='truth' else 'Synthetische Ergänzung; Nägel, gerichtete Überlappung, Schaufelanstellung und Betrieb sind Kandidaten.'
   if mode=='truth' and cam['id'] in ['08','09','13','14','16']:note='Kontakt, Tragwerksmaße und Wasserfunktion nicht als Truth freigegeben; keine erfundene Ergänzung.'
   im=plate(im,f"{cam['id']}  {cam['title']}",f"{'TRUTH MODEL' if mode=='truth' else 'BRUTE-FORCE MODEL'} · Kamera identisch im Vergleichspaar",mode=='truth',note)
   path=directory/f"{cam['id']}-{mode}.png";im.save(path);manifest.append({'id':cam['id'],'model':mode,'path':str(path.relative_to(ROOT)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'camera':cam})
   print(path.name,flush=True)
 (OUT/'canonical-manifest.json').write_text(json.dumps({'iteration':'ITER-001','renderer':ctx.info['GL_RENDERER'],'source':'actual exported mesh triangles','views':manifest},indent=2))
 thumbs=Image.new('RGB',(1440,16*285),'#faf9f5');d=ImageDraw.Draw(thumbs)
 for i,cam in enumerate(cameras['views']):
  for j,mode in enumerate(['truth','brute']):
   im=Image.open(directory/f"{cam['id']}-{mode}.png");im.thumbnail((710,282));thumbs.paste(im,(j*720,i*285))
 thumbs.save(OUT/'canonical-contact-sheet.jpg',quality=90)

def technical():
 out=OUT/'technical';out.mkdir(exist_ok=True)
 ref={'eye':[-2,-3,1.2],'target':[0,0,0],'height':.85,'filter':'reference'}
 shots=[('01-kumpf-section','Kumpf · Längsschnitt durch Dauben und Bodennut','reference',{**ref,'eye':[0,-3,0],'clip':[0,-1,0,0]},'12 Dauben · Nutboden · 3 flache Metallbänder | Nutabmessungen nur Kandidat'),
 ('02-four-holes','Zwei Befestigungsdauben · vier reale Bohrungen','drilled',{**ref,'eye':[-3,0,0]},'HA1/HA2 auf Daube 1 · HB1/HB2 auf gegenüberliegender Daube 7 (Zuordnung Kandidat)'),
 ('03-nails-A','Kumpfnägel · A: gleiche Lochhöhen','nails-A',{**ref,'height':1.0},'Lang: HA1–HB1 · Kurz: HA2–HB2 | Einsteckrichtung und Krümmung unbestätigt'),
 ('04-overlap','Drei Kümpfe · gerichtete Überlappung','brute',{'eye':[-5,-4,3],'target':[-.75,-.5,2.02],'height':1.7,'filter':'cluster'},'Richtung A: K[i] Boden über Nachbarmündung | Umfangsfolge ist ein Kandidat'),
 ('05-exploded','Dauben / Nutboden / Reifen / Nägel · zerlegt','reference-exploded',{**ref,'height':1.2},'Explosionsabstände nur für die Darstellung; keine reale Ausbaufolge behauptet'),
 ('06-paddle','Schaufel · X + radial; Normale tangential','brute',{'eye':[-4,-4,4],'target':[-.15,-.3,2.12],'height':1.5,'filter':'local'},'X: Welle · R: radial · T: tangential | n·X=0 für V2 UND V3; Pitch unterscheidet sie'),
 ('07-local','Kumpf / Schaufel / Krümmling · Anschlusskandidat','brute',{'eye':[-4,-1,3],'target':[-.65,-.25,2.08],'height':1.4,'filter':'local'},'Nagelpfade geometrisch gegen Krümmlinge geprüft; Bohrung im Krümmling noch unbekannt'),
 ('08-operating-path','Betriebsbahn · Wasseraufnahme bis Trog / Rinne','brute',{'eye':[-8,-3,3],'target':[-.7,0,0],'height':6.2,'filter':'all'},'Füllung aus Mundlage und Schwerkraft; Verluste außerhalb des Trogs bleiben sichtbar')]
 for stem,title,name,cam,note in shots:
  im=plate(render(name,cam,operation=stem.startswith('08')),title,'GEOMETRIEABGELEITETE TECHNISCHE ANSICHT · ITER-001',False,note);im.save(out/f'{stem}.png')
 # Section contours/hatching are computed by actual mesh-plane intersections.
 pr=json.loads((TMP/'reference-section.json').read_text());img=Image.new('RGB',(1440,860),'#faf9f5');draw=ImageDraw.Draw(img)
 def xy(p):return (720+p[0]*1120,430-p[1]*1120)
 for seg in pr['hatch']:draw.line([xy(v) for v in seg],fill='#a28a66',width=1)
 for seg in pr['cuts']:draw.line([xy(v) for v in seg],fill='#31434b',width=3)
 for text,pt in [('Boden in Nut',[.15,-.255]),('Mündung',[.115,.3]),('Bohrung HA1 / HB1',[.135,.11]),('Bohrung HA2 / HB2',[.15,-.15])]:
  a=xy(pt);draw.line([a,(1030,a[1])],fill='#65878a',width=1);draw.text((1040,a[1]-11),text,font=font(16),fill='#35434b')
 plate(img,'Kumpf · Längsschnitt durch Dauben und Bodennut','Exakte Mesh-Ebenen-Schnittlinien und materialbegrenzte Schraffur',False,'12 Dauben · Nutboden · 3 Bänder | Keine Maßfreigabe: Bohrungs- und Nutmaße sind Kandidaten').save(out/'01-kumpf-section.png')
 # Additional construction detail is rendered from the same grooved meshes.
 grooveCam={'eye':[.14,-3,-.255],'target':[.14,0,-.255],'height':.13,'filter':'reference','clip':[0,-1,0,0]}
 plate(render('reference',grooveCam),'Bodennut · vergrößerter Schnitt','Geometrie-Makro · keine unabhängige Detailzeichnung',False,'Bodenrand liegt in der Nut. 8 mm Tiefe / 14 mm Breite sind ausdrücklich synthetische Werte.').save(out/'groove-detail.png')
 ex={'eye':[-4,-4,4],'target':[-.95,-.25,2.08],'height':2.0,'filter':'local'}
 plate(render('brute-exploded',ex),'Kumpf → Krümmling · Explosionsdetail','Gemeinsame Modellgeometrie · Nägel / Dauben / Ring',False,'Explosionsabstand dient nur der Sichtbarkeit. Nagelbohrung im Krümmling bleibt verdeckter Kandidat.').save(out/'kumpf-kruemmling-exploded.png')
 # Real front/side/top dimensions remain photo estimates; views use one shape.
 for n,eye in [('front',[-3,0,0]),('side',[0,-3,0]),('mouth',[0,0,3]),('base',[0,0,-3])]:
  plate(render('reference',{**ref,'eye':eye}),f'Referenz-Kumpf · {n}','Orthografisch aus demselben Mesh',False,'Fotoablesung: L ≈ 600 ± 20 mm · Boden-Ø ≈ 300 ± 20 mm · Mund-Ø ≈ 225 ± 15 mm').save(out/f'reference-{n}.png')
 ims=[Image.open(out/f'{x[0]}.png') for x in shots];sheet=Image.new('RGB',(1440,4*520),'white')
 for i,im in enumerate(ims):im.thumbnail((720,520));sheet.paste(im,((i%2)*720,(i//2)*520))
 sheet.save(OUT/'technical-contact-sheet.jpg',quality=92)

def comparisons():
 out=OUT/'comparisons';out.mkdir(exist_ok=True)
 local={'eye':[-4,-4,4],'target':[-.65,-.2,2.1],'height':1.7,'filter':'local'}
 specs=[('01-kumpf-v2-v3','V2 Fassprofil / V3 konischer Referenzkörper','old','brute',local),('02-nail-hypothesis','V2 freie Stifte / V3 vier Lochpositionen und Krümmlingbezug','old','brute',local),('03-paddle-v2-v3','V2 X+T / V3 X+R · beide senkrecht zur Radebene','old','brute',local),('04-isolated-overlap','Isoliertes Gefäß / drei benachbarte Kümpfe','brute','brute',{**local,'target':[-.7,-.5,2],'height':1.9,'filter':'cluster'}),('05-operating-cycle','V2 feste Winkel / V3 aus Pose berechnete Füllung','old','brute',{'eye':[-8,-3,3],'target':[-.7,0,0],'height':6.4,'filter':'all'})]
 for stem,title,left,right,cam in specs:
  page=Image.new('RGB',(1440,680),'#faf9f5');d=ImageDraw.Draw(page);d.text((24,16),title,font=font(24),fill='#24333b')
  for j,name in enumerate([left,right]):
   cc={**cam};
   if stem.startswith('04') and j==0:cc['filter']='local'
   im=render(name,cc,operation=stem.startswith('05'));im.resize((720,430)).save(TMP/f'{stem}-{j}.png');page.paste(im.resize((720,430)),(j*720,92))
   d.text((j*720+24,61),'V2 / vorher' if j==0 else 'ITER-001 / Kandidat',font=font(18),fill='#52646b')
  d.text((24,550),'Gleiche Kamera und Projektion. Synthetische Geometrie bleibt getrennt von Truth.',font=font(17),fill='#52646b');d.text((24,590),'ITER-001 · Keine automatische Bestätigung durch visuelle Plausibilität',font=font(17),fill='#52646b')
  page.save(out/f'{stem}.png')
 # All three explicit hole-pairing candidates, same reference coordinate system.
 page=Image.new('RGB',(1440,700),'#faf9f5');d=ImageDraw.Draw(page);d.text((25,15),'Nagelpfade A / B / C · geometrische Alternativen',font=font(25),fill='#24333b')
 for j,key in enumerate(['A','B','C']):
  im=render('nails-'+key,{'eye':[-2,-3,1],'target':[0,0,0],'height':1.1,'filter':'reference'});im.thumbnail((480,530));page.paste(im,(j*480,90));d.text((j*480+25,60),key+': '+['gleichhohe Paare','umgekehrter Einsteckweg','Kreuzpaarung'][j],font=font(17),fill='#24333b')
 d.text((25,610),'A führend; B braucht anderen Zugang; C verletzt achsparallele Bohrung und bleibt nachrangig.',font=font(18),fill='#52646b');page.save(out/'06-nail-candidates-ABC.png')

def projected(point,cam):
 v=matrix(cam)@np.array([*point,1.]);return ((v[0]+1)*W/2,(1-v[1])*H/2)

def animation():
 cycle=json.loads((TMP/'cycle.json').read_text());cam={'eye':[-7,-8,4],'target':[-.7,0,-.2],'height':7.3,'filter':'all'}
 frames=[];out=OUT/'operation';out.mkdir(exist_ok=True)
 for degree in range(0,360,5):
  im=render('brute',cam,angle=math.radians(degree),operation=True);d=ImageDraw.Draw(im)
  for slot in range(24):
   state=cycle[round(((degree+slot*15)%360)/2)%180]
   if state['discharging']:
    pts=[projected(p,cam) for p in state['stream']];d.line(pts,fill='#2987b1',width=3)
  state=cycle[round(degree/2)%180];x,y=projected(state['center'],cam);d.ellipse((x-8,y-8,x+8,y+8),fill='#efffff',outline='#267f9d',width=3);d.text((x+12,y-12),'K01',font=font(16),fill='#206682')
  if any(cycle[round(((degree+i*15)%360)/2)%180]['inTrough'] for i in range(24)):
   cfg=json.loads((ROOT/'data/calibration-v3.json').read_text())['production'];points=[[cfg['troughX'],0,cfg['troughZ']+.04],[cfg['troughX'],1.25,cfg['troughZ']-.01],[-3.8,1.25,cfg['troughZ']-.17]];d.line([projected(p,cam) for p in points],fill='#2987b1',width=4)
  frame=plate(im,'Betrieb · vollständiger Kumpfzyklus',f"K01 · {degree:03d}° · {state['state']} · Füllanteil {state['fill']:.0%}",False,'Ballistischer Ausfluss: 1,8 m/s Kandidat + Raddrehung + Schwerkraft. Kein CFD / keine Fördermengenprognose.')
  if degree in [175,260,325,340]:frame.save(out/f"phase-{degree}.png")
  frame=frame.resize((1008,728));frames.append(frame)
  if degree%60==0:print('cycle',degree,flush=True)
 frames[0].save(out/'full-cycle.gif',save_all=True,append_images=frames[1:],duration=420,loop=0,optimize=False)
 sheet=Image.new('RGB',(1440,1040),'white')
 for i,degree in enumerate([175,260,325,340]):
  im=Image.open(out/f'phase-{degree}.png');im.thumbnail((720,520));sheet.paste(im,((i%2)*720,(i//2)*520))
 sheet.save(out/'pickup-lift-discharge-channel.jpg',quality=92)

if __name__=='__main__':
 import sys
 jobs=sys.argv[1:] or ['canonical','technical','comparisons']
 for job in jobs:globals()[job]()

from pathlib import Path
import json,hashlib
from PIL import Image,ImageOps,ImageDraw,ImageFont
exec((Path(__file__).parent/'safe-image-write.py').read_text())
R=Path(__file__).resolve().parents[1];O=R/'output/calibration/ITER-001/sources';O.mkdir(parents=True,exist_ok=True)
font=lambda n:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',n)
records=[('1000046420.jpg','Nut im teilweise zerlegten Kumpf',[(250,164,740,194,'Nut: Existenz sichtbar; genaue Tiefe offen'),(561,326,645,771,'zwei Lochlagen in einer Daube')]),('1000046421.jpg','Bodenansicht mit Maßstab',[(128,830,849,391,'äußere Ablesung ungefähr 30 cm ± 2 cm')]),('1000046422.jpg','Mündung / Daubenquerschnitt',[(487,217,569,1000,'Mündungs-Ø ungefähr 22–24 cm')]),('1000046423.jpg','Längsprofil / drei Bänder',[(46,370,1210,352,'Länge ungefähr 60 cm ± 2 cm'),(415,325,945,325,'Lochlagen ungefähr 19 / 45 cm; Bezug prüfen')])]
manifest=[]
for fn,title,lines in records:
 src=R/'evidence/raw'/fn;im=ImageOps.exif_transpose(Image.open(src)).convert('RGB');d=ImageDraw.Draw(im)
 for x1,y1,x2,y2,label in lines:
  d.line((x1,y1,x2,y2),fill='#00b3d1',width=6);d.ellipse((x1-8,y1-8,x1+8,y1+8),fill='#00b3d1');d.ellipse((x2-8,y2-8,x2+8,y2+8),fill='#00b3d1')
 im.thumbnail((900,1060));page=Image.new('RGB',(1440,1200),'#faf9f5');page.paste(im,(25,105));dd=ImageDraw.Draw(page);dd.text((25,22),fn+' · '+title,font=font(25),fill='#24333b');y=160
 for *_,label in lines:
  # hand wrap text for readable annotation column
  words=label.split();line=''
  for word in words:
   if len(line+' '+word)>34:dd.text((940,y),line,font=font(19),fill='#35434b');y+=31;line=word
   else:line=(line+' '+word).strip()
  dd.text((940,y),line,font=font(19),fill='#35434b');y+=74
 dd.text((940,y),'Fotoablesung, kein Ist-Aufmaß.',font=font(18),fill='#88693f');dd.text((25,1162),'ITER-001 · Original unverändert archiviert · Markierungen bezeichnen Beobachtungsbereiche, keine registrierte Projektion.',font=font(17),fill='#52646b');page.save(O/(src.stem+'-annotated.png'))
 manifest.append({'source':str(src.relative_to(R)),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'annotations':lines,'status':'visual-readout-unrectified-reference-only'})
# Installed-photo comparison. Explicitly no false metric overlay on an unregistered view.
photo=ImageOps.exif_transpose(Image.open(R/'evidence/raw/IMG_6854.jpeg')).convert('RGB');d=ImageDraw.Draw(photo);d.line((640,825,655,1150),fill='#00b3d1',width=8);d.line((305,532,425,700),fill='#00b3d1',width=8);photo.thumbnail((650,870));page=Image.new('RGB',(1440,1040),'#faf9f5');page.paste(photo,(15,90));mod=Image.open(R/'output/calibration/ITER-001/canonical/12-brute.png');mod.thumbnail((760,780));page.paste(mod,(675,100));d=ImageDraw.Draw(page);d.text((25,20),'Einbaukontext · PHOTO-6854 / gerichteter Kandidat A',font=font(26),fill='#24333b');d.text((25,970),'Türkis: Nachbarschaft / Nagelköpfe. Gegenüberstellung ohne Kamera- oder Scanregistrierung.',font=font(19),fill='#35434b');d.text((25,1005),'Existenz und sichtbare Formen stützen den Kandidaten; Richtung, Pose und verdeckte Kontakte bleiben offen.',font=font(16),fill='#52646b');page.save(O/'installed-overlap-comparison.png')
# Scan side-by-side: export coordinates, not a mechanically aligned overlay.
scan=Image.open(R/'evidence/derived/ply-orthographic.png');scan.thumbnail((1390,600));page=Image.new('RGB',(1440,900),'#faf9f5');page.paste(scan,(25,100));d=ImageDraw.Draw(page);d.text((25,20),'Radscan · 75.619 Punkte · unregistrierte Exportachsen',font=font(26),fill='#24333b');d.text((25,725),'PLY / GLB enthalten dieselbe unvollständige Aufnahme. Ein eigenständiger Schaufel-/Nagelscan ist nicht vorhanden.',font=font(20),fill='#35434b');d.text((25,770),'Keine zuverlässige Brettsegmentierung oder Ebenenwinkelmessung: sichtbare Schaufelkandidaten bleiben mehrdeutig.',font=font(18),fill='#52646b');d.text((25,820),'Keine metrische Übertragung in Truth. Siehe SCAN-FINDINGS.md und unveränderte scan-transforms.json.',font=font(18),fill='#52646b');page.save(O/'scan-review.png')
(R/'state/reconstruction-loop/ITER-001/source-photo-readouts.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
# Coordinate arrows are projected on the actual paddle render, not a replacement schematic.
import numpy as np,math
cam={'eye':[-4,-4,4],'target':[-.15,-.3,2.12],'height':1.5}
def proj(pt):
 eye=np.array(cam['eye'],float);target=np.array(cam['target'],float);forward=(target-eye)/np.linalg.norm(target-eye);right=np.cross(forward,[0,0,1]);right/=np.linalg.norm(right);up=np.cross(right,forward);delta=np.array(pt)-target;scale=860/cam['height'];return (720+np.dot(delta,right)*scale,110+430-np.dot(delta,up)*scale)
img=Image.open(R/'output/calibration/ITER-001/technical/06-paddle.png').convert('RGB');d=ImageDraw.Draw(img);phase=json.loads((R/'data/calibration-v3.json').read_text())['production']['paddlePhaseSlots']*math.pi/12;origin=np.array([0,-math.sin(phase)*2.23,math.cos(phase)*2.23]);vectors=[('X · Welle',np.array([1,0,0]),'#ad6652'),('R · Brettfläche',np.array([0,-math.sin(phase),math.cos(phase)]),'#328b95'),('T · Normale',np.array([0,-math.cos(phase),-math.sin(phase)]),'#6579b1')]
for label,v,col in vectors:
 a=proj(origin);b=proj(origin+.4*v);d.line([a,b],fill=col,width=5);d.ellipse((b[0]-6,b[1]-6,b[0]+6,b[1]+6),fill=col);d.text((b[0]+8,b[1]-22),label,font=font(17),fill=col)
img.save(R/'output/calibration/ITER-001/technical/06-paddle.png')
# Rebuild technical contact sheet after vector annotations.
files=['01-kumpf-section','02-four-holes','03-nails-A','04-overlap','05-exploded','06-paddle','07-local','08-operating-path'];sheet=Image.new('RGB',(1440,2080),'white')
for i,n in enumerate(files):
 im=Image.open(R/f'output/calibration/ITER-001/technical/{n}.png');im.thumbnail((720,520));sheet.paste(im,((i%2)*720,(i//2)*520))
sheet.save(R/'output/calibration/ITER-001/technical-contact-sheet.jpg',quality=92)

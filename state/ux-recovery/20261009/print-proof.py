import fitz,pathlib,hashlib,json,runpy
runpy.run_path("scripts/safe-image-write.py")
from PIL import Image,ImageOps,ImageDraw
root=pathlib.Path('state/ux-recovery/20261009/evidence/print-live');root.mkdir(parents=True,exist_ok=True);result=[]
for label,name in [('a3','KS-Werkstatt-Aufnahmeplan-A3.pdf'),('a4','KS-Kurzplan-A4.pdf')]:
 p=root/name;d=fitz.open(p);pages=[]
 for i,page in enumerate(d):
  pix=page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False);im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.save(root/f'{label}-{i+1:02d}-color.png');ImageOps.grayscale(im).save(root/f'{label}-{i+1:02d}-gray.png');pages.append({'page':i+1,'width_pt':page.rect.width,'height_pt':page.rect.height,'text_chars':len(page.get_text()),'synthetic_label':'synthet' in page.get_text().lower() or 'kandidat' in page.get_text().lower()})
 for mode in ['color','gray']:
  thumbs=[]
  for i in range(len(d)):
   im=Image.open(root/f'{label}-{i+1:02d}-{mode}.png').convert('RGB');im.thumbnail((580,425));tile=Image.new('RGB',(600,455),'#dddddd');tile.paste(im,((600-im.width)//2,25));ImageDraw.Draw(tile).text((10,5),f'{label.upper()} {i+1} {mode}',fill='black');thumbs.append(tile)
  for start in range(0,len(thumbs),4):
   sheet=Image.new('RGB',(1200,910),'white')
   for j,tile in enumerate(thumbs[start:start+4]):sheet.paste(tile,((j%2)*600,(j//2)*455))
   sheet.save(root/f'{label}-{mode}-overview-{start//4+1}.jpg',quality=90)
 result.append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'pages':pages})
(root/'pdf-metadata.json').write_text(json.dumps(result,indent=2))
print([(x['path'],len(x['pages'])) for x in result])

from pathlib import Path
import fitz,json,hashlib
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parent.parent
pdf=root/'output/pdf/KS-Werkstatt-Aufnahmeplan-A3.pdf';doc=fitz.open(pdf);out=root/'state/reconstruction/pdf-review';out.mkdir(parents=True,exist_ok=True)
contact=Image.new('RGB',(1800,1840),'#e8e8e4');rows=[]
for i,page in enumerate(doc):
 assert abs(page.rect.width-1190.55)<2 and abs(page.rect.height-841.89)<2
 pix=page.get_pixmap(matrix=fitz.Matrix(1.2,1.2));pix.save(out/f'{i+1:02}.png')
 im=Image.open(out/f'{i+1:02}.png');im.thumbnail((580,415));x=i%3*600+10;y=i//3*460+10;contact.paste(im,(x,y));ImageDraw.Draw(contact).text((x+5,y+423),f'{i+1:02} / {len(doc)}',fill='#222222')
 text=page.get_text();assert 'REKONSTRUIERT' in text or 'Aufnahmebereiche' in text
 rows.append({'page':i+1,'size_points':[round(page.rect.width,2),round(page.rect.height,2)],'render':f'{i+1:02}.png','text_characters':len(text)})
contact.save(out/'contact-sheet.jpg',quality=91)
(out/'render-manifest.json').write_text(json.dumps({'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':rows,'visual_review':'requires human or agent image inspection; not inferred from rendering'},indent=2)+'\n')
print(f'Rendered {len(doc)} A3 pages and contact sheet.')

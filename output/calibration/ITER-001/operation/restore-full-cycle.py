from pathlib import Path
import hashlib,json,os
p=Path(__file__).resolve().parent
m=json.loads((p/'full-cycle.parts.json').read_text())
chunks=[]
for part in m['parts']:
    b=(p/part['name']).read_bytes()
    assert len(b)==part['bytes'] and hashlib.sha256(b).hexdigest()==part['sha256']
    chunks.append(b)
b=b''.join(chunks)
assert len(b)==m['bytes'] and hashlib.sha256(b).hexdigest()==m['sha256']
target=p/m['file']
if target.exists():
    assert target.read_bytes()==b, 'Existing GIF differs; preserved without overwrite'
else:
    temp=p/'full-cycle.restoring.tmp'
    with temp.open('xb') as f:
        f.write(b);f.flush();os.fsync(f.fileno())
    temp.replace(target)
print('Restored exact original GIF:', target, m['sha256'])

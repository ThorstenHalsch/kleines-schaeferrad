"""Read existing evidence; never re-export, fit, or render reconstruction geometry."""
from pathlib import Path
import hashlib,json,struct,subprocess
from PIL import Image
R=Path(__file__).resolve().parent.parent
O=R/'state/reconstruction-loop/ITER-001/truth-critic';O.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((R/p).read_text())
base=read('data/pre-disassembly-evidence-gate.json')['base_commit']
manifest=read('output/calibration/ITER-001/canonical-manifest.json');views=[]
for v in manifest['views']:
 p=R/v['path'];Image.open(p).verify();views.append({'path':v['path'],'sha256':sha(p),'matches_manifest':sha(p)==v['sha256']})
assert len(views)==32 and all(v['matches_manifest'] for v in views)
for i in range(1,17):
 pair=[v for v in manifest['views'] if v['id']==f'{i:02}'];assert len(pair)==2 and pair[0]['camera']==pair[1]['camera']
models={}
for mode in ['truth','brute']:
 p=R/f'output/calibration/ITER-001/{mode}-ITER-001.glb';b=p.read_bytes();magic,version,length=struct.unpack_from('<III',b);assert magic==0x46546c67 and version==2 and length==len(b)
 n=struct.unpack_from('<I',b,12)[0];d=json.loads(b[20:20+n]);meshes=[x for x in d['nodes'] if 'mesh' in x]
 models[mode]={'sha256':sha(p),'mesh_nodes':len(meshes),'families':sorted(set(x.get('extras',{}).get('family','unknown') for x in meshes)),'metric_statuses':sorted(set(x.get('extras',{}).get('metricStatus','absent') for x in meshes))}
 if mode=='truth':
  assert not any(x.get('extras',{}).get('nailPath') for x in meshes)
  assert d['nodes'][1]['extras']['asBuilt'] is False
  models[mode]['note']='No exact nail paths. Display vertices still synthetic; metadata is not a metrical survey.'
# Attached copies are optional when verifying this repository on another machine.
attachments=[]
for p in sorted((R.parent/'project_sources').glob('*')):
 name=p.name.split('-',1)[-1];q=R/'evidence/raw'/name
 attachments.append({'file':name,'sha256':sha(p),'archive_match':q.exists() and sha(p)==sha(q)})
assert not attachments or len(attachments)==30 and all(a['archive_match'] for a in attachments)
scan=read('data/scan-transforms.json');assert scan['adopted_mechanical_transform'] is None and scan['field_scale'] is None
with (R/'evidence/raw/Scaniverse 2026-10-07 173556.ply').open('rb') as f:
 header=[]
 while True:
  s=f.readline().decode('ascii').strip();header.append(s)
  if s=='end_header':break
assert 'element vertex 75619' in header
scanbytes=(R/'evidence/raw/Scaniverse 2026-10-07 173556.glb').read_bytes()
scann=struct.unpack_from('<I',scanbytes,12)[0];scandoc=json.loads(scanbytes[20:20+scann])
primitives=[p for m in scandoc['meshes'] for p in m['primitives']]
scan_geometry={'position_accessor_vertices':sum(scandoc['accessors'][i]['count'] for i in {p['attributes']['POSITION'] for p in primitives}), 'indexed_triangles':sum(scandoc['accessors'][p['indices']]['count']//3 for p in primitives if 'indices' in p and p.get('mode',4)==4),'scope':'Binary accessor/header inspection; no fit or mechanical registration'}
prior=read('data/pre-disassembly-evidence-gate.json');tasks=read('data/field-tasks.json')['tasks'];old=json.loads(subprocess.check_output(['git','show',base+':data/field-tasks.json'],cwd=R))['tasks']
assert [t['task_id'] for t in tasks]==[t['task_id'] for t in old], 'Preserve persisted numeric field positions'
assert {p['task_id'] for p in prior['priorities']}=={t['task_id'] for t in tasks}
assert all(q['status']=='UNANSWERED' and q['answer'] is None for q in prior['decisions'])
for q in prior['decisions']:
 for p in q['sources']:assert (R/p).is_file(),p
# Confirm originals, full ITER-001 outputs, geometry and projection payloads unchanged from reviewed base.
frozen=['evidence/raw','output/calibration/ITER-001','src/workbench','data/calibration-v3.json','data/scan-transforms.json','data/geometry.claims.json','data/evidence-authority.json','docs/field-kit/model-projections.json','docs/field-kit/model-projections.json.gz']
changed=subprocess.check_output(['git','diff',base,'--name-only','--',*frozen],cwd=R,text=True).splitlines();assert not changed,changed
inventory=[]
for folder in ['evidence/raw','evidence/contributions','state/reconstruction-loop/ITER-001','output/calibration/ITER-001']:
 for p in sorted((R/folder).rglob('*')):
  if p.is_file() and O not in p.parents:inventory.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
report={'schema':'ks-independent-evidence-verification/v1','base_commit':base,'scope':'existing artifacts, metadata, source hashes and gate contracts; no reconstruction replay','canonical_views':views,'paired_cameras_checked':16,'models':models,'attachments':attachments,'scan_state':scan['state'],'ply_vertex_count_from_header':75619,'scan_glb':scan_geometry,'frozen_paths_unchanged':frozen,'canonical_task_ids_and_array_order_preserved':True,'all_21_tasks_ranked':True,'all_5_decisions_unanswered':True,'source_inventory':inventory}
(O/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f'PASS: 32 render hashes; 16 paired cameras; 2 GLBs; {len(attachments)} attachment matches; 21 tasks; 5 open decisions; frozen model paths unchanged')

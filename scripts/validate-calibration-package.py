"""Check exported package integrity, stable paired cameras, provenance and decoded frames."""
import hashlib,json,struct
from pathlib import Path
from PIL import Image,ImageSequence
root=Path(__file__).resolve().parents[1]
out=root/'output/calibration/ITER-001'
state=root/'state/reconstruction-loop/ITER-001'
def read(p): return json.loads(p.read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
cameras=read(root/'data/canonical-cameras.json')
manifest=read(out/'canonical-manifest.json')
assert len(manifest['views'])==32
for camera in cameras['views']:
    pair=[v for v in manifest['views'] if v['id']==camera['id']]
    assert len(pair)==2 and {v['model'] for v in pair}=={'truth','brute'}
    for v in pair:
        assert v['camera']==camera
        p=root/v['path']
        assert sha(p)==v['sha256'],str(p)
        with Image.open(p) as im: assert list(im.size)==cameras['imageSize']
images=frames=0
for p in sorted(out.rglob('*')):
    if p.suffix.lower() in ('.png','.jpg','.gif'):
        with Image.open(p) as im:
            for frame in ImageSequence.Iterator(im): frame.load();frames+=1
        images+=1
for mode in ('truth','brute'):
    p=out/f'{mode}-ITER-001.glb';b=p.read_bytes()
    assert struct.unpack_from('<4sII',b)==(b'glTF',2,len(b))
    n,kind=struct.unpack_from('<II',b,12);assert kind==0x4e4f534a
    doc=json.loads(b[20:20+n]);assert doc['meshes']
    index=read(out/f'{mode}-index.json')
    for key,path in [('calibration','src/workbench/calibration.mjs'),('geometry','src/workbench/geometry.mjs'),('parameters','data/calibration-v3.json')]:
        assert index['geometryHashes'][key]==sha(root/path)
    assert index['acceptedInstalledMetrics'] is None
truth=read(out/'truth-index.json');assert truth['truthConstraints']['exactNailPaths'] is None
assert truth['truthConstraints']['directedOverlap'] is None
intake=read(state/'attachment-intake.json');assert intake['count']==30
for f in intake['files']: assert f['archiveMatches'] and sha(root/f['archive'])==f['sha256']
for n in range(1,9): assert len(list((out/'technical').glob(f'{n:02}-*.png')))==1
assert len(list((out/'comparisons').glob('*.png')))>=5
with Image.open(out/'operation/full-cycle.gif') as im: assert im.n_frames==72
for name in ['ITERATION-REPORT.md','CONSTRAINT-DELTA.json','MODEL-DELTA.json','SCORECARD.json','CRITIQUE-READY.md','SATURDAY-QUESTIONS.md','ADVERSARIAL-AUDIT.md']:
    assert (state/name).stat().st_size>0
contacts=read(state/'contact-audit.json');assert all(contacts['stats'][k]==0 for k in ['vesselNeighbor','vesselPaddle','vesselRim'])
assert all(s['collisionSamples']==0 for s in contacts['sweep'])
assert read(state/'stationary-audit.json')['hits']=={}
result={'iteration':'ITER-001','status':'PASS','canonicalViews':32,'pairedCameras':16,'decodedImages':images,'decodedFrames':frames,'animationFrames':72,'separateModelExports':2,'verifiedSourceAttachments':30,'mandatoryTechnicalSubjects':8,'limitations':'Integrity and sampled geometry checks; no new measured dimensions, continuous collision proof or browser playback verification.'}
(state/'PACKAGE-VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

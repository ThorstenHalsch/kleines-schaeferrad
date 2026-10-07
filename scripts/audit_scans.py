import json, struct, hashlib
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parents[1]
raw=root/'evidence/raw'
out=root/'evidence/derived';out.mkdir(parents=True,exist_ok=True)
ply=next(raw.glob('*.ply')).read_bytes()
offset=ply.index(b'end_header\n')+len(b'end_header\n')
header=ply[:offset].decode();n=int(header.split('element vertex ')[1].splitlines()[0])
dtype=np.dtype([('xyz','<f4',(3,)),('rgb','u1',(3,))])
p=np.frombuffer(ply, dtype=dtype,offset=offset,count=n)
xyz=p['xyz'];rgb=p['rgb']/255
glb=next(raw.glob('*.glb')).read_bytes()
assert struct.unpack_from('<III',glb)==(0x46546c67,2,len(glb))
chunks=[];o=12
while o<len(glb):
 size,kind=struct.unpack_from('<II',glb,o);chunks.append((kind,glb[o+8:o+8+size]));o+=8+size
j=json.loads(chunks[0][1]);buf=chunks[1][1]
def access(i):
 a=j['accessors'][i];v=j['bufferViews'][a['bufferView']];dt={5126:'<f4',5125:'<u4'}[a['componentType']];width={'VEC3':3,'VEC2':2,'SCALAR':1}[a['type']]
 return np.frombuffer(buf,dtype=dt,offset=v.get('byteOffset',0)+a.get('byteOffset',0),count=a['count']*width).reshape(-1,width)
verts=access(0);uv=access(1);faces=access(2).reshape(-1,3)
area=np.linalg.norm(np.cross(verts[faces[:,1]]-verts[faces[:,0]],verts[faces[:,2]]-verts[faces[:,0]]),axis=1)/2
edges=np.sort(np.concatenate([faces[:,[0,1]],faces[:,[1,2]],faces[:,[2,0]]]),axis=1);ue,c=np.unique(edges,axis=0,return_counts=True)
def bounds(a):return {'min':a.min(0).tolist(),'max':a.max(0).tolist(),'extent':np.ptp(a,axis=0).tolist(),'finite':bool(np.isfinite(a).all())}
report={'schema':'ks-scan-audit/v1','ply':{'vertices':n,'header':header,'payload_bytes':len(ply)-offset,'expected_payload_bytes':n*dtype.itemsize,'bounds':bounds(xyz),'unique_positions':len(np.unique(xyz,axis=0))},'glb':{'vertices':len(verts),'faces':len(faces),'bounds':bounds(verts),'index_range':[int(faces.min()),int(faces.max())],'boundary_edges':int((c==1).sum()),'nonmanifold_edges':int((c>2).sum()),'zero_area_faces':int((area==0).sum()),'nodes':j['nodes'],'accessors':j['accessors'],'generator':j['asset']['generator'],'texture_bytes':j['bufferViews'][0]['byteLength']},'registration':{'measured_scale':None,'mechanical_transform':None,'ply_to_glb_transform':None,'units':'export coordinate units; expected metric convention is not field calibration'}}
(out/'scan-audit.json').write_text(json.dumps(report,indent=2)+'\n')
np.savez('/tmp/ks_scan_arrays.npz',xyz=xyz,rgb=rgb,verts=verts,uv=uv,faces=faces)
for label,pts,colors in [('ply',xyz,rgb),('glb',verts,None)]:
 fig,axs=plt.subplots(1,3,figsize=(18,7))
 for ax,(a,b) in zip(axs,[(0,1),(0,2),(2,1)]):
  ax.scatter(pts[:,a],pts[:,b],c=colors,s=.4);ax.set_aspect('equal');ax.set_xlabel('XYZ'[a]);ax.set_ylabel('XYZ'[b]);ax.set_title(label+' export coordinates');ax.grid(alpha=.2)
 fig.tight_layout();fig.savefig(out/(label+'-orthographic.png'),dpi=150);plt.close(fig)
 # GLB texture provides per-vertex appearance for forensic views, no alteration of geometry.
 if label=='glb':
  from PIL import Image
  import io
  v=j['bufferViews'][0];im=np.asarray(Image.open(io.BytesIO(buf[v['byteOffset']:v['byteOffset']+v['byteLength']])).convert('RGB'))
  colors=im[np.clip((uv[:,1]*im.shape[0]).astype(int),0,im.shape[0]-1),np.clip((uv[:,0]*im.shape[1]).astype(int),0,im.shape[1]-1)]/255
 fig=plt.figure(figsize=(10,10));ax=fig.add_subplot(projection='3d');ax.scatter(pts[:,0],pts[:,2],pts[:,1],c=colors,s=.6);ax.set_xlabel('X');ax.set_ylabel('Z');ax.set_zlabel('Y');ax.set_box_aspect(np.ptp(pts[:,[0,2,1]],axis=0));ax.view_init(20,35);fig.savefig(out/(label+'-spatial.png'),dpi=180);plt.close(fig)
print(json.dumps(report,indent=2))

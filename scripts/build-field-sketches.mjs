import fs from 'node:fs';
import * as T from 'three';
import {makeModel,disposeModel} from '../src/workbench/geometry.mjs';
const sets=[];
for(const [id,shape,layers] of [['OPEN','unknown','staggered'],['STRAIGHT','straight','staggered'],['DOGLEG','dogleg','staggered'],['COPLANAR','straight','coplanar'],['REVERSE','straight','reverse']]){
 const model=makeModel('A',0,{armShape:shape,armLayers:layers}),cam=new T.PerspectiveCamera();cam.up.set(0,0,1);cam.position.set(2,-6,3);cam.lookAt(0,0,0);cam.updateMatrixWorld();const lines=[];
 for(const mesh of model.children.filter(m=>m.userData.family==='COMP-ARMS'||m.userData.id==='HYP-SHAFT'||m.userData.unknownZone)){const edges=new T.EdgesGeometry(mesh.geometry,30),a=edges.attributes.position;for(let i=0;i<a.count;i+=2){const pts=[];for(let j=0;j<2;j++){const v=new T.Vector3().fromBufferAttribute(a,i+j).applyMatrix4(mesh.matrixWorld).applyMatrix4(cam.matrixWorldInverse);pts.push([v.x,v.y])}lines.push({points:pts,unknown:!!mesh.userData.unknownZone})}edges.dispose()}
 sets.push({id,shape,layers,lines});disposeModel(model);
}
fs.mkdirSync('docs/field-kit',{recursive:true});fs.writeFileSync('docs/field-kit/model-projections.json',JSON.stringify({source:'src/workbench/geometry.mjs',status:'HYPOTHESIS_ONLY_NO_HIDDEN_JOINERY',views:sets}));

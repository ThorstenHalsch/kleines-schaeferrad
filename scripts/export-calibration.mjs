import {projectMeshes,hatchSection,sectionMaterial} from '../src/workbench/projection.mjs';
import fs from 'node:fs';import crypto from 'node:crypto';import * as T from 'three';
import {GLTFExporter} from 'three/addons/exporters/GLTFExporter.js';
import {makeModel,disposeModel} from '../src/workbench/geometry.mjs';
import {referenceKumpf,cfg,calibratedCycle} from '../src/workbench/calibration.mjs';
const out='output/calibration/ITER-001';fs.mkdirSync(out,{recursive:true});fs.mkdirSync('/tmp/ks-calibration',{recursive:true});
globalThis.FileReader=class{readAsArrayBuffer(b){b.arrayBuffer().then(r=>{this.result=r;this.onloadend?.()})}readAsDataURL(b){b.arrayBuffer().then(r=>{this.result=`data:${b.type};base64,${Buffer.from(r).toString('base64')}`;this.onloadend?.()})}};
const digest=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
function meshData(model,name){model.updateMatrixWorld(true);const arrays=[],meshes=[];let offset=0;
 model.traverse(m=>{if(!m.isMesh)return;let g=m.geometry.index?m.geometry.toNonIndexed():m.geometry.clone();g.applyMatrix4(m.matrixWorld);const a=g.attributes.position,n=g.attributes.normal,col=m.material.color.toArray(),buf=new Float32Array(a.count*9);for(let i=0;i<a.count;i++){buf.set([a.getX(i),a.getY(i),a.getZ(i),n.getX(i),n.getY(i),n.getZ(i),...col],i*9)}arrays.push(Buffer.from(buf.buffer));meshes.push({name:m.name,first:offset,count:a.count,...m.userData});offset+=a.count;g.dispose()});fs.writeFileSync(`/tmp/ks-calibration/${name}.bin`,Buffer.concat(arrays));fs.writeFileSync(`/tmp/ks-calibration/${name}.json`,JSON.stringify(meshes));return meshes;
}
for(const mode of ['truth','brute']){
 const model=makeModel('A',0,{modelMode:mode}),register=meshData(model,mode),root=new T.Group();root.rotation.x=-Math.PI/2;root.name=`KS ${mode} ITER-001`;root.userData={...model.userData,units:'metre display coordinates; reference-only photo estimates',transform:'mechanical Z-up to glTF Y-up by Rx(-90deg)',geometryHashes:{calibration:digest('src/workbench/calibration.mjs'),geometry:digest('src/workbench/geometry.mjs'),parameters:digest('data/calibration-v3.json')},acceptedInstalledMetrics:null};root.add(model);root.updateMatrixWorld(true);
 const glb=await new GLTFExporter().parseAsync(root,{binary:true});fs.writeFileSync(`${out}/${mode}-ITER-001.glb`,Buffer.from(glb));fs.writeFileSync(`${out}/${mode}-index.json`,JSON.stringify({schema:'ks-model-index/v3',...root.userData,components:register.map(({first,count,...m})=>m)},null,2));disposeModel(root);
 const exploded=makeModel('A',.65,{modelMode:mode,componentExplode:.4});meshData(exploded,`${mode}-exploded`);disposeModel(exploded);
}
for(const [name,opt]of Object.entries({reference:{nails:false},'reference-exploded':{explode:1},'nails-A':{mapping:'A'},'nails-B':{mapping:'B'},'nails-C':{mapping:'C'}})){const m=referenceKumpf(opt);meshData(m,name);disposeModel(m)}
const drilled=referenceKumpf({nails:false});for(const mesh of [...drilled.children]){if(!mesh.userData.drilled){drilled.remove(mesh);continue}if(mesh.userData.staveIndex===6)mesh.geometry.rotateZ(Math.PI);mesh.position.y=mesh.userData.staveIndex===6?.085:-.085}meshData(drilled,'drilled');disposeModel(drilled);
const old=makeModel('A',0,{calibration:false});meshData(old,'old');disposeModel(old);
const reverse=makeModel('A',0,{overlapDirection:-1});meshData(reverse,'overlap-B');disposeModel(reverse);
fs.writeFileSync('/tmp/ks-calibration/cycle.json',JSON.stringify(Array.from({length:180},(_,i)=>({degree:i*2,...calibratedCycle(i*Math.PI/90)}))));
console.log('Truth / Brute GLBs, provenance indexes and renderer inputs exported.');

const sect=referenceKumpf({nails:false});const section={axis:'y',value:1e-6},pr=projectMeshes(sect.children,{view:[0,-1,0],section});pr.hatch=pr.cutGroups.flatMap((c,i)=>hatchSection(c,.007,sectionMaterial(sect.children[i],pr,section)));fs.writeFileSync('/tmp/ks-calibration/reference-section.json',JSON.stringify(pr));disposeModel(sect);

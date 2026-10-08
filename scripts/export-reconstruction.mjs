import fs from 'node:fs';import crypto from 'node:crypto';import * as T from 'three';
import {GLTFExporter} from 'three/addons/exporters/GLTFExporter.js';
import {makeModel,disposeModel} from '../src/workbench/geometry.mjs';
import {MECHANICAL_FRAME} from '../src/workbench/mechanics.mjs';
// Node has Blob but no browser FileReader. No images/textures are included in this mechanical export.
globalThis.FileReader=class{readAsArrayBuffer(blob){blob.arrayBuffer().then(r=>{this.result=r;this.onloadend?.()})}readAsDataURL(blob){blob.arrayBuffer().then(r=>{this.result=`data:${blob.type};base64,${Buffer.from(r).toString('base64')}`;this.onloadend?.()})}};
const model=makeModel(),root=new T.Group();root.name='Kleines Schaefferrad - reconstruction candidate';root.rotation.x=-Math.PI/2;
root.userData={mechanicalFrame:MECHANICAL_FRAME,units:'metre candidate coordinates; no measured scale',conversion:'root Rx(-90 degrees) maps mechanical Z-up to glTF Y-up',asBuilt:false,geometrySHA256:crypto.createHash('sha256').update(fs.readFileSync('src/workbench/geometry.mjs')).digest('hex')};
const moving=new T.Group(),fixed=new T.Group();moving.name='Radkoerper';fixed.name='Radstatt und Wasserweg';root.add(moving,fixed);const families=new Map(),register=[];
const map=JSON.parse(fs.readFileSync('data/reconstruction-evidence-map.json')).components;
for(const mesh of [...model.children]){const {family,stationary,id}=mesh.userData,key=(stationary?'fixed:':'moving:')+family;if(!families.has(key)){const g=new T.Group();g.name=family;families.set(key,g);(stationary?fixed:moving).add(g)}
 const evidence=map.find(x=>x.component===family)||map.find(x=>x.component===(stationary?'COMP-RADSTATT':family.includes('KUMPF')?'COMP-KUEMPFE':family));
 mesh.userData.sourceRefs=mesh.userData.sources||evidence?.sources||[];mesh.userData.physicalInstanceId=null;families.get(key).add(mesh);register.push({id,family,stationary,status:mesh.userData.status,sources:mesh.userData.sourceRefs,physical_instance:null})}
root.updateMatrixWorld(true);const data=await new GLTFExporter().parseAsync(root,{binary:true});fs.mkdirSync('output/model',{recursive:true});fs.writeFileSync('output/model/KS-Rekonstruktion-V2.glb',Buffer.from(data));fs.writeFileSync('output/model/component-index.json',JSON.stringify({schema:'ks-model-export/v2',...root.userData,meshes:register.length,components:register},null,2)+'\n');disposeModel(root);console.log(`Exported ${register.length} candidate meshes with component hierarchy; no physical instances pre-created.`);

// Review images and SVG handoff exports for the new revision-04 scenarios.
const fs=require('node:fs');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
const {chromium}=require(require.resolve('playwright',{paths:[process.argv[2]||__dirname]}));
(async()=>{
 const payload=JSON.parse(fs.readFileSync(path.join(__dirname,'prototype.json'),'utf8'));
 const cases=[['edit-achievement-ready','06-edit-achievement'],['admin-accounts-saved','07-admin-accounts'],['admin-assignment-ready','08-teacher-assignment'],['admin-grading-preview','09-grading-policy']];
 const out=path.resolve(__dirname,'../../../prototype/exports');
 const proof=process.argv[3];
 const browser=await chromium.launch({headless:true,channel:'chrome'});
 try{
  const page=await browser.newPage({viewport:{width:1500,height:1200}});
  await page.goto(pathToFileURL(path.join(__dirname,'preview.html')).href);
  for(const [key,name]of cases){
   const screen=payload.screens.find(s=>s.key===key);
   fs.writeFileSync(path.join(out,name+'.svg'),screen.svg+'\n');
   await page.locator('#screens').selectOption(key);
   if(proof)await page.locator('#stage').screenshot({path:path.join(proof,name+'.png')});
  }
  console.log('Exported four revision-04 scenario SVGs and review images.');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});

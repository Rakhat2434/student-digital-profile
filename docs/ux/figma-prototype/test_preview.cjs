const assert = require('node:assert/strict');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const {chromium} = require(require.resolve('playwright', {paths: [process.argv[2] || __dirname]}));
(async()=>{
  const browser=await chromium.launch({headless:true,channel:process.argv[3] || undefined});
  try {
    const page=await browser.newPage({viewport:{width:1500,height:1100}});
    const errors=[];page.on('pageerror',e=>errors.push(e.message));
    await page.goto(pathToFileURL(path.join(__dirname,'preview.html')).href);
    const check=async key=>assert.equal(await page.locator('#stage').getAttribute('data-screen'),key);
    const click=async label=>page.getByRole('button',{name:label,exact:true}).click();
    await check('login');await click('Continue as student');await check('overview');
    await click('Achievements');await click('Add achievement');await click('Save achievement');await check('add-error');
    await click('Fill Title');await check('add-filled');await click('Save achievement');await click('View saved list');await check('achievements-saved');
    await page.locator('#screens').selectOption('teacher');await page.getByRole('button',{name:'Edit or inspect result',exact:true}).first().click();
    await click('Choose demonstration grade');await click('Test invalid 5.00');await check('grade-invalid');
    await click('Choose demonstration grade');await click('Choose B · 3.00');await click('Save result');await check('grade-saved');
    await click('Back to assigned list');await check('teacher-saved');
    await page.setViewportSize({width:430,height:900});await page.locator('#screens').selectOption('mobile');await click('Records');await check('mobile-records');await click('Achievements');await check('mobile-achievements');
    assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
    assert.deepEqual(errors,[]);
    console.log('PASS: real browser student save/validation, teacher correction/save, mobile navigation, no page errors or narrow overflow. Figma execution is separate.');
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});

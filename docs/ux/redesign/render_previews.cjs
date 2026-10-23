const fs = require('node:fs');
const path = require('node:path');
const sharp = require('sharp');

(async () => {
  for (const file of fs.readdirSync(__dirname).filter(name => name.endsWith('.svg'))) {
    await sharp(path.join(__dirname, file))
      .png()
      .toFile(path.join(__dirname, file.replace(/\.svg$/, '.png')));
  }
})().catch(error => {
  console.error(error);
  process.exitCode = 1;
});

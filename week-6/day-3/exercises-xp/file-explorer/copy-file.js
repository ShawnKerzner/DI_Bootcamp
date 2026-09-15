const fs = require('fs/promises');

async function copyFile(src, dst) {
    const content = await fs.readFile(src, 'utf-8');
    await fs.writeFile(dst, content, 'utf-8');
}

copyFile('source.txt', 'destination.txt');
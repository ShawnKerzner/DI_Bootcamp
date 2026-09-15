const fs = require('fs/promises');

async function readFiles(directoryPath) {
    const fileNames = await fs.readdir(directoryPath);
    console.log(fileNames)
}

readFiles('.')
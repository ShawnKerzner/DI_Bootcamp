const fs = { readFile, writeFile } = require('./fileManager.js');

readFile('Hello-World.txt')
  .then(data => console.log(data))
  .catch(err => console.error(err));

writeFile('Bye-World.txt', "Writing to File")
.then(data => console.log(data))
.catch(err => console.error(err));
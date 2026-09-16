const http = require('http');

const menu = {
    "menu": {
        "firstCourse": "Vegetable Soup",
        "mainCourse": "Hamburger",
        "dessert": "FruitSalad"
    }
};

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'application/json'});
    res.end(JSON.stringify(menu));
});

server.listen(3000, () => {
    console.log('Server running on http://localhost:3000')
});
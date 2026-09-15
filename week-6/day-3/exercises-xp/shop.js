const products = require('./products.js');

function findProduct(productName) {
    for (let product of products) {
        if (product["name"] === productName) {
            console.log(product);
        } 
    }
}

findProduct("xbox");
findProduct("basketball");
findProduct("blue shirt");

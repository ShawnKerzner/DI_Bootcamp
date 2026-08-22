// Exercise 1
// function displayNumberDivisible(divisor) {
//     for (i = 0; i < 500; i++) {
//         if (i % divisor == 0) {
//             console.log(i)
//         }
//     }
// }

// displayNumberDivisible(56)

// Exercise 2
const stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
};

const prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
};

const shoppingList = ["banana", "orange", "apple"];
let totalPrice = 0

function myBill() {
    for (item of shoppingList) {
        if (item in stock) {
            if (stock[item] > 0) {
                stock[item] = stock[item] - 1;
                totalPrice += prices[item];
            }
        }
    }
    console.log(totalPrice);
};

myBill()
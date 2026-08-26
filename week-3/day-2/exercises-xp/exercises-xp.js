// // Exercise 1
// function displayNumberDivisible(divisor) {
//     for (i = 0; i < 500; i++) {
//         if (i % divisor == 0) {
//             console.log(i)
//         }
//     }
// }

// displayNumberDivisible(56)

// // Exercise 2
// const stock = {
//     "banana": 6,
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry": 1
// };

// const prices = {
//     "banana": 4,
//     "apple": 2,
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry": 10
// };

// const shoppingList = ["banana", "orange", "apple"];
// let totalPrice = 0

// function myBill() {
//     for (item of shoppingList) {
//         if (item in stock) {
//             if (stock[item] > 0) {
//                 stock[item] = stock[item] - 1;
//                 totalPrice += prices[item];
//             }
//         }
//     }
//     console.log(totalPrice);
// };

// myBill()

// // Exercise 3
// function changeEnough(itemPrice, amountOfChange) {
//     let sumOfChange = 0.0;
//     const coins = [.25, .10, .05, .01];
//     for (let i = 0; i < 4; i++) {
//         sumOfChange += (amountOfChange[i] * coins[i]);
//     }
//     if (sumOfChange > itemPrice) {
//         return true
//     } else {
//         return false
//     }
// }

// console.log(changeEnough(14.11, [2, 100, 0, 0])) // we need false
// console.log(changeEnough(0.75, [0, 0, 20, 5]))  // we need true

// Exercise 4
function hotelCost() {
    while (a = 1) {
        const numOfNights = prompt("How many nights would you like to stay?");
        if (isNaN(numOfNights)) {
            continue
        } else {
            if (numOfNights == "") {
                numOfNights = 0;
            }
            totalHotelCost = (numOfNights * 140);
            return totalHotelCost
        }
    }
}



function planeRideCost() {
    ticketPrice = 0
    while (b = 2) {
        const destination = prompt("What is your destination?").toLowerCase();
        if (destination == "") {
            continue
        } else if (isNaN(destination) == false) {
            continue
        } else if (destination == "london") {
            ticketPrice += 183;
            return ticketPrice
        } else if (destination == "paris") {
            ticketPrice += 220;
            return ticketPrice
        } else {
            ticketPrice += 300;
            return ticketPrice
        }
    }
}

function rentalCarCost() {
    let total_car_cost = 0;

    while (c = 3) {
        const rentalTime = prompt("How many days would you like to rent a car for?");
        if (rentalTime == "") {
            continue
        } else if (isNaN(rentalTime) == true) {
            continue
        } else {
            total_car_cost += (rentalTime * 10);
            if (rentalTime > 10) {
                let discount = total_car_cost * .05;
                return total_car_cost - discount;
            } else {
                return total_car_cost
            }
        }
    }

}

function totalVacationCost() {
    return planeRideCost() + hotelCost() + rentalCarCost()
}

console.log(totalVacationCost());
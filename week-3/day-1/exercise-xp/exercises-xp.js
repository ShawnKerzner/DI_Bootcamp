// const readlineSync = require('readline-sync'); // for exercise 3
// // Exercise 1
// const people = ["Greg", "Mary", "Devon", "James"];
// people.splice(0, 1);
// people.splice(2, 3, 'Jason');
// people.push("Shawn");
// console.log(people.indexOf("Mary"));
// const copyPeople = people.slice(1, -1);
// console.log(people.indexOf("Foo")); // It returns negative 1 because the item 'Foo' is not an item in the list

// for (const item of people) {
//     console.log(item)
// };

// for (const item of people) {
//     if (item == "Devon") {
//         console.log(item);
//         break;
//     }
//     else {
//         console.log(item);
//         break;
//     }
// };

// // Exercise 2
// const colors = ["navy", "black", "white", "beige", "brown"]
// const suffixes = ["st", "nd", "rd", "th", "th"]
// for (let i = 0; i < colors.length; i++) {
//     console.log("My #" + (i + 1) + " choice is " + colors[i])
// }

// for (let i = 0; i < colors.length; i++) {
//     console.log("My " + (i + 1) + suffixes[i] + " choice is " + colors[i])
// }

// // Exercise 3

// do {
//     let user_input = readlineSync.question("Enter a number equal to or greater than 10 to exit the loop.");
//     let user_number = Number(user_input);
//     if (isNaN(user_number)) {
//         console.log("Input must be a number");
//         continue
//     } else {
//         if (user_number < 10) {
//             continue
//         } else {
//             break
//         }
//     }
// } while (1);

// // Exercise 4
// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent: {
//         sarah: [3, 990],
//         dan: [4, 1000],
//         david: [1, 500],
//     },
// }
// console.log(building.numberOfFloors);
// console.log(building.numberOfAptByFloor.firstFloor, building.numberOfAptByFloor.thirdFloor);
// console.log(building.nameOfTenants[1], building.numberOfRoomsAndRent.dan[0]);
// if (building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1] > building.numberOfRoomsAndRent.dan[1]) {
//     building.numberOfRoomsAndRent.dan[1] = 1200
// };
// console.log(building.numberOfRoomsAndRent.dan[1])

// Exercise 5
const family = {
    Dad: 65,
    Mom: 62,
    Ari: 34,
    Erin: 29,
    Shawn: 28,
    Daniel: 27,
}
for (let key in family) {
    console.log(key)
}
for (let key in family) {
    console.log(family[key])
}



const readlineSync = require('readline-sync');
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

// Exercise 3

do {
    let user_input = readlineSync.question("Enter a number equal to or greater than 10 to exit the loop.");
    let user_number = Number(user_input);
    if (isNaN(user_number)) {
        console.log("Input must be a number");
        continue
    } else {
        if (user_number < 10) {
            continue
        } else {
            break
        }
    }
} while (1);
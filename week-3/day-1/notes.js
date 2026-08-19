// let i = 0;
// while (10) {
//     i++;
//     if (i < 5) {
//         continue;
//     }
//     console.log("Hello");
//     if (i == 7) {
//         break;
//     }
// }
// console.log(i)

// let a = 5;
// let b = 10;
// let ab = a * b;
// if (ab > 10) {
//     console.log("Hello");
// } else {
//     console.log(ab);
// }

// let a = 5; // [5] primitive types: string, number, boolean
// let b = [1, 2, 3, 4, 5, 6, 7]; // [REFERENCE] arrays and objects
// const myFirstArray = [1, 2, 3, 4]
// myFirstArray.push(5);
// console.log(myFirstArray[1]);
// let myOtherValue = myFirstArray.pop();
// console.log(myOtherValue)
// console.log(myFirstArray)

// const arrayOfNames = [];
// arrayOfNames.push("Shawn", "Sean", "Shuan");
// console.log(arrayOfNames.length);
// let arrayPop = arrayOfNames.pop()
// console.log(arrayPop)
// console.log(arrayOfNames)

// const myFirstObject = {
//     name: "John",
//     lastname: "Doe"
// };

// // let keyName = 'name';
// // console.log(myFirstObject[keyName]);

// for (let i in myFirstObject) {
//     console.log(i, myFirstObject[i]);
// }

const a = [10, 25, 390, 44];

for (let i = 0; i < a.length; i++) {
    switch (a[i]) {
        case 10:
            console.log("It's 10");
            break;
        case 20:
            console.log("It's 20");
            break;
        case 30:
            console.log("It's 30");
            break;
        default:
            console.log("It's something else")
    }
}
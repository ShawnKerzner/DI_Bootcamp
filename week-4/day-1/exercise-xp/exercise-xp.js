// // Exercise 1
// const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
// colors.forEach((color, index) => {
//     console.log(`${(index + 1)}# choice is ${color}.`);
// })      
// const violet = colors.some((color) =>  color === "Violet");
// if(violet) {
//             console.log("Yeah");
//         } else {
//             console.log("No...");
//         }

// // Exercise 2
// const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
// const ordinal = ["th","st","nd","rd"];

// colors.forEach((color, index) => {
//     console.log(index >= 3 ? `${(index + 1)}${ordinal[0]} choice is ${color}.` : `${(index + 1)}${ordinal[(index +1)]} choice is ${color}.`)
// })

// // Exercise 3
// const fruits = ["apple", "orange"];
// const vegetables = ["carrot", "potato"];

// const result = ['bread', ...vegetables, 'chicken', ...fruits];
// console.log(result);
// // result = ['bread, 'carrot', 'potato', 'chicken', 'apple', 'orange']

// const country = "USA";
// console.log([...country]);
// // ['U', 'S', 'A']

// //------Bonus------
// let newArray = [...[,,]];
// console.log(newArray);
// //[undefined, undefined]

//Exercise 4
const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
             { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
             { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
             { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
             { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
             { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
             { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}];

const welcomeStudents = users.map((dict) => `Hello ${dict["firstName"]}`);
console.log(welcomeStudents);


// // Exercise 1
// function sayHello(): void {
//     console.log("Hello World!");
// }
// sayHello();

// // Exercise 2
// let num: number = 28;
// let myName: string = "Shawn";
// console.log(num, myName);

// // Exercise 3 
// let union: (number | string) = "Kerzner";
// union = 1998;

// //Exercise 4

// function findValue(num: number): string {
//     if (num > 0) {
//         return "positive";
//     }
//     else if (num < 0) {
//         return "negative";
//     }
//     else {
//         return "zero";
//     }
// }

// console.log(findValue(5));

// // Exercise 5
// function getDetails(name: string, age: number): [string, number, string] {
//     return [name, age, `Hello ${name}! You are ${age} years old.`];
// }

// console.log(getDetails("Shawn", 28));

// // Exercise 6 
// type Person = {
//     name: string;
//     age: number;
// };

// function createPerson(name: string, age: number): Person {
//     return {
//         name: name,
//         age: age,
//     }
// }

// console.log(createPerson("Shawn", 28))

// // Exercise 7
// let inputElement = document.getElementById("input-element") as HTMLInputElement;
// inputElement.value = "value here";

// // Exercise 8 
// function getAction(role: string): void {
//     switch (role) {
//         case "admin":
//            console.log("Manage users and settings");
//            break;
//         case "editor":
//             console.log("Edit content");
//             break;
//         case "viewer":
//             console.log("View content");
//             break;
//         case "guest":
//             console.log("Limited access");
//             break;
//         default:
//             console.log("Invalid role");
//             break;
//     }
// }

// getAction("editor")

// Exercise 9
function greet(name? : string): string {
    if (typeof name === "undefined") {
        let defaultGreeting = "Hello there!"
        return defaultGreeting
    } else {
        let personalGreeting = "Hello " + name;
        return personalGreeting
    }
}
console.log(("Obi Wan"));
console.log(greet());


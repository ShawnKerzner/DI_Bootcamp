// // Exercise 1 
// function processValue(input: string | number): void {
//     if(typeof input === "number") {
//         console.log(`$${input}.00`);
//     } else {
//         const reversed: string = input.split("").reverse().join("");
//         console.log(reversed)
//     }
// }
// processValue(12);
// processValue("Hello");

// // Exercise 2
// function sumNumbersInArray(myArray: (string | number) []): number {
//     let result: number = 0
//     for(let item of myArray) {
//         if (typeof item === "number") {
//             result += item
//         }
//     }
//     return result;
// }

// console.log(sumNumbersInArray([1,"hi", 4, "bye", 5]));

// Exercise 3

type AdvancedUser = {
    name: string;
    age: number;
    address?: string;
}

function introduceAdvancedUser(obj: AdvancedUser) {
    if (obj["address"] !== undefined) {
        return `Hello! My name is ${obj["name"]}. I am ${obj["age"]} years old. My address is ${obj.address}.`;
    } else {
        return `Hello! My name is ${obj["name"]}. I am ${obj["age"]} years old.`;
    }
}

const userWithAddress: AdvancedUser = {
  name: "Alice",
  age: 30,
  address: "123 Main St"
};

const userWithoutAddress: AdvancedUser = {
  name: "Bob",
  age: 25
};

console.log(introduceAdvancedUser(userWithAddress));
console.log(introduceAdvancedUser(userWithoutAddress));


// // Exercise 4
// function welcomeUser(name: string, greeting?: boolean ): void {
//     if (greeting === undefined) {
//         console.log("Hello");
//     } else {
//         console.log(`Good morning ${name}! I hope you have an amazing day!`)
//     }
// }

// welcomeUser("Shawn");
// welcomeUser("Shawn", true)
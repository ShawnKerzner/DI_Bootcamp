// // Exercise 1

// type Person = {
//     name: string;
//     age: number;
// }

// type Address = {
//     street: string;
//     city: string;
// }

// type PersonWithAddress = Person & Address;

// let ourObj: PersonWithAddress = {
//     name: "Shawn",
//     age: 28,
//     street: "123 Dev St",
//     city: "TypeScript"
// }

// Exercise 2

// function describeValue(value: number | string) {
//     if (typeof value === "number") {
//         return "This is a number";
//     } else {
//         return "This is a string";
//     }
// }

// console.log(describeValue("Hello"));
// console.log(describeValue(1));

// // Exercise 3

// let someValue: any = "string";
// // let someValue1: string = <string>someValue; // this should also work but VS code is being weird
// let someValue2: string = someValue as string;
// console.log(typeof someValue, /*typeof someValue1,*/ typeof someValue2); 

// Exercise 4

// function getFirstElement(myArray: (string | number) []): string {
//     let string = (myArray[0] as string);
//     return string
// }

// console.log(typeof getFirstElement([1,"two"]));

// // Exercise 5

// function logLength<T extends {length: number}>(parameter: T): void {
//      const parameterLength: number = parameter.length
//      console.log(parameterLength)
// }

// // logLength("Shawn")

// // Exercise 6

// type Person = {
//     name: string;
//     age: number;  
// }

// type Job = {
//     position: string;
//     department: string;
// }

// type Employee = Person & Job;

// function describeEmployee(obj: Employee): string {
//     if (obj["position"] === "Manager") {
//         return `${obj["name"]} is a ${obj["position"]} in ${obj["department"]} and loves to review code!`
//     } else if (obj["position"] === "Developer") {
//         return `${obj["name"]} is a ${obj["position"]} in ${obj["department"]} and loves to code!`
//     }
//     return "Employee info not available"
// }

// console.log(describeEmployee({name: "Shawn", age: 28, position: "Developer", department: "R&D"}))
// console.log(describeEmployee({name: "Shawn", age: 28, position: "Manager", department: "R&D"}))

// Exercise 7
 function formatInput<T>(parameter: T) {
    let string = parameter as string;
    return string.toString()
 }

 console.log(typeof formatInput("Test"));
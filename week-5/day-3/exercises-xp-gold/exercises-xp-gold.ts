// Exercise 1 
function processValue(input: string | number): void {
    if(typeof input === "number") {
        console.log(`$${input}.00`);
    } else {
        const reversed: string = input.split("").reverse().join("");
        console.log(reversed)
    }
}
processValue(12);
processValue("Hello");

// // Exercise 2
// function sumNumbersInArray(myArray: string | number): string {
//     let result: number = 0
//     for(let item of myArray)
// }

// Exercise 4
function welcomeUser(name: string, greeting?: boolean ): void {
    if (greeting === undefined) {
        console.log("Hello");
    } else {
        console.log(`Good morning ${name}! I hope you have an amazing day!`)
    }
}

welcomeUser("Shawn");
welcomeUser("Shawn", true)
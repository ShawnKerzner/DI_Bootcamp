// const student = {
//     name: "John",
//     age: "28",
//     course: "Full Stack"
// }

// let jsonStudent = JSON.stringify(student);

// console.log(typeof jsonStudent);
// console.log(jsonStudent);

// const backToTheFuture = JSON.parse(jsonStudent);
// console.log(typeof backToTheFuture);
// console.log(backToTheFuture);

// const event = new Date('May 21, 2020 12:15:30 UTC');
// const jsonDate = event.toJSON();
// console.log(jsonDate);

// try {
//     // here's what we try
// } catch (e) {
//     // her we handle the error
// } finally {
//     // what runs in the end regardless
// }

// console.log("starting the try block")
// hello
// console.log("finishing the try block")

// try {
//     console.log("starting the try block")
//     if (0 === 0) {
//         throw new Error("My Error!")
//     }
//     console.log("finishing the try block")
// } catch (e) {
//     console.log("starting the catch block")
//     console.log(`
//         Error Name : ${e.name},
//         Error Msg : ${e.message},
//         Error Stack : ${e.stack}`)
// } finally {
//     console.log("Function completed")
// }

// const myFunction = (a, b) => {
//     try {
//         const result = a + b;
//         if (result % 2 == 1) throw new Error("Oh no you are so odd just like your number!")
//         return result
//     } catch (e) {
//         console.log("Error " + e.name);
//         console.log(e.message)
//     }
// }

// console.log(myFunction(3, 4));
// console.log(myFunction(1, 1));

const str = "Happy Birthday";
const patt = /birthday/i;
const result = str.match(patt)
console.log(result);
for (const i in result) {
    console.log(result[i])
}
console.log(result["index"])
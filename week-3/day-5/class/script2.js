// const myArray = [1, 2, 3, 4, 5];

// // myArray.push(6);
// // let a = myArray.pop();
// // let b = myArray.shift();
// // myArray.unshift(-1);
// // console.log(myArray);

// for (let i = 0; i < myArray.length; i++) {
//     myArray[i]++
// }
// console.log(myArray)

// const a = 5; // the value is immutable
// const b = [1, 2, 3]; // the value is a reference to the array, the reference itself is immutable
// but not the actual content of the array

// const myArray = ["Hello", "Goodbye", "Hi", "Bye"]

// for (let item of myArray) {
//     console.log(item)
// }

// for (let i = 0; i < myArray.length; i++) {
//     console.log(myArray[i])
// }

// for (let word in myArray) {
//     console.log(word)
// }


// const numbers = [10, 11, 12, 15, 20];
// let result = 0;
// const mySumFunction = item => {
//     // if (item % 2 == 1) {
//     //     result += item;
//     // }
//     result += item % 2 == 1 ? item : 0;
// }

// numbers.forEach(mySumFunction);
// console.log(result)

// const numbers = [10, 11, 12, 15, 20];
// const myCondition = (item) => {
//     return item % 2 == 1
// }
// // forEach() -> take each element and run a fucntion using this element
// // .some: .forEach() true or false
// // .every: .forEach() all true all false
// console.log(numbers.some(myCondition))
// console.log(numbers.every(myCondition))
// const numbers = [10, 11, 12, 15, 20];
// // const myCondition = item => item % 2 === 1;
// // console.log(numbers.filter(myCondition))
// const myCondition = item => item > 12 || item < 11;
// console.log(numbers.filter(myCondition))
// const numbers = [10, 11, 12, 15, 20];
// const mySumFunction = (accumulator, item) => accumulator += item % 2 === 1 ? item : 0;
// console.log(numbers.reduce(mySumFunction, 0));

const numbers = [10, 11, 12, 15, 20];
const mySumFunction = (accumulator, item) => accumulator *= item % 2 === 1 ? item : 1;
console.log(numbers.reduce(mySumFunction, 1))
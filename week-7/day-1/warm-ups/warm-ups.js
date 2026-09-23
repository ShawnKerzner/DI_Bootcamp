// Exercise 1
console.log("Exercise 1\n" + '—'.repeat(10));
let x = 0;
console.log(x++); // 0; x = x + 1; x = 1 value and then increment
console.log(++x); // 1; x = x + 1; x = 2 increment and then value

// Exercise 2
console.log("\nExercise 2\n" + '—'.repeat(10));
const arr = [1, 2, 3]; // length of 3
arr[10] = 99;
console.log(arr) // [1,2,3, undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined, 99]
console.log(arr.length); // 11

// Exercise 3
console.log("\nExercise 3\n" + '—'.repeat(10));
const comp = 5 === 5 && 5 == '5'; // true && true = true
console.log(comp * 2); // true * 2; false = 0 and true = 1 so 1 * 2 = 2

// Exercise 4
console.log("\nExercise 4\n" + '—'.repeat(10));
const fns = [];
for (var i = 0; i < 3; i++) {
    fns.push(() => i); // a reference to this function
}
console.log(fns)
console.log(fns.map(f => f())); // provides a function to each element of the array and creates a new array of the same length

// Exercise 5
console.log("\nExercise 5\n" + '—'.repeat(10));
const a = { n: 1 }; // reference 1
const b = a; // reference 1
b.n = 2;
const c = { ...a }; // reference 2
c.n = 3;
console.log(a.n, b.n, c.n);

// Exercise 6
console.log("\nExercise 6\n" + '—'.repeat(10));
console.log(greet()); // "hi"
console.log(typeof sayBye); // undefined because no value yet
function greet() {
    return "hi";
}
var sayBye = () => "bye"; // hoisting

// Exercise 7
console.log("\nExercise 7\n" + '—'.repeat(10));
const myFunFunc = (async () => {
    console.log(await new Promise((resolve, _) => {
        setTimeout(() => {
            resolve(true)
        }, 10);
    }));
})()
console.log(myFunFunc);

// Exercise 8
console.log("\nExercise 8\n" + '—'.repeat(10));
const time1 = setTimeout(() => {
    console.log('A');
}, 100);
const time2 = setInterval(() => {
    console.log('B');
}, 100);
const time3 = new Promise((resolve, _) => {
    setTimeout(() => {
        resolve(true)
    }, 250)
});
time3.then(() => {
    console.log('C');
    clearInterval(time2);
})

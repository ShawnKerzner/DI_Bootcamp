// let sentence = "The movie is not that bad, I like it.";
// let sentenceLower = sentence.toLowerCase();
// const start = "not"
// const end = "bad"
// let wordNot = sentenceLower.indexOf(start);
// let wordBad = sentenceLower.indexOf(end);

// if (wordNot < wordBad || false) {
//     console.log(sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + end.length));
// } else {
//     console.log(sentence);
// }
// going to wrap this code into a function later

// function helloWorld() {
//     console.log("Hello World!!");
// }

const helloWorld = () => {
    console.log("Hello World!!");

}

helloWorld();

const findSum = (a, b) => {
    return a + b
};

console.log(findSum(1, 3));

const numbers = [1, 2, 3, 4, 5, 6];
const sums = []
for (let i = 0; i < numbers.length - 1; i += 2) {
    sums.push(findSum(numbers[i], numbers[i + 1]));
}

const myFunction = (x, y = 6) => {
    let m = 100;
    console.log(m)
    return x + y
}

console.log(m)
console.log(myFunction(0))
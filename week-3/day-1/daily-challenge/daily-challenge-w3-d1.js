// const sentence = "The movie is not that bad, I like it.";
// const wordNot = sentence.indexOf("not");
// const wordBad = sentence.indexOf("bad");
// if (wordBad > wordNot) {
//     const goodSwitch = "The movie is good, I like it."
//     console.log(goodSwitch)
// } else {
//     console.log(sentence)
// };

// Refactor 
let sentence = "The movie is not that bad, I like it.";
let sentenceLower = sentence.toLowerCase();
const start = "not"
const end = "bad"
let wordNot = sentenceLower.indexOf(start);
let wordBad = sentenceLower.indexOf(end);

if (wordNot < wordBad || false) {
    console.log(sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + end.length));
} else {
    console.log(sentence);
}

// if (wordBad > wordNot) {
//     console.log(sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + end.length));
// } else {
//     console.log(sentence);
// }
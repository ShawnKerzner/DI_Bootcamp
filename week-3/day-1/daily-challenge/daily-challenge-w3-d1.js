const sentence = "The movie is not that bad, I like it.";
const wordNot = sentence.indexOf("not");
const wordBad = sentence.indexOf("bad");
if (wordBad > wordNot) {
    const goodSwitch = "The movie is good, I like it."
    console.log(goodSwitch)
} else {
    console.log(sentence)
};




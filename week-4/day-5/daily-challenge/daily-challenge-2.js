const morse = `{
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}`

function toJs() {
    const morseJs = JSON.parse(morse);
    return new Promise ((resolve, reject) => {
        if (morseJs.length !== 0) {
            resolve(morseJs)
        } else {
            reject("Error. Object is empty")
        }       
    });
}

function toMorse(morseJs) {
    return new Promise((resolve, reject) => {
        const sentence = prompt("Type a sentence:").toLowerCase();
        const morseTranslation = [];
        for (let char of sentence) {
            if (char === " ") {
                morseTranslation.push("/");
            } else if (morseJs[char]) {
                morseTranslation.push(morseJs[char]);
            } else {
                reject(`Error: "${char}has no morse equivalent"`);
                return;
            }
        }
        resolve(morseTranslation);
    });
    
}

function joinWords(morseTranslation) {
    const result = morseTranslation.join("\n");
    console.log(result);
    return result;
}


toJs()
    .then((morseJs) => toMorse(morseJs))
    .then((morseTranslation) => joinWords(morseTranslation))
    .catch((err) => console.log(err));




const anagrams = (stringOne, stringTwo) => {
    let stringOneFiltered = stringOne.toLowerCase().split('').filter(char => char !== ' ').sort().join('');
    let stringTwoFiltered = stringTwo.toLowerCase().split('').filter(char => char !== ' ').sort().join('');

    if (stringOneFiltered == stringTwoFiltered) {
        console.log("Anagram!")
    } else {
        console.log("Not an anagram :'(")
    }
}

anagrams("astronomer", "Moon starer");
anagrams("This is not an anagram", "Bananas")
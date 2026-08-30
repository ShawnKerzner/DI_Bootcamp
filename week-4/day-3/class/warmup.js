const findAnagrams = (words) => {
    const wordGroups = {};
    for (const word of words) {
        console.log(wordGroups)
        const wordKey = word.toLowerCase().split("").join("");
        if (!wordGroups[wordKey]) wordGroups[wordKey] = [];
        wordGroups[wordKey].push(word);
    }
    console.log(wordGroups);
    return Object.values(wordGroups)
}
const words = ["name", "Mean", "Man"];
findAnagrams(words);
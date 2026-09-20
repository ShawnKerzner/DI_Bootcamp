const express = require('express');
const app = express();

let currentAnswer = null;
let currentPlayer = {
    score:0
};

const emojis = [
    { emoji: '😀', name: 'Smile' },
    { emoji: '🐶', name: 'Dog' },
    { emoji: '🌮', name: 'Taco' }
];

app.use(express.json());

app.listen(5000, () => {
    console.log("server is listening on port 5000...")
});

app.get('/round', (req, res) => {
    const randomNumber = Math.floor((Math.random() * emojis.length));
    const randomEmoji = emojis[randomNumber];
    const wrongAnswers = emojis.filter((emoji) => {
    return (emoji.name != randomEmoji.name)
    })
    const randomIndex = Math.floor(Math.random() * (wrongAnswers.length + 1));
    wrongAnswers.splice(randomIndex, 0, randomEmoji);
    const answersShuffled = wrongAnswers
    currentAnswer = randomEmoji;
    const data = {
        emoji: currentAnswer.emoji,
        options: answersShuffled
    }
    res.status(200).json(data)
})

app.post('/guess', (req, res) => {
    const guess = req.body.guess;
    if (guess === currentAnswer.name){
        currentPlayer.score += 1;
        res.status(200).json({correct: true, score: currentPlayer.score});
    } else {
        res.status(200).json({correct: false, answer: currentAnswer.name})
    }
})
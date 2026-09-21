const express = require('express');
const app = express();

let currentAnswer = null;
let currentPlayer = null;
let players = [];

const emojis = [
    { emoji: '😀', name: 'Smile' },
    { emoji: '🐶', name: 'Dog' },
    { emoji: '🌮', name: 'Taco' }
];

app.use(express.json());
app.use(express.static(__dirname));

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

app.post ('/newPlayerEntry', (req, res) => {
    const playerName = req.body.name;
    const newPlayer = {name: playerName, score: 0};
    currentPlayer = newPlayer;
    players.push(currentPlayer);
    res.status(200).json({message: "New player confirmed"});
})

app.get('/leaderboard',  (req, res) => {
    const topThree = players.sort((a, b) => {
        return b.score - a.score
    }).slice(0,3);
    res.status(200).json(topThree);
})

app.listen(5000, () => {
    console.log("server is listening on port 5000...")
});



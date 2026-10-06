import { triviaQuestions } from "../models/triviaQuestions.js";
import express from 'express';

const router = express.Router();

let currentQuestion = 0;
let  score = 0;

router.get('/', (req, res) => {
    currentQuestion = 0;
    score = 0;
    let question = triviaQuestions[0].question;
    res.status(200).json({ question: question })
});

export default router;

router.post('/', (req, res) => {
    if (currentQuestion === triviaQuestions.length) {
        currentQuestion = 0;
        score = 0;
    }
    const userAnswer = req.body.answer
    if (!userAnswer) {
        res.status(400).json( {Error: "no answer found"});
        return
    }
    let feedBack;
    if (userAnswer === triviaQuestions[currentQuestion].answer) {
        feedBack = 'Correct';
        score += 1;
    } else {
        feedBack = 'Incorrect';
    }
    currentQuestion += 1;
    if (currentQuestion === triviaQuestions.length) {
        res.status(200).json(`${feedBack} Score: ${score} Thank you for playing`);
        
    } else {
        res.status(200).json(`${feedBack}\n ${triviaQuestions[currentQuestion].question}`);
    }
});

router.get('/score',(req, res) => {
    res.status(200).json(score)
});
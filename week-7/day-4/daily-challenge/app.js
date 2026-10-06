import express from 'express'
import router from './routes/quiz.js';

const app = express();

app.use(express.json());
app.use('/quiz', router)

app.listen(3000, 'localhost', () => {
    console.log("Server is active and listening on Port 3000...")
});


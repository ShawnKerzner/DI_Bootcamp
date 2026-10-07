import express from 'express';
import router from './routes/index.js';

const app = express();

app.listen(3000, () => {
    console.log("Server listening on port 3000")
});

app.use('/', router);
import express, { json } from 'express';
import router from './routes/todos.js';

const app = express();

app.use(json());
app.use('/todos', router);

app.listen(3000, () => {
    console.log("Server listening on port 3000")
});
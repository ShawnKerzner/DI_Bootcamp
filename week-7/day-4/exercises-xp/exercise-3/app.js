import express, {json} from 'express';
import router from './routes/books.js';

const app = express();

app.use(json());
app.use('/books', router);

app.listen(3000, () => {
    console.log("Server listening on port 3000")
}); 
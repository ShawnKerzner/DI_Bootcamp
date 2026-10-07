import express from 'express';

const router = express.Router();

const books = [];
let bookNum = 0;

router.get('/', (req, res) => {
    res.json(books);
});

router.post('/', (req, res) => {
    if (!req.body.title) {
        res.status(400).json({error: "Book is missing title"});
        return;
    }

    bookNum += 1;

    const newBook = {
        id: bookNum,
        title: req.body.title
    }

    books.push(newBook);
    res.status(201).json(newBook)
});

router.put('/:id', (req, res) => {
    const id = Number(req.params.id);
    const book = books.find(book => book.id === id);

    if(!book) {
        return res.status(404).json({ error: "Book not found"});
    }

    if (!req.body.title) {
        res.status(400).json({error: "Book is missing title"});
        return;
    }
    book.title = req.body.title;
    res.json(book);
});

router.delete('/:id', (req, res) => {
    const id = Number(req.params.id);
    const index = books.findIndex(book => book.id === id);

    if(index === -1) {
        return res.status(404).json({ error: "Book not found"});
    }

    books.splice(index, 1);
    res.json({ message: "Book deleted"});
});


export default router;
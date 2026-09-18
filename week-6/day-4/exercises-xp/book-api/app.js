const express = require("express");
const app = express();
const books = [
    {
        id:1,
        title: "book 1",
        author: "author 1",
        publishedYear: "2026"
    },
    {
        id:2,
        title: "book 2",
        author: "author 2",
        publishedYear: "2022"
    },
    {
        id:3,
        title: "book 3",
        author: "author 3",
        publishedYear: "2025"
    }
];

app.listen(5000, () => {
    console.log("server is listening on port 5000...");
})

app.use(express.json());

app.get('/api/books', (req, res) => {
    res.status(200).json(books)
})

app.get('/api/books/:bookId', (req, res) => {
    const matchedBook = books.find((book) => {
        return Number(req.params.bookId) === book.id
    })
    if(!matchedBook) {
        res.status(404).json({ message: "Book not found" })
    } else {
        res.status(200).json(matchedBook)
    }
})

app.post('/api/books', (req, res) => {
    const onlyIdArray = books.map((book) => {
        return book.id;
    })
    const newId = Math.max(...onlyIdArray) + 1;
    const newBook = {id: newId, title: req.body.title, author: req.body.author, published: req.body.publishedYear};
    books.push(newBook);
    res.status(201).json(newBook)
})
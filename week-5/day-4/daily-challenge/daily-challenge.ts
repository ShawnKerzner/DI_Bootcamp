interface Book {
    title: string;
    author: string;
    publishedYear: number;
    isbn: string;
    genre?: string
}

// interface DigitalBook extends Book {
//     downloadable: string;
// }

class Library {

    private books: Book[] = [];

    constructor() {
        this.books = []
    }

    getBookAuthor(isbn: string): string {
        const book = this.books.find(book => book.isbn === isbn);
        return book?.author || "";
    }

    getBookTitles() {
        return this.books.map(book => book.title);
    }

    getBookDetails(isbn: string): string{
        const book = this.books.find(book => book.isbn === isbn);
        let result = "Book does not exist";
        if (book) {
            result = `Book Title: ${book.title}\nAuthor: ${book.author}\nPublished: ${book.publishedYear}\nISBN: ${book.isbn}\n${book.genre ? "Genre: " + book.genre : "" }`;
        }
        return result
    }

    addBook(newBook: Book): void {
        this.books.push(newBook);
    }
}

class DigitalLibrary extends Library {
    readonly website: string;
    constructor(website: string) {
        super();
        this.website = website;
    }

    listBooks(){
        let result = this.getBookTitles();
        return result;
    }

}

const genericBooks = [
    
  { title: "1984", author: "George Orwell", publishedYear: 1949, isbn: "9780451524935", genre: "Dystopian" },
  { title: "To Kill a Mockingbird", author: "Harper Lee", publishedYear: 1960, isbn: "9780061120084", genre: "Fiction" },
  { title: "The Hobbit", author: "J.R.R. Tolkien", publishedYear: 1937, isbn: "9780547928227", genre: "Fantasy" },
  { title: "Brave New World", author: "Aldous Huxley", publishedYear: 1932, isbn: "9780060850524", genre: "Dystopian" },
  { title: "The Great Gatsby", author: "F. Scott Fitzgerald", publishedYear: 1925, isbn: "9780743273565", genre: "Fiction" },
  { title: "Fahrenheit 451", author: "Ray Bradbury", publishedYear: 1953, isbn: "9781451673319", genre: "Dystopian" },
  { title: "Dune", author: "Frank Herbert", publishedYear: 1965, isbn: "9780441172719", genre: "Science Fiction" },
  { title: "Pride and Prejudice", author: "Jane Austen", publishedYear: 1813, isbn: "9780141439518", genre: "Romance" },
  { title: "The Catcher in the Rye", author: "J.D. Salinger", publishedYear: 1951, isbn: "9780316769488", genre: "Fiction" },
  { title: "Moby-Dick", author: "Herman Melville", publishedYear: 1851, isbn: "9781503280786" }
];




let ourLibrary = new DigitalLibrary("amazon");

for(let book of genericBooks) {
    ourLibrary.addBook(book);
}

console.log(ourLibrary.getBookDetails("9780061120084"));
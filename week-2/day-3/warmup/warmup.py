class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.lended = True

    def get_info(self):
        if self.lended == True:
            status = "is home"
        else:
            status = "has been lended to somebody"
        return f"{self.title}: {self.author} {status}"

    def lend_book(self):
        self.lended = True

    def return_book(self):
        self.lended = False


library = []


def create_a_library():
    while True:
        current = input("Book Title (type 'exit' to stop): ")
        if current == "exit":
            break
        author = input("Book author: ")
        library.append(Book(current, author))
    return library


my_library = create_a_library()

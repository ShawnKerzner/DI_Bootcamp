class Genre():
    def __init__(self, genre, list):
        self.genre = genre
        self.list = list

    def get_books(self):
        return f"{self.list}"

    def show_info(self):
        return f"{self.genre}.Here are some books in that genre: {self.list}"

    def get_genre(self):
        return self.genre


genre1 = Genre("fiction", [1, 2, 1])

print(genre1.get_books())
print(genre1.show_info())
print(genre1.get_genre())

class

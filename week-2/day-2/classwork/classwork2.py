class Computer():

    def __init__(self):
        self.name = "Apple Computer"  # public
        self.__max_price = 900  # private

    def sell(self):            # public method
        print(f"Selling Price: {self.__max_price}")

    def __sell(self):          # private method
        print('This is private method')

    def set_max_price(self, price):
        self.__max_price = price


c = Computer()
c.sell()
# >> Selling Price: 900


class Parrot():

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Penguin():

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")

# common interface


def flying_test(bird):
    bird.fly()


# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
# >> Parrot can fly

flying_test(peggy)
# >> Penguin can't fly


class A():

    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C():
    def dothis(self):
        print("doing this in C")


class D(B, C):
    pass


d_instance = D()
d_instance.dothis()


class Book():
    def __init__(self, title, author, publication_date, price):
        self.title = title
        self.author = author
        self.publication = publication_date
        self.price = price

    def present(self):
        print(f'Title: {self.title}')


class Fiction(Book):
    def __init__(self, title, author, publication_date, price, is_awesome):
        super().__init__(title, author, publication_date, price)
        self.genre = 'Fiction'
        self.is_awesome = is_awesome
        if self.is_awesome:
            self.bored = False
            print('Woow this is an awesome book')
        else:
            self.bored = True
            print('I am very bored')


if __name__ == '__main__':
    foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
    foundation.present()
    print(foundation.price)
    print(foundation.bored)
    boring_book = Fiction('boring_guy', 'boring_title',
                          'boring_date', '9000£', False)
    print(boring_book.bored)

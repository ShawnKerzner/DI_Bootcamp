class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        else:
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                new_amount = self.amount + other.amount
                self.amount = new_amount
                return self
            else:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        else:
            new_amount = self.amount + other
            self.amount = new_amount
            return self


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1)
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>

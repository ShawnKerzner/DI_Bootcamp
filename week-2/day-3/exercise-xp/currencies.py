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
                    f"Cannot add between Currency type <dollar> and <shekel>")

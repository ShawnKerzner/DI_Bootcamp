# Exercise 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Simba", 8)
cat2 = Cat("Ash", 7)
cat3 = Cat("Kuuz", 3)


def find_oldest_cat(*cats):
    oldest = max((cats), key=lambda item: item.age)
    return oldest


result = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {result.name} and is {result.age} years old")

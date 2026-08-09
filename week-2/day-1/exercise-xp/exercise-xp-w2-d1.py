# Exercise 1
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age


# cat1 = Cat("Simba", 8)
# cat2 = Cat("Ash", 7)
# cat3 = Cat("Kuuz", 3)


# def find_oldest_cat(*cats):
#     oldest = max((cats), key=lambda item: item.age)
#     return oldest


# result = find_oldest_cat(cat1, cat2, cat3)
# print(f"The oldest cat is {result.name} and is {result.age} years old")

# Exercise 2


class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(dog):
        return f"{dog.name} goes woof!"

    def jump(dog):
        return f"{dog.name} jumps {dog.height * 2} cm high!"


davids_dog = Dog("Max", 50)
sarahs_dog = Dog("Willow", 75)

dogs = (davids_dog, sarahs_dog)

for dog in dogs:
    print(f"{Dog.bark(dog)}")
    print(f"{Dog.jump(dog)}")


def dog_height_comparison(dog1, dog2):
    if dog1.height > dog2.height:
        print(f"{dog1.name} is bigger")
    elif dog2.height > dog1.height:
        print(f"{dog2.name} is bigger")
    else:
        print("Both dogs are the same height!")


dog_height_comparison(davids_dog, sarahs_dog)

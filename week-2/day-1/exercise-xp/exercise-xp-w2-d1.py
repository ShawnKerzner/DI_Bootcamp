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

    def bark(self):
        return f"{self.name} goes woof!"

    def jump(self):
        return f"{self.name} jumps {self.height * 2} cm high!"


davids_dog = Dog("Max", 50)
sarahs_dog = Dog("Willow", 75)

dogs = (davids_dog, sarahs_dog)

for dog in dogs:
    print(f"{dog.bark()}")
    print(f"{dog.jump()}")


def dog_height_comparison(dog1, dog2):
    if dog1.height > dog2.height:
        print(f"{dog1.name} is bigger")
    elif dog2.height > dog1.height:
        print(f"{dog2.name} is bigger")
    else:
        print("Both dogs are the same height!")


dog_height_comparison(davids_dog, sarahs_dog)

# Exercise 3


# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for lyric in self.lyrics:
#             print(lyric)


# stairway = Song(["There’s a lady who's sure", "all that glitters is gold",
#                 "and she’s buying a stairway to heaven"])

# stairway.sing_me_a_song()

# Exercise 4


# class Zoo:
#     def __init__(self, zoo_name):
#         self.zoo_name = zoo_name

#     animals = []

#     def add_animal(self):
#         if new_animal not in Zoo.animals:
#             Zoo.animals.append(new_animal)

#     def get_animals(animals):
#         print(animals)

#     def sell_animal(animal_sold):
#         if animal_sold in Zoo.animal:
#             Zoo.animal.remove(animal_sold)

#     def sort_animals(animals):
#         animals_dict = {}
#         sorted_animals = sorted(animals)
#         for animal in animals:
#             if animal:
#                 first_letter = animal[0].lower()
#                 animals_dict[first_letter].append(animal)

#     def get_groups(animals_dict):
#         print(animals_dict)


# ramat_gan_zoo = Zoo("Ramat Gan Zoo")
# ramat_gan_zoo.add_animal("Giraffe")
# ramat_gan_zoo.add_animal("Bear")
# ramat_gan_zoo.add_animal("Baboon")
# ramat_gan_zoo.get_animals()
# ramat_gan_zoo.sell_animal("Bear")
# ramat_gan_zoo.get_animals()
# ramat_gan_zoo.sort_animals()
# ramat_gan_zoo.get_groups()

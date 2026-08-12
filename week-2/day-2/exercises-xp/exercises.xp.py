import random
# # Exercise 1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())


# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'


# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# class Siamese(Cat):
#     pass


# toby = Bengal("Toby", 3)
# crouton = Chartreux("Crouton", 5)
# fuego = Siamese("Fuego", 1)

# all_cats = [toby, crouton, fuego]

# sara_pets = Pets(all_cats)

# sara_pets.walk()

# Exercise 2


# class Dog():
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

#     def bark(self):
#         return f"{self.name} is barking"

#     def run_speed(self):
#         return self.weight / self.age * 10

#     def fight(self, other_dog):
#         my_stats = self.run_speed() * self.weight
#         foe_stats = other_dog.run_speed() * other_dog.weight
#         if my_stats > foe_stats:
#             return f"{self.name} wins"
#         else:
#             return f"{other_dog.name} wins"


# dog1 = Dog("Barcus", 12, 54)
# dog2 = Dog("Brodie", 6, 37)
# dog3 = Dog("Batman", 2, 45)

# print(dog1.bark())
# print(dog2.run_speed())
# print(dog1.fight(dog2))

# # Exercise 3


# class PetDog(Dog):
#     def __init__(self, trained=False):
#         self.trained = trained

#     def train(self):
#         self.trained = True
#         return f"{self.bark()}"

#     def play(self, *args):
#         print(f"{args} all play together")

#     def do_a_trick(self):
#         if self.trained == True:
#             print()

# Exercise 4
class Person():
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False


class Family():
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        person = Person(first_name, age)
        person.last_name = self.last_name
        self.members.append(person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18() == True:
                    print(
                        "You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends."
                          )

    def family_presentation(self):
        print(f"{self.last_name}")
        for member in self.members:
            print(f"{member.first_name}: {member.age}")


family1 = Family("Kerzner")
family1.born("Kevin", 65)
family1.born("Rivkah", 62)
family1.born("Ari", 34)
family1.born("Erin", 29)
family1.born("Shawn", 28)
family1.born("Daniel", 27)
family1.family_presentation()
family1.check_majority("Shawn")

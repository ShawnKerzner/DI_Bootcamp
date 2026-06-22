import random

# Challenge 1:
def display_message():
    print("I am learning about functions in Python")

display_message()

# Challenge 2:
def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Harry Potter")

# Challenge 3:
def describe_city(city, country="Unknown"):
    print(f"{city} is located in {country}")

describe_city("Rome", "Italy")
describe_city("London")

# Challenge 4:
def random_number(a):
    random_num = random.randint(1, 100)
    if a == random_num:
        print(f"Success!!! {random_num} {a}")
    else:
        print(f"Better luck next time. {random_num} {a}")

random_2 = random.randint(1,100)
random_number(random_2)

# Challenge 5:
def make_shirt(size="large", text="I love Python"):
    print(f"This shirt is a size {size} and has the text '{text}' on it")

make_shirt("medium", "I love NY")
make_shirt()
make_shirt(size="medium")
make_shirt("small", "small shirt for a small guy")
make_shirt(size="small", text="hello")

# Challenge 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    return(magician_names)

magician_list = map(show_magicians, magician_names)
print(list(magician_names))

def make_great(magicians):
    for index, value in enumerate(magicians):
        magicians[index] = value + " the great"
        continue
    return magicians       
    
make_great(magician_names)
print(list(magician_names))

# Exercise 7

def get_random_temp():
    temp = random.randint(-10, 40)
    return temp

def main(temp):
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today")
    if temp == 0 or temp < 16:
        print("Quite chilly! Don't forget your coat")


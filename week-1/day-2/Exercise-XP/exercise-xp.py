# Exercise 1: Hello World
print("Hello world " * 4)

# Exercise2: Some Math
print((99^3)*8)

# Exercis 3: What is the output?
# >>> 5 < 3 # False
# >>> 3 == 3 # True
# >>> 3 == "3" # TypeError cannot compare int to strings
# >>> "3" > 3 # Type Error same reason as above
# >>> "Hello" == "hello" # False capitalization counts
# print(5 < 3)
# print(3 == 3)
# print(3 == "3")
# print("3" > 3)
# print("Hello" == "hello")

# Exercise 4: Your computer brand
computer_brand = "Lenovo"
print(f"I have a {computer_brand} computer")

# Exercise 5: Your information
name = "Shawn"
age = 27
shoe_size = (44.5)
info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."
print(info)

# Exercise 6: A & B
a = 18
b = 2
if a > b:
    print("Hello World")

# Exercise 7: Odd of Even
number = int(input("Enter a nmuber: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Exercise 8: What's your name
my_name = "Shawn"
users_name = input("Please enter your name ")
if my_name == users_name:
    print("One of us! One of us! One of us!")
else:
    print("Ew. You should leave.")

# Exercise 9: Tall enough to ride a roller coaster
user_height = int(input("how tall are you in cm? "))
if user_height < 145:
    print("You need to grow some more to ride")
else:
    print("You are tall enough to ride")

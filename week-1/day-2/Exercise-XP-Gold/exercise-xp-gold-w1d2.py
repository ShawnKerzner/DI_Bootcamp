import random
# Exercise 1
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
list_1.extend(list_2)
print(list_1)

# Exercise 2
for num in range(1500, 2000):
    if num % 5 == 0 and num % 7 == 0:
        print(num)

# Exercise 3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
while True:
    user_name = input("Enter your name: ")
    try:
        name_index = names.index(user_name)
        print(name_index)
        break
    except ValueError:
        print(f"Sorry username not found")

# Exercise 4
nums_list = []
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))
num_3 = int(input("Enter a number: "))
nums_list.extend([num_1, num_2, num_3])
print(max(nums_list))

# Exercise 5
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in alphabet:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print(f"{char} : vowel")
        continue
    else:
        print(f"{char} : consonant")
        continue

# Exercise 6

words_list = []
while len(words_list) < 7:
    word_input = input("Please enter a word for the list: ")
    words_list.append(word_input)
while True:
    try:
        letter = input("Enter a single character: ")
        if len(letter) != 1:
            raise ValueError
        break
    except ValueError:
        print("Invalid input! You must enter exactly ONE character.\n")
for word in words_list:
    found = False
    for char in word:
        if char == letter:
            print(f"{letter} found in {word} Index: {word.index(char)}")
            found = True
            break
        if found == False:
            print(f"Sorry but {letter} is not found in {word}")

# Exercise 7
million_list = range(1, 1000000)
print(min(million_list))
print(max(million_list))
print(sum(million_list))

# Exercise 8
numbers_list = (input("Enter some numbers: "))
print(list(numbers_list))
print(tuple(numbers_list))

# Exercise 9
attempts = 0
correct = False
random_number = random.randint(1, 9)
while correct == False:
    guess = int(input("Guess a number 1 - 9 or enter 0 to quit: "))
    if guess == 0:
        break
    if guess == random_number:
        print("Winner")
        correct = True
    else:
        attempts += 1
        print("Try again")
print(f'attempts: {attempts}')

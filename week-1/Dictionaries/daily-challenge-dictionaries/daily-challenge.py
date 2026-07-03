# Exercise 1

dictionary = {}
user_input = input("Please enter a word: ")
for index, char in enumerate(user_input):
    if char not in dictionary:
        dictionary[char] = [index]
    else:
        dictionary[char].append(index)
print(dictionary)
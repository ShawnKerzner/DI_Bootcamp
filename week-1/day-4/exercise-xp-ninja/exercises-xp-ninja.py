import math
import random
import sys
# # Exercise 1:
# # Q = Square root of [(2 * C * D)/H]
# c = int(50)
# h = int(30)
# result = []
# user_input = input("Please enter 3 numbers seperated by commas: ")
# print(user_input)
# numbers = [int(num) for num in user_input.split(",")]
# print(numbers)
# for d in numbers:
#     q = int(math.sqrt((2 * c * d) // h))
#     result.append(q)
#     continue
# print(result)

# # Exercise 2
# # step 1
# integers_list = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7, 7, 47]
# # step 2
# print(integers_list)
# sorted_list = sorted(integers_list)
# sorted_list.reverse()
# print(sorted_list)
# list_sum = sum(integers_list)
# print(list_sum)
# # step 3
# first_last_list = integers_list[:1] + integers_list[-1:]
# print(first_last_list)
# # step 4
# over_fifty = []
# for integer in integers_list:
#     if integer > 10:
#         over_fifty.append(integer)
# print(over_fifty)
# # step 5
# under_ten = []
# for integer in integers_list:
#     if integer < 50:
#         under_ten.append(integer)
# print(under_ten)
# # step 6
# squared_list = []
# for integer in integers_list:
#     squared_int = integer ** 2
#     squared_list.append(squared_int)
# print(squared_list)
# # step 7 
# dupes = []
# for integer in integers_list:
#     if integers_list.count(integer) > 1:
#         dupes.append(integer)
#         integers_list.remove(integer)
# print(len(dupes))
# # step 8 
# print(sum(integers_list) // len(integers_list))
# # step 9
# highest_value = 0 
# for integer in integers_list:
#     if integer > highest_value:
#         highest_value = integer
# print(highest_value)
# # you can also do print(max(integers_list))
# # step 10
# print(min(integers_list))
# # step 11
# num_sum = 0
# for integer in integers_list:
#     num_sum = integer + num_sum
# print(num_sum)
# print(num_sum // len(integers_list))
# lowest_value = 0
# for integer in integers_list:
#     if lowest_value > integer:
#         lowest_value = integer
#         print(integer)
# # step 12
# user_integers = 0
# count = 0
# while count < 10:
#     user_input = int(input("Please enter an integer between the values -100 and 100: "))
#     user_integers = user_input + user_integers
#     count += 1
# print(user_integers)
# # step 13
# random_integers = 0
# count = 0
# while count < 10:
#     random_num = random.randint(-100, 100)
#     print(random_num)
#     random_integers = random_num + random_integers
#     count += 1
# print(random_integers)
# step 14
# random_integers = 0
# count = 0
# while  count < 10:
#     unknown_amount_of_random_ints = (random.randint(50, sys.maxsize) for _ in range(random.randint(1, 10)))
#     print(unknown_amount_of_random_ints)
#     random_integers = unknown_amount_of_random_ints + random_integers
#     count += 1
# print(random_integers)
    
# Step 15 
# no it doesnt work it just keeps generating nonstop in and endless loop
#  ex: <generator object <genexpr> at 0x000001C4C77B1EE0>
# <generator object <genexpr> at 0x000001C4C77B1FC0>
# <generator object <genexpr> at 0x000001C4C77B1EE0>
# <generator object <genexpr> at 0x000001C4C77B1FC0>
# <generator object <genexpr> at 0x000001C4C77B1EE0>
# <generator object <genexpr> at 0x000001C4C77B1FC0>
# <generator object <genexpr> at 0x000001C4C77B1EE0>
# <generator object <genexpr> at 0x000001C4C77B1FC0>
# <generator object <genexpr> at 0x000001C4C77B1EE0>
# <generator object <genexpr> at 0x000001C4C77B1FC0>
 
# Exercise 3
# moon_paragraph = "The Moon is Earth’s only natural satellite and a constant companion in our journey through space. Positioned roughly 384,400 kilometers away, its gravitational pull drives the ocean tides on Earth and helps stabilize our planet's wobble, maintaining a steady climate. It is a world of stark beauty, covered in a fine grey dust called regolith and scarred by millions of craters left behind by asteroid impacts over billions of years. Because the Moon is tidally locked to Earth, it completes one rotation on its axis in the exact same time it takes to orbit our planet, meaning humanity always sees the same familiar face looking down from the night sky."
# character_count = len(moon_paragraph.replace(" ", ""))
# print(f"There are {character_count} characters in your paragraph")
# sentence_count = 0
# whitespace_count = 0
# for char in moon_paragraph:
#     if char == ".":
#         sentence_count += 1
#     if char == " ":
#         whitespace_count += 1
# print(f"There are {sentence_count} sentences in this paragraph")
# word_count = len(moon_paragraph.split())
# print(f"There are {word_count} words in this paragraph")
# words = moon_paragraph.split()
# unique_words = set(words)
# print(f"There are {len(unique_words)} unique words")
# print(f"There are {whitespace_count} spaces in this paragraph")
# avg_words_per_sentence = word_count / sentence_count
# print(f"The average amount of words per sentence is {avg_words_per_sentence}.")
# unique_words_2 = 0
# duplicate_words = word_count - len(unique_words)
# print(f"There are {duplicate_words} duplicate words in this paragraph")

# Exercise 4
# user_input = input("Please type in a sentence") to use later at the end
numbers = []
uppercase = []
lowercase = []
example_input = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
split_example_input = example_input.split()
for word in split_example_input:
    clean_word = word.strip("?.!,")
    if clean_word.isdigit():
        numbers.append(word)
    elif clean_word and clean_word[0].isupper():
        uppercase.append(word)
    else:
        lowercase.append(word)
numbers.sort()
uppercase.sort()
lowercase.sort()
ordered_list = numbers + uppercase + lowercase
for word in ordered_list:
    print(f"{word}:{split_example_input.count(word)}")
    
         
    



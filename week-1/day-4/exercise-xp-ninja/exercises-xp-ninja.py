import math
import random
# Exercise 1:
# Q = Square root of [(2 * C * D)/H]
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

# Exercise 2
# step 1
integers_list = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7, 7, 47]
# step 2
print(integers_list)
sorted_list = sorted(integers_list)
sorted_list.reverse()
print(sorted_list)
list_sum = sum(integers_list)
print(list_sum)
# step 3
first_last_list = integers_list[:1] + integers_list[-1:]
print(first_last_list)
# step 4
over_fifty = []
for integer in integers_list:
    if integer > 10:
        over_fifty.append(integer)
print(over_fifty)
# step 5
under_ten = []
for integer in integers_list:
    if integer < 50:
        under_ten.append(integer)
print(under_ten)
# step 6
squared_list = []
for integer in integers_list:
    squared_int = integer ** 2
    squared_list.append(squared_int)
print(squared_list)
# step 7 
dupes = []
for integer in integers_list:
    if integers_list.count(integer) > 1:
        dupes.append(integer)
        integers_list.remove(integer)
print(len(dupes))
# step 8 
print(sum(integers_list) // len(integers_list))
# step 9
highest_value = 0 
for integer in integers_list:
    if integer > highest_value:
        highest_value = integer
print(highest_value)
# you can also do print(max(integers_list))
# step 10
print(min(integers_list))
# step 11
num_sum = 0
for integer in integers_list:
    num_sum = integer + num_sum
print(num_sum)
print(num_sum // len(integers_list))
lowest_value = 0
for integer in integers_list:
    if lowest_value > integer:
        lowest_value = integer
        print(integer)
# step 12
user_integers = 0
count = 0
while count < 10:
    user_input = int(input("Please enter an integer between the values -100 and 100: "))
    user_integers = user_input + user_integers
    count += 1
print(user_integers)
# step 13
random_integers = 0
count = 0
while count < 10:
    random_num = random.randint(-100, 100)
    print(random_num)
    random_integers = random_num + random_integers
    count += 1
print(random_integers)
# step 14
import math
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
for int in integers_list:
    if int > 10:
        over_fifty.append(int)
print(over_fifty)
# step 5
under_ten = []
for int in integers_list:
    if int < 50:
        under_ten.append(int)
print(under_ten)
# step 6
squared_list = []
for int in integers_list:
    squared_int = int ** 2
    squared_list.append(squared_int)
print(squared_list)
# step 7 
dupes = []
for int in integers_list:
    if integers_list.count(int) > 1:
        dupes.append(int)
        integers_list.remove(int)
print(len(dupes))
# step 8 
print(sum(integers_list) // len(integers_list))
# step 9

       
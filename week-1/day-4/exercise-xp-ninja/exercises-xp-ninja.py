import math
# Exercise 1:
# Q = Square root of [(2 * C * D)/H]
c = int(50)
h = int(30)
result = []
user_input = input("Please enter 3 numbers seperated by commas: ")
print(user_input)
numbers = [int(num) for num in user_input.split(",")]
print(numbers)
for d in numbers:
    q = int(math.sqrt((2 * c * d) // h))
    result.append(q)
    continue
print(result)
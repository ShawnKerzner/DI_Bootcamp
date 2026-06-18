# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# print(sample_dict["class"]["student"]["marks"]["history"])

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }
# keys_to_remove = ["name", "salary"]

# del sample_dict["name"], sample_dict["salary"]
# print(sample_dict)

# my_books = {
#     "title": "Harry Potter",
#     "author": "JK Rowling"
# }

# for x, y in my_books.items():
#     print(f"the {x} is {y}")

# print(list(range(1, 10, 2)))

# for item in enumerate("abcd"):
#     print(item)

# for (index_count, letter) in enumerate('abcd'):
#     print('At index {} the letter is {}'.format(index_count, letter))

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# list3 = [1.1, 2.2, 3.3, 4.4, 5.5]
# for item in zip(list1, list2, list3):
#     print(type(item))

# for i in range(1, 3):
#     print(i)
# else:
#     print("The for loop is over")

# x = 0
# while x < 2:
#     print(f"x is {x}")
#     x += 1
# else:
#     print("x is bigger than 2")

# for letter in 'Leonardo':
#     if letter == 'a':
#         break
#     print(letter, end='')

# while True:
#     s = input("Enter something")
#     if s == "quit":
#         break
#     print('Length of the string is ', len(s))
# print("Done")

# for letter in "Leonardo":
#     if letter == "o":
#         continue
#     print(letter, end="")

# while True:
#     s = input("Enter Something")
#     if s == "quit":
#         break
#     if len(s) < 3:
#         print('Too small')
#         continue
#     print("Input is of sufficient length")

# for item in [1,2,3]:
#     pass
# print("Finish the script")

# my_number = '1234'
# my_list = []

# for num in my_number:
#     my_list.append(num)
# print(my_list)

# my_number = '1234'
# my_list = []
# my_list = [num for num in my_number]
# print(my_list)

# my_list = [x for x in range(0,6)]
# print(my_list)

# my_list = [x**2 for x in range(0,6)]
# print(my_list)

# my_list = [x for x in range(0,11) if x%2 == 0]
# print(my_list)

# my_list = []
# for i in [2, 3, 4]:
#     for j in [100, 200, 300]:
#         my_list.append(i*j)
# print(my_list)

# my_list = []
# my_list = [(i*j) for i in [2,3,4] for j in [100, 200, 300]]
# print(my_list)

family_age = {'Lea': 12, 'Mark': 25, 'George': 50}
new_year = 1
new_family_age = {name: age+new_year for (name, age) in family_age.items()}
print(new_family_age)
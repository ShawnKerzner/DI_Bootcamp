# participants = int(input("Enter the number of participants: "))
# participants_list = [i for i in range(1, participants + 1)]
# number_of_teams = participants // 3
# list_of_teams = []

# for number in range(1, 3 * number_of_teams, 3):
#     team = tuple(participants_list[number - 1: number + 2])
#     list_of_teams.append(team)
# print(list_of_teams)

dict = {"name": "shawn", "lastname": "kerzner", "age": 28,
        "program": "developers institute", "courses": ["Fullstack", "Gen AI", "Data Science"]}

# print(dictionary)
# print(dictionary["name"])
# print(dictionary.items())
# dict["name"] = "John"
# print(dictionary["name"])
dict['height'] = 180
print(tuple(dict.items()))
# print(dict.items())

# del dict['height']

# print(dict.items())

# print('height' in dict)

# for key in dict:
#     print(dict[key])
# print(dict.items())

# print(dict.keys())

# print(dict.values())

# print(list(range(10)))

# my_string = 'hello world'

# for i in range(len(my_string)):
#     print(my_string[i])

# for c in enumerate(my_string):
#     print(c)

# num = 0
# while num < 6:
#     num += 1
#     print(num)
#     # if num > 5:
#     #     break
# else:
#     print("oh no!")

# for name_name_name in range(5):
#     continue

# print("end")
# my_number = "1234"
# my_list = [int(num) for num in my_number]
# print(my_list)

# my_list2 = [num * 2 for num in range(2, 5)]
# print(my_list2)

# my_list3 = [num for num in range(10) if num % 2 == 1]
# print(my_list3)


my_list = [1, 2, 3]


def multiply_2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))
print(my_list)

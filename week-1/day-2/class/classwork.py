# def string_reverse():
#     user_string = input("Please enter a string: ")
#     reverse = ""
#     for char in user_string:
#         reverse = char + reverse
#     print(reverse)


# string_reverse()

# odd_nums = []
# for i in range(0, 22):
#     if i % 2 != 0:
#         odd_nums.append(i)
# print(odd_nums)

# odd_nums = [i for i in range(0, 22) if i % 2 != 0]
# print(odd_nums)

user_list = []
length = int(input("How long would you like your list to be? "))
while length > len(user_list):
    list_entry = (input("Please enter a number: "))
    if not list_entry.isdigit():
        print("Must be a number")
    else:
        user_list.append(list_entry)
print(user_list)

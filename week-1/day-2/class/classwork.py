def string_reverse():
    user_string = input("Please enter a string: ")
    reverse = ""
    for char in user_string:
        reverse = char + reverse
    print(reverse)


string_reverse()

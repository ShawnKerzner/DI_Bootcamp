def find_2():
    user_input = input("Please type a string: ")
    counter = 0
    if len(user_input) < 1:
        raise ValueError("String can not be empty")

    for char in user_input:
        if char == "2":
            counter += 1
    sum_of_counters = counter * int(char)
    print(sum_of_counters)
    return sum_of_counters


find_2()

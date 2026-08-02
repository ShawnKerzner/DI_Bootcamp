import random


def build_up_a_string():
    user_input = input("Type a string: ")
    if len(user_input) < 10:
        print("String not long enough")
    elif len(user_input) > 10:
        print("String too long.")
    else:
        print("Perfect string")
    print(user_input[0], user_input[-1])
    characters = []
    for char in user_input:
        characters.append(char)
        result = " ".join(characters)
        print(result)
    input_to_list = list(user_input)
    random.shuffle(input_to_list)
    shuffled_text = "".join(input_to_list)
    print(shuffled_text)


build_up_a_string()

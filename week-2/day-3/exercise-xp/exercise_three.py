import random
import string


def ran_str_gen():
    random_string = ""
    for i in range(5):
        random_char = random.choice(string.ascii_letters)
        random_string = random_string + random_char
    return random_string


ran_str_gen()

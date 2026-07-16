# # Exercise 1
# def get_full_name(first_name, last_name, middle_name=None):
#     if middle_name == None:
#         print(f"{first_name} {last_name}")
#         return first_name + " " + last_name
#     else:
#         print(f"{first_name} {middle_name} {last_name}")
#     return first_name + " " + middle_name + " " + last_name


# get_full_name(first_name="Chaim", middle_name="Shmuel", last_name="Kerzner")
# get_full_name(first_name="Shawn", last_name="Kerzner")

# Exercise 2
def english_to_morse(english_string):
    morse_dict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...",
                  "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", " ": "/"}
    morse_conv = []
    lower_english_string = english_string.lower()
    for char in lower_english_string:
        morse_conv.append(morse_dict[char])
    morse_string = " ".join(morse_conv)
    print(morse_string)
    return (morse_string)


english_to_morse("Lets see if this function actually works")

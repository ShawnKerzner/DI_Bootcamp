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
    if english_string == "":
        raise ValueError(
            "The variable english_string needs to contain an actual string with characters")
    elif not isinstance(english_string, str):
        raise TypeError(
            "The variable 'english_string' needs to be an actual string")
    else:
        lower_english_string = english_string.lower()
        for char in lower_english_string:
            if char in morse_dict:
                morse_conv.append(morse_dict[char])
        morse_string = " ".join(morse_conv)
        print(morse_string)
        return (morse_string)


# english_to_morse("Lets see if this function actually works")


def morse_to_english(morse_string):
    if not isinstance(morse_string, str):
        raise TypeError("Input needs to be a string")
    if morse_string == "":
        raise ValueError(
            "The variable morse_string needs to contain an actual string with characters")
    morse_characters = (".", "-", "/", " ")
    for char in morse_string:
        if char not in morse_characters:
            raise ValueError(
                "Input needs to made up of actual morse code characters")
    english_dict = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's',
                    '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '/': ' '}
    english_list = []
    morse_list = morse_string.split("/")
    for item in morse_list:
        english_letters = []
        word_to_letter = item.split()
        for letter in word_to_letter:
            if letter in english_dict:
                english_letters.append(english_dict[letter])
        english_word = "".join(english_letters)
        english_list.append(english_word)
        english_string = " ".join(english_list)
    print(english_string)
    return english_string


# morse_to_english(
    # ".-.. . - ... / ... . . / .. ..-. / - .... .. ... / .-. . .- .-.. .-.. -.-- / .-- --- .-. -.- ...")

morse_to_english(".- zzzz -...")

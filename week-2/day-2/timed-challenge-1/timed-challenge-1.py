def character_counter():
    string = input("Enter a string: ")
    while True:
        character = input("enter a character: ")
        if len(character) > 1:
            print("Error: Character should be a single letter or number")
        else:
            break
    character_count = string.count(character)
    print(
        f"The character {character} is found {character_count} times in the string '{string}'")
    return character_count


character_counter()

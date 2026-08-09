import random


def dog():
    dog_name = input("Dog name: ")
    print(f"Your dog's name is {dog_name}")
    action = random.randint(1, 3)
    running = True
    while running:
        if action == 1:
            print(f"{dog_name} is sleeping")
        elif action == 2:
            print(f"{dog_name} is eating")
        else:
            print(f"{dog_name} is barking")
        quit = input("Would you like to continue y/n? ")
        if quit == 'n':
            continue
        elif quit == 'y':
            break


dog()

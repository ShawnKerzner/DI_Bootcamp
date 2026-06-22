def calculation(a, b):
    return a + b, a - b

print(calculation(5, 6))
print(calculation(10, 5))

def say_hello(username):
    print("Hello "+username)

say_hello("Rick") # "Rick" is an argument
# output "Hello Rick"

say_hello("Morty") # "Morty" is an argument
# output "Hello Morty"

def say_hello(username, language):
    if language == "EN":
        print("Hello "+username)
    elif language == "FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)

say_hello("Rick", "EN")
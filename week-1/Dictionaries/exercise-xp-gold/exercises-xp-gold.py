# Exercise 1
birthdays = {
    "shawn": "1998/06/23",
    "ari": "1992/01/10",
    "aaron": "1997/07/22",
    "daniel": "1999/10/26",
    "mom": "1963/05/11"
}

print("Hello! Use this script to look up birthdays!!!")
user_input = input("Please enter the name of someone's birthday you would like to look up: ")

for name, date in birthdays.items():
    if user_input == name :
        print(f"{name}: {date}")


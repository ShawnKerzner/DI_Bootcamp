from datetime import datetime

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

# Exercise 2 and 3

birthdays = {
    "shawn": "1998/06/23",
    "ari": "1992/01/10",
    "aaron": "1997/07/22",
    "daniel": "1999/10/26",
    "mom": "1963/05/11"
}

while True:   
    new_birthday = input("Please enter your birthday in the using the following format YYYY/MM/DD: ").strip()

    try:
        parsed_date = datetime.strptime(new_birthday, "%Y/%m/%d")
        today = datetime.now()
        if parsed_date > today:
            print("Error: You cannot enter a date in the future. Try again. \n")
        else:
            break
    except ValueError:
        print("Error: Invalid format or date. Please use YYYY/MM/DD")


while True:
    new_name = input("Whose birthday is it?: ").strip().lower()
    if new_name == "":
        print("Error: Name cannot be blank. Please try again \n")
    else:
        break

birthdays[new_name] = new_birthday
print(birthdays)

print(f"current users: {birthdays.keys()}")
user_search = input("Please enter the name of the user you would like to look up: ").lower()
found_match = False
for name, date in birthdays.items():
    if user_search in name :
        print(f"{name}: {date}")
        found_match = True
        break
if found_match == False:
    print(f"Sorry we don't have the birthday information for {user_search}")

# Exercise 4
# Theres no way this is the challenge. I must be misunderstanding what they want from me in the instructions
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print(f"here is our inventory and their prices. {items}")


items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

grand_total = sum(data["price"] * data["stock"] for data in items.values())
print(grand_total)
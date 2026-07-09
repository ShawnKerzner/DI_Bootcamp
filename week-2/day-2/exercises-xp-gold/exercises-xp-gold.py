import random
# # Exercise 1

# def get_age(year, month, day):
#     current_year = 2026
#     current_month = 7
#     current_day = int(input("Enter the day of the month: "))
#     if current_day < day:
#         current_month -= 1
#     if current_month < month:
#         current_year -= 1
#     age = current_year - year
#     return age


# def can_retire(date_of_birth, gender):

#     year, month, day = date_of_birth.split("/")
#     age = get_age(int(year), int(month), int(day))

#     if gender == "m":
#         age_of_retirement = 67
#     if gender == "f":
#         age_of_retirement = 62

#     if age >= age_of_retirement:
#         print("You can retire")
#     else:
#         print("You can't retire")


# can_retire("1959/06/23", "m")
# can_retire("1965/06/23", "f")

# Exercise 3
def throw_dice():
    result = random.randint(1, 6)
    print(f"Dice rolled a {result}")
    return result


def throw_until_double():
    attempts = 0
    while True:
        throw_1 = throw_dice()
        throw_2 = throw_dice()
        print(f"pair: {throw_1}, {throw_2}")
        if throw_1 != throw_2:
            attempts += 1
            continue
        else:
            print(
                f"Doubles! pair: {throw_1}, {throw_2} Number of attempts: {attempts}")
            break
    # print(f"Number of attempts: {attempts}")


# calls the throw dice function
# saves result as var1
# calls the throw dice function again
# saves result as var 2
# if var1 =! var2
# attempts += 1
# var1 = var2
# continue call to keep running the loop
# else print string doubles , both values, and attempts
throw_until_double()

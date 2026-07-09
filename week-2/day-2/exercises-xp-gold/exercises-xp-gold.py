import datetime
# Exercise 1


def get_age(year, month, day):
    current_year = 2026
    current_month = 7
    current_day = int(input("Enter the day of the month"))
    age_year = current_year - year
    if current_day < day:
        current_month -= 1
    if current_month < month:
        current_year -= 1
    age = current_year - year
    return age


print(get_age(1998, 6, 23))


def can_retire(gender, date_of_birth):
    date_of_birth.split("/")
    print(date_of_birth)
# comment out function to test if date of birth split works
# goal is to seperate the date of birth and divide it into 3 seperate variables

#     if gender == "male":
#         retirment_age = 67
#         if get_age(date_of_birth.split("/")) >= retirment_age:
#             print("Congrats you can retire")
#         else:
#             print("Sorry you are not ready to retire")
#     else:
#         gender == "female"
#         retirment_age = 62
#         if get_age(date_of_birth.split("/")) >= retirment_age:
#             print("Congrats you can retire")
#         else:
#             print("Sorry you are not ready to retire")


# print(can_retire("male", "1993/09/21"))

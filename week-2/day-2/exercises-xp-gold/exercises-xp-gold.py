
# Exercise 1

def get_age(year, month, day):
    current_year = 2026
    current_month = 7
    current_day = int(input("Enter the day of the month: "))
    if current_day < day:
        current_month -= 1
    if current_month < month:
        current_year -= 1
    age = current_year - year
    return age


def can_retire(date_of_birth, gender):

    year, month, day = date_of_birth.split("/")
    age = get_age(int(year), int(month), int(day))

    if gender == "m":
        age_of_retirement = 67
    if gender == "f":
        age_of_retirement = 62

    if age >= age_of_retirement:
        print("You can retire")
    else:
        print("You can't retire")


can_retire("1959/06/23", "m")
can_retire("1965/06/23", "f")

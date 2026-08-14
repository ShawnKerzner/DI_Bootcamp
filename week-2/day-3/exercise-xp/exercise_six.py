from datetime import datetime


def how_many_minutes_have_you_lived(birthday):
    birthday_formated = datetime.strptime(birthday, "%d/%m/%Y")
    current = datetime.now()
    difference = current - birthday_formated
    seconds = difference.total_seconds()
    minutes = seconds // 60
    return minutes


print(how_many_minutes_have_you_lived("15/1/1998"))

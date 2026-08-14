from datetime import datetime

current = datetime.now()

print(current)

next_year = current.year + 1
print(next_year)
jan_1st = datetime(next_year, 1, 1)

difference = jan_1st - current
print(difference)

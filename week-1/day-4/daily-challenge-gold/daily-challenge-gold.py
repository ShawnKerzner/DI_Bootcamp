# step 1: implement date time to turn dates into integers

# step 2: subtract the current date from the birthdate to find the age. 
# if the birthdate(month/day) is less than the current date(month/day) subtract one from the age

# Step 3: seperate the last number from the age using age % 0.

# Step 4: determine if birthyear is a leap year
#  if (birthyear % 4 == 0 and not birthyear % 100 == 0) or birthyear % 400 == 0
from datetime import datetime

current_date = datetime.now()
current_date_str = current_date.strftime("%d/%m/%Y")
user_birthdate = input("Please enter your the date you were born. DD/MM/YYYY: ")
user_birthdate_str = datetime.strptime(user_birthdate,"%d/%m/%Y" )
potential_age = current_date.year - user_birthdate_str.year
if (current_date.month, current_date.day) < (user_birthdate_str.month, user_birthdate_str.day):
    potential_age -= 1
candles = potential_age % 10
print(f'___{"i" * candles}___'.center(19))
print('|:H:a:p:p:y:|'.center(19))
print('__|___________|__'.center(19))
print('|^^^^^^^^^^^^^^^^^|'.center(19))
print('|:B:i:r:t:h:d:a:y:|'.center(19))
print('|                 |'.center(19))
print('~~~~~~~~~~~~~~~~~~~'.center(19))
    
if (user_birthdate_str.year % 4 == 0 and not user_birthdate_str.year % 100 == 0) or user_birthdate_str.year % 400 == 0:
    print(f'___{"i" * candles}___'.center(19))
    print('|:H:a:p:p:y:|'.center(19))
    print('__|___________|__'.center(19))
    print('|^^^^^^^^^^^^^^^^^|'.center(19))
    print('|:B:i:r:t:h:d:a:y:|'.center(19))
    print('|                 |'.center(19))
    print('~~~~~~~~~~~~~~~~~~~'.center(19))


# Exercise 1
my_fav_numbers = {18, 732, 2018}
my_fav_numbers.update([2016, 845])
print(my_fav_numbers)
items_to_remove = [2016, 845]
my_fav_numbers.difference_update(items_to_remove)
print(my_fav_numbers)
friend_fav_numbers = {1, 60, 23}
power_of_friendship = my_fav_numbers.union(friend_fav_numbers)
print(power_of_friendship)

# Exercise 2
my_tuple = (1, 2, 3 ,4)
# my_tuple[4] = 8

# Exercise 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0,"Apples")
print(basket)
print(basket.count("Apples"))
basket.clear()
print(basket)


# Exercise 4
float_list = [1.5 + (i * 0.5) for i in range(8)]
mixed_list = []
for num in float_list:
    if num % 1 == 0:
        mixed_list.append(int(num))
    else:
        mixed_list.append(num)
print(mixed_list)

# Exercise 5
for i in range(1, 21):
    print(i)

for i in range(1, 20 + 1):
    if i % 2 == 0:
        print(i)

#Exercise 6

user_input = input("Please enter your name: ")
while True:
    if len(user_input) < 3 or user_input.isdigit():
        print("Retry")
        user_input = input("Please enter your name: ")
    else:
        print("Thank you")
        break

# Exercise 7:
fav_fruits = input("Please enter your favorite fruits seperated by space: ")
fav_fruit_list = fav_fruits.split()
user_input = input("Please enter a fruit")
for fruit in fav_fruit_list:
    if fruit == user_input:
        print("You chose one of your favorite fruits! Enjoy!")
    else:
        print("You chose a new fruit. I hope you enjoy it!")



        




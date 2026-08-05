# Exercise 1
dictionary1 = {}
dictionary2 = {}
user_input = input("Please enter a word: ")
for index, char in enumerate(user_input):
    if char not in dictionary1:
        dictionary1[char] = [index]
    else:
        dictionary1[char].append(index)
print(dictionary1)

for char in user_input:
    if char in dictionary2:
        dictionary2[char] += 1
    else:
        dictionary2[char] = 1
print(dictionary2)

# Exercise 2
items_purchase = {"Water": "$1", "Bread": "$3",
                  "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14",
                  "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet = "$100"

items_purchase = {"Phone": "$999", "Speakers": "$300",
                  "Laptop": "$5,000", "PC": "$1200"}
wallet = "$1"

basket = []

for key, value in items_purchase.items():
    new_value = value.replace("$", "")
    new_value = new_value.replace(",", "")
    items_purchase[key] = int(new_value)
print(items_purchase)

new_wallet = wallet.replace("$", "")
new_wallet = new_wallet.replace("$", "")
new_wallet = int(new_wallet)
print(new_wallet)

for key, value in items_purchase.items():
    if new_wallet >= value:
        new_wallet -= value
        basket.append(key)
if basket == []:
    print("Nothing")
else:
    print(
        f"The following items are in your basket {sorted(basket)} and you have ${new_wallet} left over")

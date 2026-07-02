# # Exercise 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# result = dict(zip(keys, values))
# print(result)

# # Execise 2
# total_cost = 0
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# for key, value in family.items():
#     if value < 3:
#         print(f"{key}'s ticket is free")
#     elif value > 3 and value < 12:
#         total_cost += 10
#         print(f"{key}'s ticket costs $10")
#     elif value >= 12:
#         total_cost += 15
#         print(f"{key}'s ticket costs $15")
# print(f"The total cost is ${total_cost}")
# #  Exercise 2 Bonus
# family = {}
# total_cost = 0
# number_of_entries = int(input("Number of movie tickets: "))
# family = {input("Name: "): int(input("Age: ")) for _ in range(number_of_entries)}
# for key, value in family.items():
#     if value < 3:
#         print(f"{key}'s ticket is free")
#     elif value > 3 and value < 12:
#         total_cost += 10
#         print(f"{key}'s ticket costs $10")
#     elif value >= 12:
#         total_cost += 15
#         print(f"{key}'s ticket costs $15")
# print(f"The total cost is ${total_cost}")

# Exercise 3
brand = {
    "name": "zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": "men, women, children, home",
    "international_competitors": "Gap, H&M, Benetton",
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": "pink, green"
    }
}

brand["number_stores"] = 2
print("number_stores:", brand["number_stores"])

print(f"Zara's clients like styles for {brand['type_of_clothes']}.")



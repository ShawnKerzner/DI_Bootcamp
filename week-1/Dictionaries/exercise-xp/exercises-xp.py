# Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = dict(zip(keys, values))
print(result)

# Execise 2
total_cost = 0
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for key, value in family.items():
    if value < 3:
        print(f"{key}'s ticket is free")
    elif value > 3 and value < 12:
        total_cost += 10
        print(f"{key}'s ticket costs $10")
    elif value >= 12:
        total_cost += 15
        print(f"{key}'s ticket costs $15")
print(f"The total cost is ${total_cost}")
    
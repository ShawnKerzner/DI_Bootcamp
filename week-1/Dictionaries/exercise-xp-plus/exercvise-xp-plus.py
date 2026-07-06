# # Exercise 1
# student_grades = {
#     "Alice": [88, 92, 100],
#     "Bob": [75, 78, 80],
#     "Charlie": [92, 90, 85],
#     "Dana": [83, 88, 92],
#     "Eli": [78, 80, 72]
# }
# student_averages = {}

# student_letter_grades = {}

# for name, grade in student_grades.items():
#     student_average = sum(grade) // len(grade)
#     student_averages[name] = student_average

# for name, average in student_averages.items():
#     if average >= 90:
#         student_letter_grades[name] = "A"
#     elif average >= 80 and average <=89:
#         student_letter_grades[name] = "B"
#     elif average >= 70 and average <=79:
#         student_letter_grades[name] = "C"
#     elif average >= 60 and average <=69:
#         student_letter_grades[name] = "D"
#     else:
#         student_letter_grades[name] = "F"

# class_average = sum(student_averages.values()) // len(student_averages.keys())
# print(f"The class has an average of {class_average}")

# for name in student_grades:
#     average = student_averages[name]
#     grade = student_letter_grades[name]
#     print(f"Student: {name}, Average: {average}, Grade: {grade}")

# Exercise 2

sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

total_sales = {}

for dict in sales_data:
    current_product = dict["product"]
    total_revenue = dict["price"] * dict["quantity"]
    if current_product not in total_sales:
        total_sales[current_product] = total_revenue
    else:
        total_sales[current_product] += total_revenue
print(f"total_sales {total_sales}")
        
customer_spending_profile = {}
for dict in sales_data:
    current_customer = dict["customer_id"]
    total_spend = dict["price"] * dict["quantity"]
    if current_customer not in customer_spending_profile:
        customer_spending_profile[current_customer] = total_spend
    else:
        customer_spending_profile[current_customer] += total_spend
print(f"customer_spending_profile {customer_spending_profile}")

for dict in sales_data:
    dict["total_price"] = dict["price"] * dict["quantity"]
    print(f"total price for the transaction is {dict["total_price"]}")

high_value_sales = [dict for dict in sales_data if dict["total_price"] > 500]
high_value_sales.sort(key=lambda dict: dict["total_price"], reverse=True)
print(f"high value sales from highest to lowest: {high_value_sales}")

purchase_counts = {}
for dict in sales_data:
    current_customer = dict["customer_id"]
    if current_customer not in purchase_counts:
        purchase_counts[current_customer] = 1
    else:
        purchase_counts[current_customer] += 1
print(f"customer counter: {purchase_counts}")

category_counts = {}
for dict in sales_data:
    current_product = dict["product"]
    if current_product not in category_counts:
        category_counts[current_product] = 1
    else:
        category_counts[current_product] += 1
print(f"purchases per category {category_counts}")

for item in category_counts:
    average_rev_per_category = total_sales[item] // category_counts[item]
    print(average_rev_per_category)

product_quantities = {}
for dict in sales_data:
    current_product = dict["product"]
    current_quantity = dict["quantity"]
    if current_product not in product_quantities:
        product_quantities[current_product] = current_quantity
    else:
        product_quantities[current_product] += current_quantity

most_popular_product = max(product_quantities, key=lambda prod: product_quantities[prod])
print(most_popular_product)

print("--- 5. BUSINESS & MARKETING STRATEGIES ---")

print("""
[STRATEGY 1: The 'High-Volume Hook' (Headphones)]
- Insight: Headphones are the most popular item by volume (6 units), but bring in a lower price point.
- Strategy: Use Headphones as a digital ad hook to drive traffic. Implement website cross-selling pop-ups 
            prompting headphone buyers to look at premium items like Smartphones before checking out.
""")

print("""
[STRATEGY 2: The 'Bundle Boost' (Smartphones & Laptops)]
- Insight: Big-ticket items have high margins but lower purchase frequency.
- Strategy: Create a 'Tech Essentials Bundle' (e.g., 'Buy a Smartphone or Laptop, get 30% off Headphones'). 
            This uses your high-volume item to increase the average order value of big purchases.
""")

print("""
[STRATEGY 3: VIP Loyalty Targeting]
- Insight: Customer 1 is a frequent high-value spender, while Customer 3 buys high volume at lower costs.
- Strategy: Automatically segment your email lists. Send Customer 1 exclusive early access to premium tech 
            launches. Send Customer 3 volume-based promotions like 'Buy 2 accessories, get 1 free.'
""")
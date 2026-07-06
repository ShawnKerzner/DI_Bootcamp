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
print(total_sales)
        
customer_spending_profile = {}
for dict in sales_data:
    current_customer = dict["customer_id"]
    total_spend = dict["price"] * dict["quantity"]
    if current_customer not in customer_spending_profile:
        customer_spending_profile[current_customer] = total_spend
    else:
        customer_spending_profile[current_customer] += total_spend
print(customer_spending_profile)

for dict in sales_data:
    dict["total_price"] = dict["price"] * dict["quantity"]
print(sales_data)
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}
student_averages = {}

student_letter_grades = {}

for name, grade in student_grades.items():
    student_average = sum(grade) // len(grade)
    student_averages[name] = student_average

for name, average in student_averages.items():
    if average >= 90:
        student_letter_grades[name] = "A"
    elif average >= 80 and average <=89:
        student_letter_grades[name] = "B"
    elif average >= 70 and average <=79:
        student_letter_grades[name] = "C"
    elif average >= 60 and average <=69:
        student_letter_grades[name] = "D"
    else:
        student_letter_grades[name] = "F"

class_average = sum(student_averages.values()) // len(student_averages.keys())
print(f"The class has an average of {class_average}")

for name in student_grades:
    average = student_averages[name]
    grade = student_letter_grades[name]
    print(f"Student: {name}, Average: {average}, Grade: {grade}")
class Person():
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def hello(self):
        return f"Hello I am {self.name}"


class Student(Person):
    def __init__(self, name, program):
        self.name = name
        self.program = program


student_name = input("name: ")
program = ""
my_student = Student(student_name, program)

print(f"{my_student.hello()}")

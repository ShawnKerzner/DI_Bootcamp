# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"


# print(greet("Student"))
# print(greet("Shawn", "Goodmorning"))


# def find_sum(*args):
#     return sum(args)


# print(find_sum(1, 2, 10, -20, 25))
# print(find_sum(-1, 23, 170, -20))

a = 5
print(a)


def my_func(x):
    x = 10


my_func(a)
print(a)

b = [1, 3, 5]


def func2(my_list):
    my_list[1] = -10
    return


func2(b)
print(b)

my_list = [1, 2, 5, 11, 78]


def my_map_function(my_map_list_item):
    return my_map_list_item + 10


map_object = map(my_map_function, my_list)
print(list(map_object))

my_string = "Hello World"


def reverse_case(word):
    for char in word:
        if char.isupper():
            return char.lower()
        else:
            return char.upper()


map_string = map(reverse_case, my_string)
back_to_string = "".join(map_string)
print(back_to_string)

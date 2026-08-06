from functools import reduce

my_list = [1, 2, 5]


def my_function(e):
    return e * e


print(list(map(my_function, my_list)))


def my_filter_function(e):
    return e % 2 == 1


print(list(filter(my_filter_function, my_list)))


def my_reduce_function(a, b):
    return a - b


print(reduce(my_reduce_function, my_list))

result = my_list[0]
for i in range(1, len(my_list)):
    result -= my_list[1]

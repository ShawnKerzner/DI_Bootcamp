def upper_string(s):
    return s.upper()

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(upper_string, fruit)

print(list(map_object))

#  ['APPLE', 'BANANA', 'PEAR', 'APRICOT', 'ORANGE']

def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filtered_object = filter(starts_with_A, fruit)

print(list(filtered_object))
# ['Apple', 'Apricot']

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

filtered_list = filter(lambda name: len(name)  <=4, people)
def say_hello(name):
    return(f"hello {name}")
map_list = map(say_hello, filtered_list)
print(list(map_list))
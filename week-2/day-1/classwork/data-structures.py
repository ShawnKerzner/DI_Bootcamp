# cubes = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
# print(cubes.pop(4))
# print(cubes)
# print(cubes.popitem())
# print(cubes)
# cubes.clear()
# print(cubes)

# d = {1:'10', 2:'20', 3:'30', 4:'40', 5:'50'}
# l1 =list(d.keys())
# print("the key values are:")
# print(l1)
# l2 = list(d.values())
# print("The values are of dictionary is")
# print(l2)
# l3 = list(d.items())
# print("the list items are")
# print(l3)

# set1 = {1, 2, 3, 4, "hi", "world", "python"}
# print("python" in set1)
# set1.remove(4)
# print(set1)

a = {1, 2, 3, 4, 5}
b = {2, 3, 6, 7, 5}
c = a^b 
print(c)
d = a - b
print(d)
e = b - a 
print(e)
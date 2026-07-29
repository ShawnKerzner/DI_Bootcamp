x = int(input("Enter a number: "))

divisble_nums = []

for i in range(1, x):
    if x % i == 0:
        divisble_nums.append(i)

if sum(divisble_nums) == x:
    print(True)
else:
    print(False)

# Time remaining 26:33
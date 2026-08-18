
num = int(input("Enter a number between 1 and 10: "))
total = 1
for i in range(2, num + 1):
    total *= i

with open("result.txt", "w") as f:
    f.write("My result is: " + str(total))
# try:
#     f = open("result.txt", "w")
#     f.write("My result is : " + str(total))
# finally:
#     f.close()

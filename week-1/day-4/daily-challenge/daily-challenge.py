# Daily Challenge: 1

number = int(input("Please enter a number: "))
length = int(input("Please enter a second number: "))
multiples = [number * i for i in range(1, length + 1)]
print(multiples)


# Daily Challenge: 2
string = input("Please enter a word with repeating letters: ")
result = ""
for char in string:
   if not result or char != result[-1]:
      result += char
print(result)
    



print("Before the loop")

while True:
    value = input("Enter a number 0-2: ")
    if value not in ("0", "1", "2"):
        raise ValueError("Bad input!")
    else:
        print("You entered a valid value:", value)
        break

print("After the loop - did we get here?")

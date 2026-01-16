# Program to compare two lists using == and is operators

num1 = [2, 3, 4, 5]
num2 = [2, 3, 4, 5]

# Using == operator (checks values)
if num1 == num2:
    print("num1 and num2 have same values (==)")
else:
    print("num1 and num2 have different values (==)")

# Using is operator (checks memory location)
if num1 is num2:
    print("num1 and num2 refer to the same object (is)")
else:
    print("num1 and num2 refer to different objects (is)")

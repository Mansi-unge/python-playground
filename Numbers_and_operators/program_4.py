# Write a Python program to:
# Swap two numbers without using a third variable

a = 2
b = 3

print("Numbers Before Swapping is a = ",a," and b = ", b)

a = a + b 
b = a - b
a = a - b

print("Numbers After Swapping is a = ",a," and b = ", b)
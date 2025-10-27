"""
Concept: 
Recognizing built-in data types
Question: 
Write a Python program that takes user input and prints its data type.
Steps:
1.Take input using input().
2.Use type() function.
3.Print the result.
"""

d_1 = (input("enter any value : "))
print(type(d_1))

"""
output: enter any value : 20
<class 'str'>

always returns as str. because input always takes every value as string
"""
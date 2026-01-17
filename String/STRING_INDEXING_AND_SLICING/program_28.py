# Write a program to extract first half and second half of a string.

string = "I am extracting the first half and second half of a string seperately"
print("original string")
print(string)

middle_index = len(string)//2
first_half = string[0:middle_index]
second_half = string[middle_index:]
print("first half of the string is :",first_half)
print("Second half of the string is :",second_half)
# Write a program to compare two strings.

str1 = "mansi"
str2 = "mansi"


# comparing the values
print("comapring by == operator for checking values")
if str1 == str2:
  print("Both the strings are equal")
else:
  print("Both the strings are diffrent")

# comparing the memory locations
print("comapring by is operator for checking memory location")
if str1 is str2:
  print("both strings have same memory location")
else:
  print("both strings have diffrent memory location")
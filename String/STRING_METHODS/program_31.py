# Write a program to count the number of vowels in a string.

vowels = ["a","e","i","o","u"]
string = "Finding the vowels in a string"

count = 0
for char in string.lower():
  if char in vowels:
    count = count + 1

print("Number of vowels in string are : ",count)
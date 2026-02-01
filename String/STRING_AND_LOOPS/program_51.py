# Write a program to remove duplicate characters from a string.

my_string = "frequency"
result = ""
for char in my_string:
  if char not in result:
    result += char

print(result)
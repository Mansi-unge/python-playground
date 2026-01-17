# Write a program to count uppercase and lowercase letters in a string.

string = "To Count The UPPERCASE And lowercase Letters In A String"

count_upper = 0
count_lower = 0
for i in string:
  if i.isupper():
    count_upper = count_upper + 1
  elif i.islower():
    count_lower = count_lower + 1

print("characters in string that are in uppercase are : ",count_upper)
print("characters in string that are in lowercase are : ",count_lower)
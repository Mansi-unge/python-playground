# Write a program to check whether a string is a palindrome.

string = "mansi"
string2 = string[::-1]

if string == string2:
  print("string is palindrome")
else:
  print("string is not palindrome")
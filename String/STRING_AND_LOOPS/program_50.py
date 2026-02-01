# Write a program to find the frequency of each character in a string.

my_string = "frequency"



for char in my_string:
  freq = 0
  for ch in my_string:
    if ch == char:
      freq += 1
  print(char , " : " , freq)  


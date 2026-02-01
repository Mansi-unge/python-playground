# Write a program to check whether two strings are anagrams.

word_1 = "listen  "
word_2 = "silent"

if sorted(word_1) == sorted(word_2):
  print("the given strings are anagrams")
else:
  print("given strings are not anagrams")
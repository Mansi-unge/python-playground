# Write a program to find the longest word in a sentence.

sentence = "program to find the longest word in a sentence."


words = sentence.split()
print(words)

longest_word = words[0]

for word in words:
  if len(word) > len(longest_word):
    longest_word = word

print("longest word : ",longest_word)
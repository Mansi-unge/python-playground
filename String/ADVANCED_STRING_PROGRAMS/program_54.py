# Write a program to compress a string
# Example: aaabb → a3b2

string = "aaabbbbb"
compressed = ""
count = 1

for i in range(1,len(string)):
  if string[i] == string[i-1]:
    count+=1
  else:
    compressed += string[i-1]+str(count)
    count = 1
compressed += string[i-1]+str(count)
print("string compressed is : ",compressed)
  
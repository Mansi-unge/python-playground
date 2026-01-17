# Write a program to check whether a string starts with a given prefix and ends with a given suffix.

string = "Write a program to check whether a string starts with a given prefix and ends with a given suffix"

prefix = "Write"
suffix = "suffix"

prefix_string = string.startswith(prefix)
print("prefix of the string is : ",prefix_string)

suffix_string = string.endswith(suffix)
print("suffix of the string is : ",suffix_string)

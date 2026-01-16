# Program to show that strings are immutable in Python
# Immutable means: once a string is created, its value cannot be changed

# Assign a string to the variable 'name'
name = "mansi"

# Print the original string
print(name)

# Print the memory address (id) of the original string
# This shows where the string is stored in memory
print("id of original string:", id(name))

# Modify the string by concatenating another word
# This does NOT change the original string
# Instead, Python creates a NEW string object
name = name + " unge"

# Print the modified string
print(name)

# Print the memory address (id) of the new string
# The id will be different, proving strings are immutable
print("id of changed string:", id(name))

"""
Concept: Combining lists and dicts
Question:
Make a list of dictionaries representing 2 students:
[
  {'name': 'Mansi', 'marks': 85},
  {'name': 'Riya', 'marks': 90}
]
Print the name of student with highest marks.

Steps:
Use max() with key = lambda d: d['marks']

Output:
Riya
"""

# CODE :

li = [
  {'name': 'Mansi', 'marks': 85},
  {'name': 'Riya', 'marks': 90}
]

topper = max(li, key=lambda d: d['marks'])
print("topper of class is :",topper['name'])

"""
OUTPUT:
topper of class is : Riya
"""
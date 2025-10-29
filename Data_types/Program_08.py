"""
Concept: Key-value mapping

Question:
Create dictionary:
student = {'name': 'Mansi', 'age': 20, 'marks': 85}
Print all keys, values, and items.

Steps:
Use .keys(), .values(), .items()

Output:
dict_keys(['name','age','marks'])
dict_values(['Mansi',20,85])
dict_items([('name','Mansi'),('age',20),('marks',85)])
"""

# CODE :

#dictionary of student data  
student = {
  'name':'mansi' ,
  'age' : '22' ,
  'marks' : '85'
}

# getting keys in dictionary
dict_keys = student.keys()
print("keys in student dictionary are :", dict_keys)

# getting values in dictionary 
dict_values = student.values()
print("values in student dictionary are :", dict_values)

# getting the dictionary items 
dict_items = student.items()
print("items in student dictionary are :",dict_items)


"""
OUTPUT :
keys in student dictionary are : dict_keys(['name', 'age', 'marks'])
values in student dictionary are : dict_values(['mansi', '22', '85'])
items in student dictionary are : dict_items([('name', 'mansi'), ('age', '22'), ('marks', '85')])
"""

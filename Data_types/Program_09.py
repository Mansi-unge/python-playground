"""
Concept: Unique values, union & intersection

Question:
s1 = {1,2,3} and s2 = {3,4,5}
Find union and intersection.

Steps:
Use s1 | s2, s1 & s2

Output:
{1,2,3,4,5}
{3}
"""

# CODE :

#set 
s1 = {1,2,3}        #set 1
s2 = {3,4,5}        #set 2

# finfing the union between both sets s1 & s2
union_of_sets = s1 | s2
print("union of set 1 and set 2 is :",union_of_sets)

# finding intersection between both sets s1 and s2
intersection_of_sets = s1 & s2
print("intersection of set 1 and set 2 is :", intersection_of_sets)


"""
OUTPUT :
union of set 1 and set 2 is : {1, 2, 3, 4, 5}
intersection of set 1 and set 2 is : {3}
"""
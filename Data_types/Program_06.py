"""
Concept: List methods
Question:
Start with nums = [1,2,3].
Append 4
Insert 0 at beginning
Remove 2
Reverse the list
Steps:
Use .append(), .insert(), .remove(), .reverse()
Output:
[0, 1, 3, 4]"""

# CODE : 

# original list
li = [1,2,3]
print("orginal list :",li)

# appending 2 in list
li.append(4)
print("list after appending 4 : ",li)

# adding 0 at th beginning at list
li.insert(0,0)
print("list after inserting 0 at beginning :",li )

# removing 2 from list 
li.remove(2)
print("list after removing 2 from it :",li)

# reversing the list 
li.reverse()
print("reversed list :",li)

"""
OUTPUT :
orginal list : [1, 2, 3]
list after appending 4 :  [1, 2, 3, 4]
list after inserting 0 at beginning : [0, 1, 2, 3, 4]
list after removing 2 from it : [0, 1, 3, 4]
reversed list : [4, 3, 1, 0]
"""
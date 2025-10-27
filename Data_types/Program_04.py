"""
Concept: 
Mutability
Question:
Create a tuple and try changing one element.
Steps:
Define t = (1,2,3)
Try t[0] = 10
"""

# code :

t_1 = (1,2,3)
print(t_1)
t_1[0] =10
print(t_1)



"""output :  
 File "C:\Users\DELL\Desktop\python-playground\Data_types\program_04.py", line 13, in <module>
    t_1[0] =10
    ~~~^^^
TypeError: 'tuple' object does not support item assignment"""

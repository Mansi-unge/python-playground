"""
Concept: 
Type promotion and arithmetic
Question:
What happens when you do 5 + 2.0, True + 10, and '5' + '2'?
Steps:
Try each expression.
Observe which works and why.
"""

# code :

print(5+2.0)
print(True + 10)
print("5" + "2")

"""
output :
7.0 ---  Python automatically performs type promotion (int → float) so that both are of the same type.
11  ---  In Python, True is treated as 1 and False as 0 in arithmetic, So this becomes 1 + 10.
52  ---  Both are strings, so + acts as a concatenation operator, not arithmetic addition.
"""
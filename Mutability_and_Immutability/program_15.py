# Write a program to:

# Modify a list inside a function and observe changes outside the function

def change_list(num):
  num.append(10)
  print("list inside function",num)


num = [2,4,6,8]
print("list outside function before function call : ",num)

change_list(num)
print("list outside the function after the function call :",num)

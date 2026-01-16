# Write a program to:
# Demonstrate the use of and, or, not operators

# and operator 
username = "mansi"
password = "mansi@123"

user_name = input("Enter your Username : ")
pass_word = input("Enter your Password : ")

if username == user_name and password == pass_word:
  print("Login Successfull.....!")
else:
  print("Login Failed")

# or operator 
email = "mansi@gmail.com"
username = "mansi"

my_email = input("Enter your email : ")
user_name = input("Enter your username : ")
if email == my_email or username == user_name :
  print("you can login")
else:
  print("enter valid username or email")


# or operator
blocked = False

if not blocked:
  print("You are not blocked....you can login")
else:
  print("you are blocked...")





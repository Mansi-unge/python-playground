# Write a program that:

# Takes username and password

# Prints Login Successful if both are correct, else Login Failed

username = "mansi"
password = "mansi@123"

user_name = input("Enter your Username : ")
pass_word = input("Enter your Password : ")

if username == user_name and password == pass_word:
  print("Login Successfull.....!")
else:
  print("Login Failed")
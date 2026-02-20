class Constructor_demo:
  def msg():
    print("this is not a constructor method")
  
  def __init__(self):
    print("This is a constructor")


cons = Constructor_demo()
cons.msg()
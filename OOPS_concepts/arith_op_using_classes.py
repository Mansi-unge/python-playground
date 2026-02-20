class AMO:
  a = 10
  b = 20
  def sum(self):
    print("Addition = ",self.a+self.b)

  def sub(self):
    print("Subtraction = ",self.a-self.b)

  def mul(self):
    print("Multiplication = ",self.a*self.b)

  def div(self):
    print("Division = end")
    print(self.a/self.b)


my_amo = AMO()
print(my_amo.a)
print(my_amo.b)
my_amo.sum()
my_amo.sub()
my_amo.mul()
my_amo.div()

class expenditure:
   def __init__(self,expenditure,savings):
       self.expenditure=expenditure
       self.savings=savings
   def display(self):
       print("expenditure is: %d" %self.expenditure)
       print("savings is: %d" %self.savings)
   def calculate(self):
       self.salary=self.expenditure+self.savings
   def disply(self):
       print("total salary : %d" %self.salary)
a=int(input("enter the expenditure"))
b=int(input("enter the savings"))
x=expenditure(a,b)
x.display()
x.calculate()
x.disply()
class student:
    def __init__(self,name,rollnumber):
        self.name=name
        self.rollnumber=rollnumber
    def display(self):
        print("my name is:" , self.name)
        print("my rollnumber is:" , self.rollnumber)
a=str(input("enter the name"))
b=int(input("enter the rollnumber"))
s=student(a,b)
s.display()

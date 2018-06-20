#circle
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        self.area=3.14*self.radius*self.radius
        print("the area of a circle is: %f"%self.area)
    def circumference(self):
        self.circumference=2*3.14*self.radius
        print("the circumference of a circle is: %f"%self.circumference)
n=int(input("enter the value of radius"))
s=circle(n)
s.area()
s.circumference()

        

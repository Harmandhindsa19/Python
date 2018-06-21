class shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
class rectangle(shape):
    def area(self):
        area=self.length*self.breadth
        print(area)
class square(shape):
    def area(self):
        area=self.length*self.breadth
        print(area)

m1=rectangle(5,6)
m1.area()
m2=square(4,4)
m2.area()


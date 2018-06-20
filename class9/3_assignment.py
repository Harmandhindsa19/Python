class temperature:
    def __init__(self, fahrenheit, celsius):
        self.fahrenheit=fahrenheit
        self.celsius=celsius
    def fahren(self):
        self.fahreneit=1.8*self.celsius+32
        print("enter the value of temperature in celius:", self.fahrenheit)

    def cel(self):
        self.celsius =  self.fahrenheit - 32/1.8
        print("enter the value of temperature in fahrenheit:", self.celsius)
c=int(input("enter the value of temperature in celsius: "))
f=int(input("enter the value of temperature in fahrenheit: "))
s=temperature(c,f)
s.fahren()
s.cel()


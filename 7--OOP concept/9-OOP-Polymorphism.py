#Polymorphism
#Dunder functions - double underscore
"""
  a+b -addition         a.__add__(b)
  a-b -subtraction      a.__sub__(b)
  a*b -multiplication   a.__mul__(b)
  a/b -division         a.__truediv__(b)
  a%b -modulous         a.__mod__(b)
"""

#complex number
class Complex:
    def __init__(self, real, img):
        self.real=real
        self.img=img
    
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)

num1=Complex(2,4)
num1.showNumber()

num2=Complex(3,6)
num2.showNumber()

num3=num1+num2
num3.showNumber()
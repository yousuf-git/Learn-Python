"""
Polymorphism --> Many forms

Example: Operator Overloading, Same op but diff meaning based on situation/usage
print(6 + 9) --> Add
print('6' + '9') --> Concat
print([1,3] + [4,5]) --> merge
"""
# I'm going to create a class Complex, to deal with complext numbers
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def setAttributes(self, real, img):
        self.real = real
        self.img = img
    
    def display(self):
        print(self.real,"i","+",self.img,"j")
    
    def __add__(self, num2): # dunder function, override + 
        print("Sum : ", self.real + num2.real, "i", "+", self.img + num2.img, "j")
    
    def __sub__(self, num2):
        print("Sub : ", self.real - num2.real, "i", "+", self.img - num2.img, "j")
    
    def __mul__(self, num2):
        print("Mul : ", self.real * num2.real, "i", "+", self.img * num2.img, "j")
    
    def __div__(self, num2):
        print("Div : ", self.real / num2.real, "i", "+", self.img / num2.img, "j")
    
    def __mod__(self, num2):
        print("Mod : ", self.real % num2.real, "i", "+", self.img % num2.img, "j")
    
    def __floordiv__(self, num2):
        print("Floor Div : ", self.real // num2.real, "i", "+", self.img // num2.img, "j")

num1 = Complex(-2,5)
num2 = Complex(-3,-9)
print("Num1 : ", end=" ")
num1.display()
print("Num2 : ", end=" ")
num2.display()

print()
num1 + num2
num1 - num2
num1 * num2
# num1 / num2 # Python 3.x doesn't support / operator overloading, so it will not work
num1 // num2

num1 % num2
# num1.__add__(num2)
# num1.__sub__(num2)
# num1.__mul__(num2)
# num1.__div__(num2)
# num1.__mod__(num2)

print("\nList of Dunder Methods: ")
print()
print(dir(int))
print()

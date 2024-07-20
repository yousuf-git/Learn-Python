# one class(child class) gets/derives attributes & methods of another class (parent class)

class Shape:
    def __init__(self, name):
        self.name = name
    def displayName(self):
        print("Shape Name:", self.name)

class Square(Shape):
    def __init__(self, name, len):
        # self.name = name
        self.len = len
        self.name = name # this will not use the parent attribute 'name' , but a new attribute will be created; upcoming use of super() will clear this doubt
    def getAttributes(self):
        self.displayName()
        print("Length of Shape:", self.len)

sq = Square("Square 1", 5)
sq.getAttributes()

# super() => used to access super/parent class attr & methods
# Types of inheritance --> single, multi-level and multiple

"""
1. Single Level --> Single Parent, Single Child
2. Multi-Level --> Parent1 -- Child (Parent2) -- Child 
3. Multiple --> Single Child class but multiple Parent classes
"""

# Single Level already done
# Multi-Level (Shape --> Triangle --> Equilateral Triangle)
# Shape {Name}, Triangle {Name, lenA}, EqTriangle {Name, lenA, lenB, lenC}
class Triangle(Shape):
    def __init__(self,name, lenA):
        super().__init__(name) # call Shape class constructor
        self.lenA = lenA

class EqTriangle(Triangle):
    def __init__(self, name, lenA):
        super().__init__(name, lenA) # set inherited attributes, name and lenA
        self.lenB = self.lenC = lenA # 2 new lengths of its own
    def displayAttributes(self):
        self.displayName()
        print("Length of Side A:", self.lenA)
        print("Length of Side B:", self.lenB)
        print("Length of Side C:", self.lenC)

"""This Object will now have all attributes of Shape and Triangle"""
eqTri = EqTriangle("Equilateral Triangle 1", 20)
eqTri.displayAttributes()

# Multiple Inheritance
class A:
    def __init__(self, a):
        self.a = a

    def methodA(self):
        print("I am method A")

class B:
    def __init__(self, b):
        self.b = b

    def methodB(self):
        print("I am method B")

class C(A, B):
    def __init__(self, a, b, c):
        A.__init__(self, a)  # Initialize attributes from class A
        B.__init__(self, b)  # Initialize attributes from class B
        # Avoid use of super in case of mulitple inheritance, this will always call constructor of class A
        # super().__init__(a)
        # super().__init__(b)
        self.c = c

    def printAttributes(self):
        print("a:", self.a, "b:", self.b, "c:", self.c)
        # print("a:", self.a, "c:", self.c)

cObj = C(1, 2, 3)
print("Attributes of class C Object:")
cObj.printAttributes()

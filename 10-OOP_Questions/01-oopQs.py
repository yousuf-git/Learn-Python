# 1. Define a circle class to create a circle with radius r using the construtor. Define an Area() and perimeter() method for calculating area and perimeter of circle respectively

class Circle:
    def __init__(self, rad):
        self.rad = rad
        print("Circle Created with radius:", self.rad)
    def setRadius(self, rad):
        self.rad = rad
    def getArea(self):
        return 3.14 * pow(self.rad, 2)
        # return 3.14 * self.rad ** 2
    def getPerimeter(self):
        return 2 * 3.14 * self.rad

circle  = Circle(3.9)
print("Area of Circle:", circle.getArea())
print("Perimeter of Circle:", circle.getPerimeter())
print("\n")
# 2. Define an employee class with attributes role, department and salary. showDetails() method to display all detaills. Create an engineer class that inherits properties from Employee and additional attributes name and age

class Employee:
    
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role:", self.role)
        print("Role:", self.dept)
        print("Role:", self.salary)
        
class Engineer(Employee):
    def __init__(self, name, age, role, dept, salary):
        self.name = name
        self.age = age
        super().__init__(role, dept, salary)
    def showDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().showDetails()
        
        
engineer = Engineer("Harry", 20, "Computer Enginner", "CS", 690000)
engineer.showDetails()   
print("\n")

# 3. Create a class called Order which stors item and its price. Use Dunder Function __gt__() to convet that order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    # def __gt__(obj1, obj2):
    #     return obj1.price > obj2.price
    # same as above
    def __gt__(self, obj):
        return self.price > obj.price

order1 = Order("Butter", 200)
order2 = Order("Cheese", 100)

# __gt__() will be called and order1 & order2 will be passed as arguments
if order1 > order2:
    print(order1.item, "is expensive")
else:
    print(order2.item, "is expensive")
        
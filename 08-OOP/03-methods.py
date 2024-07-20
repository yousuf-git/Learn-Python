# Methods --> Functions written in class for objects

class Student:
    # Constructor
    def __init__(self):
        print("Student Added...")
    
    # Method 1: to set marks of student
    def setMarks(self, marks):
        self.marks = marks
        print("Marks Added Successfully !")
    
    # Method 1: to get marks of student
    def getMarks(self):
        return self.marks
    
# Creating object and using its methods
student_1 = Student()
student_1.setMarks(69)

print("Marks:", student_1.getMarks())

# Q: Create a class Student that takes name and marks of 3 students as arguments in constructor. Then create a method to get average of marks

# Previous class will be overridden
class Student:
    def __init__(self, oop, ds, db):
        self.oop = oop
        self.ds = ds
        self.db = db
    
    def getAvg(self):
        return (self.oop + self.db + self.ds)/3
        
s1 = Student(95, 90, 93)
print("Average:", s1.getAvg())

# Static Methods --> class level methods [doesn't need self parametere]
class Employee:
    CompanyName = "NASA"
    @staticmethod #decorator that converts a method to static one
    def greet():
        print("Welcome to", Employee.CompanyName)
        
emp = Employee()
emp.greet()
        
# class is a blueprint for a real word object/instance
# an object can be any entity or concept

# creating class
class Employee:
    # Class attributes
    name = "newEmployee"
    contact = "newContact"

# creating objects of that class
employee1 = Employee()
employee2 = Employee()
# print(employee1) # object details

# Both employees will have same name initially bcz both have same blueprint
print(employee1.name)
print(employee2.name)

# Constructor --> __init__() function to create objects of a class
# Constructors have one parameter always, that points to the object
class Student:
    
    # Better to use one constructor at a time
    
    # Non-Parameterized/Default Constructor
    # def __init__(self): 
    #     print("Creating new Instance of Student....")
          
    # Parameterized Constructor
    def __init__(self, name = ""): # if names is passed when constructor called then that value will be used otherwise it will be empty name
        self.name = name # here self.name means a new Attribute for specially object that is passed as self
    
    
# Calling parameterized constructor with diff values
student1 = Student()
student2 = Student("Mr. Harry")

print("Student1 Name:", student1.name)
print("Student2 Name:", student2.name)

# Calling parameterized constructor for object 2
# student2 = Student("Rohn")
# print(student2.name)

# Method Overloading doesn't work in python as in other lanaguages i.e. by same name but diff args
        
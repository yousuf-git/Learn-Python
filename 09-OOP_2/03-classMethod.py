"""First revise static method --> doesn't manipulate object(self) attributes, used for utility"""

# Now coming to class method....
class Student:
    name = "harry" # class attribute
    
    # Below method is manipulating object attribute not class one
    def updateName(self, name):
        self.name = name # new object attribute 'name' will be created
        
        # Student.name = name # Method 1 to change class attribute
        # self.__class__.name = name # Method 2 to change class attribute
        
    # Method 3 of changing class attributes
    @classmethod  # overriding works ???
    def changeName(cls, name):
        cls.name = name
    
# Case 1
st1 = Student()
st1.updateName("Rohn") # this method deals with object attribute

print("\nStudent 1 Object Name:", st1.name) # rohn --> object attribute
print("Student 1 Class Name:", Student.name) # harry --> class attribute

# Case 2
st2 = Student()
st2.changeName("Weasly") # this method will change the class attrbute

print("\nStudent 2 Object Name:", st2.name) # weasly 
print("Student 2 Class Name:", Student.name) # weasly 

# print(st.__class__) # returns type of object --> class, to whom it belongs to

"""
Methods
1. static methods => no use of class or obj/self attribute
2. class methods (cls) => to manipulate class attributes
3. instance/normal methods (self)  => to manipulate object/instance attributes
"""
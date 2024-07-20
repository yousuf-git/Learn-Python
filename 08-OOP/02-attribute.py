# Attributes means properties or simply variables of an entity or blueprint

# 1. class.Attribute (For all objects of this type of class)
# 2. object.Attribute (For only the specific object itself)

class CsStudent:
    className = "Computer Science" # single location in memory 
    stName = "anonymous"
    # def __init__(self, name):
    #     self.name = name
        
# class attribute will be overridden/overwritten by object attributes 
# student1 = CsStudent("Harry") 
# student2 = CsStudent("Rohn")

student1 = CsStudent() 
student2 = CsStudent()

# student1.className = "Physics" # this will create a new attribute for object student1 only

CsStudent.className = "Maths" # change class attribute for every instance

print("\nStudent 1 Details...")
print("Class Name:", student1.className)
print("Student Name:", student1.stName)

print("\nStudent 2 Details...")
print("Class Name:", student2.className)
print("Student Name:", student2.stName)
    

"""Query --> If class attribute is a single memory location than if one object chnages it, it should be changed for other objects too...but not happening """

"""Ans --> yes, object can change class attribute that will also be changed for all other objects but the way of accessing class method should be done carefully """

"""student1.className = "Physics" --> here object is not accessing class attribute but creating its own new attribute with same name as of class attribute

CsStudent.className = "Maths" --> this is the way to access class attribute.
    This statement can be written inside a function and object can use that function to change class attribute, such functions are classMethods, discussed in next lecture OOP-2"""
# 3 ways to create a string
firstName = "Harry"
middleName = '''James'''
lastName = 'Potter'

# book = "harry's book" # --> to store ' in a string
# escape sequences (\n, \t, ....)
print(firstName, "\n", middleName, "\n", lastName) # for new line

# concatenation of strings
fullName = firstName+" "+middleName+" "+lastName
print("Full Name:", fullName)

# string methods
# 01- len(String) --> returns length of characters in a string
print("Length of Full Name:", len(fullName)) # spaces also counted

print("Name First Letter:", fullName[0]) # H
# fullName[0] = 'B' # Type Error, item assignment not allowed

# Slicing (Parts of a string)
# strName[start_index : ending_index] # end index value not included
print("First Name (by Slicing):", fullName[0:5])

# Below 3 statements will give same output
print("Full Name (by Slicing):", fullName[0:len(fullName)])
print("Full Name (by Slicing):", fullName[0:])
print("Full Name (by Slicing):", fullName[:len(fullName)])

# negative indexing
#  H   A   R   R   Y
# -5  -4  -3  -2  -1

name = 'harry'
print()
print("Negative indexing")
print("Only Start Index:", name[-5:]) # harry
print("Only Ending Index:", name[:-1]) # harr (last index is not included)
print("Both Indices:", name[-5:-2]) # har (last index is not included)

# String Functions
# 02- endswith(string) # True/False
print("harry ends with ry:", name.endswith('ry'))

# 03- capitalize() # returns a new string
print("Capitalized Name:", name.capitalize()) # harry to Harry

# 04- replace(oldValue, newValue) # returns a new string
print("Replaced Name:", name.replace("h", "b"))
# print("Replaced Name:", name.replace("H", "b")) # no change bcz H is not in name (harry)

# 05- find(string) # returns index
print("Index of y in name:", name.find('y')) # 4
print("Index of A in name:", name.find('A')) # -1 bcz no such char in name

# 06- count(string)
print("r in Name is", name.count('r'), "times")




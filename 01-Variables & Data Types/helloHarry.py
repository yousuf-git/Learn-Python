def helloHarry(s):
    {
        print("Hello Harry")
    }

helloHarry("print")

print("Hello", "Harry") # same line
print("Hello")
print("Harry") # new line

# variables (memory is dynamically allocated)
name = "harry" # single quotes can be used
age = 20
print("Name:", name)
print("Type:", type(name))
print("Age:", age)
print("Type:", type(age))

# swap 2 variables
a = 2
b = 3
print("Before Swap:", "A:", a, "B:", b)
temp = a
a = b
b = temp
print("After Swap:", "A:", a, "B:", b)



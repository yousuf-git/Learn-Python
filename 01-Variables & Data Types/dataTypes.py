# 01 integer (+ve, -ve and zero)
position = 69
# print(position)

# 02 string (characters)
positionStr = "sixty nine"
print(positionStr)
positionStr = "'sixty nine'"
print(positionStr)
positionStr = 'sixty nine'
print(positionStr)
# positionStr = '''sixty nine'''
print(positionStr)

# 03 float (floating point values)
marks = 80.34

# 04 boolean 
isAdult = True
isAddict = False

# 05 none (if datatype or value is not known initially)
marks = None 
print("Marks type:", type(marks))

# type conversion (automatically done by python)
a, b = 60, 9.0
sum = a+b
print("Sum:", sum, "Type:", type(sum)) # float (superior type)

mrk1, mrk2 = "60", 9
# total = mrk1+mrk2 # TypeError (bcz string cannot be added to int)

# type casting (explicitly/manually done by programmer)
total = int(mrk1) + mrk2
print("Total after type casting:", total)

name = "harry"
print(int(name)) # ValueError (bcz this string cannot be converted to int type)



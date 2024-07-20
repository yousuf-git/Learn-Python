# List is equivalent to array but list can store values of diff data types
marks = [12, 12, 32, 23, 56, 54, 45]
print(marks)
print("Type of marks:", type(marks))
print("Marks at index 2:", marks[2])
print("Length of marks list:", len(marks))

# lists are mutable (can be changed) but actually Strings are not
record = ["Harry", 20, 3.73]
record[0] = "Barry"
print(record)

name = "harry"

# name[0] = "B" # TypeError: 'str' object does not support item assignment
print(name)
# name.replace('h', 'B')

# List Slicing
# Same as slicing in Strings
# Below 3 will have same output
print(record[:])
# print(record[0:])
# print(record[:len(record)])
print(record[0:2]) # record[2] will not be included


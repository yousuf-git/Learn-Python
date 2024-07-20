# Set --> Collection of unorderd items(no specific index), its elements are unique and immutable but set itself is mutable (elements can be removed/added)

# int, float, str, tuple (immutable) --> allowed in set
# list & dictionary (mutable) --> not allowed in set 
# collection = {1,2,3,3,3,[2,4]} # error

# Creating a set of cities
cities = {"Berlin","Tokyo","Hogwards", "Tokyo"} # will be auto arranged and duplicate items will be removed
print("Cities:", cities)
print("Type of Cities Collection:", type(cities))
valuesSet = {69, 69.0} # single element
valuesSet = {69, 69.69} # diff elements

# Empty set
collection = {} # this will not be an empty set bcz it is syntax of dictionary
# print("Type of collection before:", type(collection)) # dict
collection = set()
# print("Type of collection after:", type(collection)) # set

# Set Methods
# 01- set.add(val)
collection.add("Stationary")
collection.add("Paint")
collection.add("Paint") # not effect on set
collection.add((2,4,6)) # adding tuple (immutable)
# collection.add([2,4,6]) # adding list (mutable) --> error: mutable (unhashable) Type
print("Added values in Collection:", collection)

# 02- set.remove(val)
collection.remove("Paint")
# collection.remove("paint") # KeyError
print("Removed values from Collection:", collection)

# 03- set.clear() --> empties the set
collection.clear()
print("Cleared Collection: ", collection)

# 04- set.pop() --> removes and returns a random value from set
person = {"p1", "p2", "p3"}
print(person.pop())
print(person.pop())
print(person.pop())
# print(person.pop()) # key error bcz person set is empty here

#  05- set.union(set2) --> same as in Math (combine all unique values)
setA = {1,2,3} 
setB = {3,4,5}
print(setA.union(setB)) # returns a new set, original ones are not affected

#  06- set.intersection(set2) --> only common elements
print(setA.intersection(setB)) # also returns a new set, original remain same










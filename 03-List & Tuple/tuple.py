# tuple --> immutable sequence of values
names = ("harry", "james", "potter", "potter")
print("Tuple:", names, " Type:", type(names))

username = ("harry")
print("Type of username without comma:", type(names))

username = ("harry",)
print("Type of username with comma:", type(names))

# slicing in tuple also works same as strings and lists

# tuple methods
# 01- tuple.index(element) --> returns index of element (first)
print("Index of Element potter:", names.index("potter"))

# 02- tuple.count(element) --> no. of times element is in tuple
print("Potter in names tuple is", names.count("potter"), "times")

# 01- Store some word meanings in a dictionary
dict = {
    "Gay" : ("Happy", "Joyful"),
    "Guy" : "Boy"
}
print("Meaning of Gay:", dict["Gay"])

# 02- Input marks of 3 subjects and store them in dictionart
result = {}
# result.update({"Math " : input("Enter Marks of Math: ")})
# result.update({"Phy" : input("Enter Marks of Physics: ")})
# result.update({"Comp" : input("Enter Marks of Computer: ")})

# print("Result:", result)
# print("Makrs of Computer:", result["Comp"])

# 03- store 9 and 9.0 separately in a set
# val = {(9, 9.0)} # will store as single element i.e., {9}
# 3 methods
val = {9, "9.0"}
val = {"9", 9.0}
val = {("int", 9), ("float", 9.0)}

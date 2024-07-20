info = { # Outer Dictionary
    "name" : "harry",
    "result" : { # Inner Dictionary
        "DSA" : 90,
        "DB" : 98,
        "OS" : 93
    }
}
# 01- dict.keys() --> returns dict_keys (list), can be type casted to simple list
print("Keys in info:",info.keys())
# Keys in a list
print("List of Keys in info:",list(info.keys())) # type casting dict_keys to list
# Count keys in dictionary
# 3 ways
print("Length of info dictionary:")
# print(len(list(info.keys()))) # first convert to list than len(list)
# print(len(info.keys())) # it is actually len(dict_keys)
print(len(info)) # len(dict)

# 02- dict.values()
print("Info Dict Values:",info.values()) # returns dict_values, can also be type casted
print("Info Dict Values List:",list(info.values()))

# 03- dict.items() --> returns key-value pairs as tuples
print("Pair Items in info:",info.items())
print("List of Pair Items in info:",list(info.items())) # type casted to list
# Accessing specifc value pair through list
print("Pair Item at index 0:", list(info.items())[0]) # Convert to list then access specific index pair (single tuple)

# 04- dict.get(key)
print("Value by dict.get(key):", info.get("name"))
print("Value by dict[key]:", info["name"]) # Same as above
# diff b/w dict.get(key) and dict[key]
info.get("Name") # None
# print(info["Name"]) # Error

# 05- dict.update(newDict)
newDict = {
    "country" : "France"
}
info.update(newDict) # Method 1 --> dict Variavle
info.update({"city" : "Paris"}) # Method 2 --> updating by direct dictionary without variable
info["result"].update({"DSA" : 91}) # if existing key is used then it will be updated (duplicate keys are not allowed in dictionary)
print("Updated Info:", info)

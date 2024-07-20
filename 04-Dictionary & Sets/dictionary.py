info = { # can be null initally, keys and values can be added later
    "name" : "harry",
    "age" : 20,
    "isMature" : True,
    "marks" : [85, 87, 90]
    # key can be int, float, tuple etc. (immutable)
    # value can be mutable or immutable
}

print("Info", info, "\nType:", type(info))

# Dictionary is mutable, not redundant keys, unordered
# Insted of index we can use key name as dic[keyName]

print("Name:", info["name"])
# Changing value of an existing key
info["marks"][0] = 89
print("Marks:", info["marks"])

# If key is not present already 
# print(info["contact"]) # key Error

# Adding new key in dictionary
info["contact"] = 911
print("Updated Info:", info)

# Nested dictionary
info = { # Outer Dictionary
    "name" : "harry",
    "result" : { # Inner Dictionary
        "DSA" : 90,
        "DB" : 98,
        "OS" : 93
    }
}

print("Name:", info["name"], ", OS Marks:", info["result"]["OS"])
""" with open("file_path", "mode") as f: 
        Block of operations on file  """
# store file stream in f

with open("07-File I-O/test.txt", "r") as f:
    data = f.read()
    print(data)
    # f.close() --> no need bcz "with" automatically do this, if there is any additional functional expression than use it either outside of "with" block or first manually close file and then do the stuff
"""    
Deleting a file --> using os module(contains already written functions)

Few modules are already installed, few needs to be installed by pip(package installer for python) as: 
# pip install module_name or
# pip3 install module_name
"""

import os # built in module
# In write mode if a file doesn't exists already, python crates it 

# First create a file
file = open("07-File I-O/new.txt", "w+") # if test.txt exists, delete it first then run this to see the result
file.write("I am a new file")
# print(file.read()) # cursor is at end so nothing will be in output if you try to read

# run this to delete it
# os.remove("new.txt")
# print("New File deleted successfuly")


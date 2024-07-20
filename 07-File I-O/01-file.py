# File I/O Methods (it will be better if all methods are tested one by one)

# 1. open("file_path", "mode")
file = open("07-File I-O/test.txt", "r") # stream of characters is returned
# data = file.read(4) # read data from stream
# print(data)
# print(type(data))
# file.close()

# 2. file.read(No_of Characters)
chrs = file.read(4)
print("First 4 Characters:", chrs)

# 3. file.readline() --> To read a line from file 
line1 = file.readline()
print("Line 1:", line1)

line2 = file.readline()
print("Line 2:", line2)

"""
After each line in output there will be a new line (bcz there exists an invisible character \n at the end of each line in text file)

If a file is already read, there is a cursor that moves, if file ends and we try to read further then there will be an empty line in output
""" 

# 4. Wrtiting a file
    # i) open in "w" mode --> overwrite
    # ii) open in "a" mode --> append (add at end)
# Method-1
file = open("07-File I-O/test.txt", "w")
file.write("Hi, This is Harry,") # this will remove old data
print("Write operation done")
file.close()

# Mwthod-2
file = open("07-File I-O/test.txt", "a")
file.write(" Practicing Python !")
file.write("\nTopic File Input/Output")
print("Appending done")
file.close()

# r+ mode --> used to read file and start writing from start
file = open("07-File I-O/test.txt", "r+")
file.write("Writing...") # it will write at beginning, if there is something already at beginning, that will be replaced
print(file.read()) # Now cursor is at (Writing...<) so data after this will be read
file.close()

# w+ mode --> used to read and write file but first all data will be truncated
file = open("07-File I-O/test.txt", "w+")
print("Trying to read file instantly after w+:", file.read()) # blank

file.write("Hello, writing new data...")
print(file.read()) # also blank, why ? bcz after write operation the cursor is at the end and there's nothing to read
file.close()

# a+ mode --> read and append, cursor is at end, if we try to read it will be blank
file = open("07-File I-O/test.txt", "a+")
print(file.read()) # blank line





    

file.close()


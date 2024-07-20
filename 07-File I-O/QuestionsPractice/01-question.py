# 1- Create a new file "question1.txt" and add following data in it:
"""
Hi bruh
I'm Learning File I/O
using Java.
It's kinda fun in Java
"""
# Write Functions for the following:
# 2- Replace all occurance of Java with Python
# 3- Search for a specific word in file
# 4- Search for a specific word in file and display line no where it came first, display -1 if word not found


# Solution:
# to replace / overwrite 
def replace():
    with open("07-File I-O/QuestionsPractice/question1.txt", "r") as f:
    # with open("07-File I-O/QuestionsPractice/question1.txt", "r+") as f:
        str = f.read()
        newStr = str.replace("Java", "Python")
        # print(newStr)
        # f.write(newStr) # cursor is at end so new data will be added at end (wrong way), we need to open file again from start
        f.close()
        
    with open("07-File I-O/QuestionsPractice/question1.txt", "w") as f:
        f.write(newStr)

def search(str):
    with open("07-File I-O/QuestionsPractice/question1.txt", "r") as f:
        data = f.read()
        # if data.find(str) != -1: 
        if data.__contains__(str):
            print(str,"exists in file")
        else:
            print(str,"doesn't exists in file")
            

def search_in_line(str):
    with open("07-File I-O/QuestionsPractice/question1.txt", "r") as f:
        line_no = 1
        line = f.readline()
        while line: # True if line is a valid value
            if str in line:
                return line_no
            else: 
                line = f.readline()
                line_no+=1
    return -1    
       

# To create and write data in file
with open("07-File I-O/QuestionsPractice/question1.txt", "w+") as f:
    f.write("Hi bruh\nI'm Learning File I/O\nusing Java.\nIt's kinda fun in Java")
    print("File Created")
    f.close()
    # Uncomment and run following functions one-by-one to see effects
    
    # replace()
    # search("Learning")
    # str = "Python"
    # line = search_in_line(str)
    # if line == -1:
    #     print(str, "not found in file")
    # else :
    #     print(str, "found on line no.", line)

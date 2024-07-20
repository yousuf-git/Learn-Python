# while loop
counter = 1
while counter < 3 :
    print("Welcome Harry")
    counter+=1

# Q: Print Elements of a list
myList = [2,3,12,132,32]
i = 0
while(i<len(myList)):
    print("List Item:", myList[i])
    i+=1

# Q: Search for marks in given tuple
marks = (89,90,45,69,70,84)
n = int(input("Enter Marks: "))
i = 0
isFound = False
while(i<len(marks)):
    if(marks[i]==n):
        isFound = True
        # break
    i+=1
if(isFound):
    print("Marks", n, "exist")
else:
    print("Marks", n, "doesn't exist")    

# Q: Factorial of n
num = int(input("Enter Number: "))
print("Factorial of", num, "is: ")
f = 1
i=1
while(i<=num):
    f=f*i
    i+=1

print(f)
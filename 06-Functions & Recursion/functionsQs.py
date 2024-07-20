# Q: Function to print length of a list
myList = [3,4,3,2,"harry"]

def printLength(l):
    print("Length of list:", len(l))
printLength(myList)

# Function to print list
def displayList(l):
    for item in l:
        print(item, end = " ")
print("List:", end = " ")
displayList(myList)

print()
# Q: Function to calculate and return factorial
def calFactorial(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f
print("Factorial of 5:", calFactorial(5))


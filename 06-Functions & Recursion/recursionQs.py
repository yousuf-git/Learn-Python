# Q: recursive function to display sum of n natural numbers

def displaySum(n):
    if(n==0):
        return 0
    else:
        return n + displaySum(n-1)
print("Sum of first 4 numbers:", displaySum(4))

# Q: recursive function to print all elements of list
myList = ["Element 1", "Element 2", "Element 3"]

def displayList(l, index):
    if(index == len(l)): # Base Case
        return
    else:
        print(l[index])
        displayList(l, index+1)
        # displayList(l, index-1)
        # print(l[index])

displayList(myList, 0)
print()
# method 2 forward display

def showList(l, index):
    if(index == -1): # Base Case
        return
    else:
        print(l[index])
        displayList(l, index-1)
showList(myList, len(myList)-1)
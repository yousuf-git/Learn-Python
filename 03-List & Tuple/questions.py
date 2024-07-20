# 01- Input 3 actors name, store them in list and then display
actors = [] # empty list
test = () # empty tuple
# print(type(actors))
# print(type(test))
# UnComment the code below then execute....
# actors.append(input("Enter Actor 1: "))
# actors.append(input("Enter Actor 2: "))
# actors.append(input("Enter Actor 3: "))
print(actors)

# 02- Check if a list is palindrome or not (list = reverse of list)
numList = [1,2,3,2,1]
tempList = numList.copy()
tempList.reverse()
# print(tempList)
# print(numList)
if(numList == tempList):
    print("List is Palindrome")
else:
    print("List is not Palindrome")

# 03- Count number of students with A grade in marks tuple, given grades are C, D, A, A, B, B, A
marks = ("C", "D", 'A', 'A', 'B', 'B', 'A')
print("Number of students with grade A:", marks.count("A"))
# 03(b)- Store above values in a list and sort them from A to D
marksList = ["C", "D", 'A', 'A', 'B', 'B', 'A']
marksList.sort()
print("Sorted Marks List:", marksList)
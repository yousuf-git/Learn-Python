myList = [2,1,3,4]
print("Original list:", myList)
# 01- append(item) --> add element at the end 
myList.append(4) # returns none
print("Appended list:", myList)

# 02- sort() --> Arrange in ascending Order
myList.sort() # returns None, changes the original list
print("Ascending Sorted list:", myList)

students = ["harry", "rohn", "george", "jinny"]
students.sort() # g > h > j > r
print("Sorted Students List:", students)

# 03- sort(reverse = True) --> Arrange in descending Order
myList.sort(reverse = True)
print("Descending Sorted list:", myList)

# 04- reverse() --> reverse the list
myList.reverse()
print("Reverse list:", myList)

# 05- insert(idx, item)
myList.insert(4, 5) # index 4 and other elements will be right shifted
print("Inserted new element in list at index 4:", myList)

# 06- remove(item)
students.remove("harry")
print("Students after removing harry:", students)
# 07- pop(idx)
students.pop(0) # students[0] = george
print("Students after pop element at index 0:", students)
# for element in list/tuple:
myList = ["harry", "Rohn", "Hermini"]
print("List")
for val in myList:
    print("Name:", val)

myTuple = (2,3,3,2)
print("Tuple")
for val in myTuple:
    print("Num: ", val)
else: # optional
    print("Loop Ended")
    print()

name = "HARRY"
for ch in name:
    print("Character:", ch)
else:
    print()

# range(n) # returns a sequence from 0 to n-1, step 1
# range(st, end) # from st to end-1, step 1
# range(st, end, stepSize) # from st to end-1, stepSize 1


seq = range(5)
print("Type of seq:", type(seq))
for i in seq:
    print("Iteration:", i)
print()

# range can also be used directly
# for i in range(5):
#     print("Iteration:", i)
# else:
#     print()

# Q: Print Odd numbers from 1 to 10
print("Odd Numbers from 1 to 10: ")
for i in range(1, 10, 2):
    print(i)
else:
    print()

# Q: Print table of number
# num = int(input("Enter Number: "))
num = 69
for i in range(1, 11):
    print(i*num)

# pass --> placeholder for future use (empty block)
for i in range(1, 5):
    pass # (if pass is not used it will be an error)
else:
    print()
print("Loop Passed")

# Q: Factorial of n
num = int(input("Enter Number: "))
print("Factorial of", num, "is: ")
f = 1
for i in range (1, num+1):
    f=f*i

print(f)

# Q: Print Prime and composite numbers in a range
# Suppose range is from 0 to 50
primeList = []

for n in range(0,51):
    for r in range(2, int(n/2+1)):
        if n%i == 0:
            print("")
        
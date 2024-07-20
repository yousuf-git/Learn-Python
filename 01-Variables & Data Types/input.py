# input() statement is used to get user input
name = input("Enter Name: ")
print("Hi,", name, "dude")

# input() always returns a String
inputVal = input("Enter Value: ")
print("Type of your input:", type(inputVal))
# value can be type casted according to nead
marks = float(input("Enter Marks: "))
print("Type of Marks:", type(marks))

# Q: Input 3 float numbers and display their average
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
num3 = float(input("Enter Third Number: "))
avg = (num1+num2+num3)/3
print("Average:", avg)

# Q: Input side length and calculate volume of cube
# Try to do it yourself.....
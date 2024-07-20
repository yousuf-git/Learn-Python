# Block of statement to perform specific task and can be called anytime
# def keyword is used to define function
def displaySum(a, b): # function definition
    print("Sum:", a+b)    
displaySum(3,6) # function call
print("Type of displaySum:", type(displaySum))

def getSum(a, b):
    return a+b
print("Sum of 9, 10:", getSum(9, 10))

# if there is no return type function returns None

# Q: Function to calculate avg of 3 numbers
def getAvg(a,b,c):
    return (a+b+c)/3
print("Avergae of 5,8,10:", getAvg(5,8,10))

# print function
print("String 1","String 2", sep = "#", end = "\t")
print("String 3")

def getProduct(a,b=4):
    print("Product:", a*b)
getProduct(3) # One argument will be passed from here and other is default

# pass keyword is used just pass control out from the function
def futureFunc():
    pass

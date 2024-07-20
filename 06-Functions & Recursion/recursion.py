# recursion --> when function calls itself
# display numbers from n to 1
def display(num):
    if(num>0):
        print(num, end = " ")
        display(num-1)
    return

display(10)
print()
# calculate factorial of n by recursion

def calFactorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * calFactorial(n-1)
print("Factorial of 5:", calFactorial(5))
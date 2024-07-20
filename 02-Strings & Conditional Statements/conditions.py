# if-elif-else 
gender = str(input("Enter Gender:"))
if(gender.__eq__("male")):
    print("Qualified") # 4 spaces indentation
elif(gender.__eq__("female")):
    print("Disqualified")
else:
    print("F*ck Off")

# Q: Allocate grade based on marks by following criteria
# A(90+), B(80 to 90), C(70 to 80), D(60 to 70), F(Less than 60)
marks = float(input("Enter Makrs: "))
grade = None
if(marks>=90 and marks<100):
    grade = 'A'
elif(marks>=80 and marks<90):
    grade = 'B'
elif(marks>=70 and marks<80):
    grade = 'C'
elif(marks>=60 and marks<70):
    grade = 'D'
elif(marks<60):
    grade = 'F'
else:
    print("Invalid Marks!")
print("Your Grade:", grade)

# Nesting and try-except (in case of any input other than integer)
try:
    age  = int(input("Enter Age: "))
    if(age>18):
        if(age<60):
            print("Eligible")
        else:
            print("Not Eligible")
except:
    print("Invalid Age!")   
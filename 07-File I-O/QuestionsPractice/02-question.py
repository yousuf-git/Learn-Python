# From a file that has numbers separated by ',' count even numbers 

def method1():
    with open("07-File I-O/QuestionsPractice/csv.txt", "r") as f:
        values = f.read()
        # print(values)
        num = ""
        myList = []
        for i in range(len(values)): # check each char
            if values[i].__eq__(","):
                myList.append(num)
                # myList.append(int(num)) # this will remove space also but if you want to remove space in next step you can leave it
                num = "" # for new value of number
            else :
                num+=values[i]
        print("Even Numbers: ")
        for i in range(len(myList)):
            myList[i] = myList[i].replace(" ", "") # to remove spaces
            if(int(myList[i])%2==0):
                print(myList[i])

def method2():
    with open("07-File I-O/QuestionsPractice/csv.txt", "r") as f:
        values = f.read()
        # print(values)
        
        myList = values.split(",")
        print(myList)
        
        print("Even Numbers: ")
        count=0
        for num in myList:
            # num = num.replace(" ", "") # to remove spaces (optional) bcz int will do its job
            if(int(num)%2==0):
                print(num)
                count+=1
        print("Total Even Numbers:", count)

# function calls are below, run one by one         

# method1()
method2()
# del keyword
# used to delete object or its properties

class Test:
    def __init__(self, name):
        self.name = name

testObj = Test("Harry")
print("Test Obj Name:", testObj.name)

"""Uncomment and try to run and then see the effect"""
# del testObj.name
# print(testObj.name) #AttributeError: 'Test' object has no attribute 'name'

# Private (like) attributes and methods
# use __ before name of attribute or method

class Account:
    def __init__(self, accNo, psw):
        self.__accNo = accNo # private attribute 1
        self.__psw = psw # private attribute 2  
    def getPass(self):
        return self.__psw
        
account = Account(1001006969, 123)
# print(account.__accNo) # AttributeError: 'Account' object has no attribute '__accNo'

print(account.getPass())

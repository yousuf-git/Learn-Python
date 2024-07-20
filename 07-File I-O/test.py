with open("07-File I-O/test.txt", "a") as f:
    data = f.write("\nNew text by 'a' mode") # returns number of characters written
    print(data)
    
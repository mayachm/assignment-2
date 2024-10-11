names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]
while True:
    letter=str(input("Enter letter: "))
    for i in names:
        if letter in i:
            print(i)        
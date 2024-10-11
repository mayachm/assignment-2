numbers = [-12, 4, 12, 25, 67]
t=True
while t==True:
    nb=int(input("Enter a number: "))
    if nb==-99:
        t=False
        print(t)
    else:
        numbers.append(nb)
        numbers.sort()
        print(numbers)
             
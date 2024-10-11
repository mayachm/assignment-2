list1 = [54,76,2,4,98,100]
a=int(input("Enter first Integer"))
b=int(input("Enter second Integer"))
c=min(a,b)
d=max(a,b)
for i in list1:
    if c<=i and d>=i:
        print(i)
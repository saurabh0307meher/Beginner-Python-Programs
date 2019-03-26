#largest of two numbers
a=int(input("Enter 1st nos"))
b=int(input("Enter 2nd nos"))
c=int(input("Enter 3rd nos"))

if (a>b and a>c):
    print(a,"is greatest")
elif (b>c):
    print(b,"is greatest")
else:
    print(c,"is greatest")

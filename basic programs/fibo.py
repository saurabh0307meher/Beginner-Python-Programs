#fibonacci
x=int(input("Enter no of fibonacci numbers"))
a=0
b=1
print(a)
print(b)
for i in range(0,x):
    x=a+b
    a=b
    b=x

    print(x)
    

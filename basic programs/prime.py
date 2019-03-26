#prime
a=int(input("enter a number"))

if a>1:
    for i in range(2,a):
        if(a%i==0):
            print("not prime number")
            break
    else:
        print("prime")
        
else:
    print("not prime")

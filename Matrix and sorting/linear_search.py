#x=[1,2,3,4,5]
x = list()
num = input("Enter how many elements you want:")
print ("Enter numbers in array: ")
for i in range(int(num)):
    n = input("num :")
    x.append(int(n))
print ("ARRAY: ",x)
n=len(x)
number_to_find=int(input("enter element to be found"))
for i in range(0,n):
    if x[i]==number_to_find:
        print("number found")
    else:
        print("not found")

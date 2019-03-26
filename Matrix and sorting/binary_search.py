#input of numbers
x = list()
num = input("Enter how many elements you want:")
print ("Enter numbers in array: ")
for i in range(int(num)):
    n = input("num :")
    x.append(int(n))
print ("ARRAY: ",x)
x.sort()
print("Sorted Array:",x)
n=len(x)

first = 0
last = len(x)-1
midpoint = (first+last)//2
number_to_find=int(input("enter element to be found"))
found=False

#binary search
for i in range(0,n):
    if(x[midpoint]==number_to_find):
        found = True    
    elif x[midpoint]>number_to_find:
        last = midpoint - 1
    else:
        first = midpoint + 1
        
        
if (number_to_find==last):
    print("Element found at position",last)
elif(number_to_find==first):
    print("Element found at position",first)
else:
    print("Not found")

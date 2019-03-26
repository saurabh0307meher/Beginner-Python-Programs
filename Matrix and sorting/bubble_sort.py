arr=[5,1,4,2,8]
print("original array",arr)
n=len(arr)

for i in range(0,n):
    for j in range(i,n):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]

print("sorteddd array",arr)

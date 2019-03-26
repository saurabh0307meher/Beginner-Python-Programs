n = int(input("Enter number Rows for matrix "))

matrix1 = [[0 for i in range(0,n)] for j in range(0,n)]
matrix2 = [[0  for i in range(0,n)] for j in range(0,n)]
add = [[0 for i in range(0,n)] for j in range(0,n)]
multiply = [[0 for i in range(0,n)] for j in range(0,n)]
print(matrix1)
print(matrix2)
for i in range(0,n):
    for j in range(0,n):
        matrix1[i][j]=input()
for i in range(0,n):
    for j in range(0,n):
        matrix2[i][j]=input()
        
for i in range(0,n):
     for j in range(0,n):
         add[i][j] = int(matrix1[i][j]) + int(matrix2[i][j])
        
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            multiply[i][j] += int(matrix1[i][k]) * int(matrix2[k][j])
        
print(matrix1)
print(matrix2)
print("Addition of matices")
print(add)
print("Multiplication of matices")
print(multiply)

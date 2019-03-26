x =[[1,0],
    [0,1]]
y =[[1,2],
    [3,4]]
result =[[0,0],
        [0,0]]


# result[0][0] = x[0][0] * y[0][0] + x[0][1] * y[1][0]
# result[0][1] = x[0][0] * y[0][1] + x[0][1] * y[1][1]
# result[1][0] = x[1][0] * y[0][0] + x[1][1] * y[1][0]
# result[1][1] = x[1][0] * y[1][0] + x[1][1] * y[1][1]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]
            
for r in result:
    print(r)



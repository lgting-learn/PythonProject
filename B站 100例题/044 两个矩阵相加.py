x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]
          ]
for column in range(len(x)):
    for row in range(len(x[0])):
        i, j = column, row
        result[i][j] = x[i][j] + y[i][j]
for i in result:
    print(i)

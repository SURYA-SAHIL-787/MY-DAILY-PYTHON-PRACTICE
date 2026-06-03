matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

for s in range(rows + cols - 1):
    temp = []

    for i in range(rows):
        j = s - i

        if 0 <= j < cols:
            temp.append(matrix[i][j])

    if s % 2 == 0:
        for i in range(len(temp) - 1, -1, -1):
            print(temp[i], end=" ")
    else:
        for i in range(len(temp)):
            print(temp[i], end=" ")
          

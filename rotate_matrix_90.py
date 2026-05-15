def rotate_matrix(matrix):
    n = len(matrix)

    for row in range(n):
        for col in range(row + 1, n):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in range(n):
        matrix[row].reverse()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_matrix(matrix)

for row in matrix:
    print(row)

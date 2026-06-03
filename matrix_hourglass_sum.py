matrix = [
    [1, 2, 3, 0],
    [0, 4, 0, 2],
    [5, 6, 7, 1],
    [0, 8, 0, 3]
]

max_sum = -999999

for i in range(len(matrix) - 2):
    for j in range(len(matrix[0]) - 2):

        total = (
            matrix[i][j] +
            matrix[i][j + 1] +
            matrix[i][j + 2] +
            matrix[i + 1][j + 1] +
            matrix[i + 2][j] +
            matrix[i + 2][j + 1] +
            matrix[i + 2][j + 2]
        )

        if total > max_sum:
            max_sum = total

print(max_sum)

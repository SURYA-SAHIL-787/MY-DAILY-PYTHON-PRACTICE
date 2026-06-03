matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

top = 0
bottom = len(matrix) - 1
left = 0
right = len(matrix[0]) - 1

while top <= bottom and left <= right:
    layer_sum = 0

    for i in range(left, right + 1):
        layer_sum += matrix[top][i]

    for i in range(top + 1, bottom + 1):
        layer_sum += matrix[i][right]

    if top < bottom:
        for i in range(right - 1, left - 1, -1):
            layer_sum += matrix[bottom][i]

    if left < right:
        for i in range(bottom - 1, top, -1):
            layer_sum += matrix[i][left]

    print(layer_sum)

    top += 1
    bottom -= 1
    left += 1
    right -= 1

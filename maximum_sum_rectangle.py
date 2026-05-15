def kadane(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for index in range(1, len(arr)):
        current_sum = max(arr[index], current_sum + arr[index])
        max_sum = max(max_sum, current_sum)

    return max_sum


def maximum_sum_rectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    max_rectangle_sum = float("-inf")

    for left in range(cols):
        temp = [0] * rows

        for right in range(left, cols):
            for row in range(rows):
                temp[row] += matrix[row][right]

            current_sum = kadane(temp)
            max_rectangle_sum = max(max_rectangle_sum, current_sum)

    return max_rectangle_sum


matrix = [
    [1, 2, -1, -4],
    [-8, -3, 4, 2],
    [3, 8, 10, -8],
    [-4, -1, 1, 7]
]

print(maximum_sum_rectangle(matrix))

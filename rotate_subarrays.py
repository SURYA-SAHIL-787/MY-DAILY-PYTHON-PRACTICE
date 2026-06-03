arr = [1, 2, 3, 4, 5, 6]
k = 3

for i in range(0, len(arr) - k + 1):
    last = arr[i + k - 1]

    for j in range(i + k - 1, i, -1):
        arr[j] = arr[j - 1]

    arr[i] = last

print(arr)


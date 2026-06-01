def permutations(arr, index=0):
    if index == len(arr):
        print(arr)
        return

    for i in range(index, len(arr)):
        arr[index], arr[i] = arr[i], arr[index]
        permutations(arr, index + 1)
        arr[index], arr[i] = arr[i], arr[index]


arr = [1, 2, 3]
permutations(arr)

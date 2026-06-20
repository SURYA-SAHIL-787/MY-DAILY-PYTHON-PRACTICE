def find_permutations(arr, index):
    if index == len(arr):
        print(arr)
        return

    for i in range(index, len(arr)):
        arr[index], arr[i] = arr[i], arr[index]

        find_permutations(arr, index + 1)

        arr[index], arr[i] = arr[i], arr[index]


arr = [1, 2, 3]
find_permutations(arr, 0)

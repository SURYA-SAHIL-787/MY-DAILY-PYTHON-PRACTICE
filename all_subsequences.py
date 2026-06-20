def print_subsequences(arr, index, current):
    if index == len(arr):
        print(current)
        return

    # Take the current element
    current.append(arr[index])
    print_subsequences(arr, index + 1, current)

    # Do not take the current element
    current.pop()
    print_subsequences(arr, index + 1, current)


arr = [1, 2, 3]

print_subsequences(arr, 0, [])

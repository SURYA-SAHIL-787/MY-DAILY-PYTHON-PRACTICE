def subset_sum(arr, index, target, current):
    if target == 0:
        print(current)
        return

    if index == len(arr):
        return

    if arr[index] <= target:
        current.append(arr[index])
        subset_sum(arr, index + 1, target - arr[index], current)
        current.pop()

    subset_sum(arr, index + 1, target, current)


arr = [2, 3, 5, 6, 8]
target = 8

subset_sum(arr, 0, target, [])

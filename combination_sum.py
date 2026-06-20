def combination_sum(arr, index, target, current):
    if target == 0:
        print(current)
        return

    if index == len(arr):
        return

    if arr[index] <= target:
        current.append(arr[index])

        # Same index because we can use same element again
        combination_sum(arr, index, target - arr[index], current)

        current.pop()

    # Move to next element
    combination_sum(arr, index + 1, target, current)


arr = [2, 3, 6, 7]
target = 7

combination_sum(arr, 0, target, [])

def subset_sum(arr, target, i=0):
    if target == 0:
        return True
    if i == len(arr):
        return False

    include = subset_sum(arr, target - arr[i], i + 1)
    exclude = subset_sum(arr, target, i + 1)

    return include or exclude


arr = [3, 34, 4, 12, 5, 2]
target = 9

print(subset_sum(arr, target))

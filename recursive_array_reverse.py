def reverse_array(arr, left, right):
    if left >= right:
        return

    arr[left], arr[right] = arr[right], arr[left]
    reverse_array(arr, left + 1, right - 1)


arr = [1, 2, 3, 4, 5]
reverse_array(arr, 0, len(arr) - 1)

print(arr)

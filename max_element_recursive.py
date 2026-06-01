def find_max(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]

    small_answer = find_max(arr, index + 1)
    return max(arr[index], small_answer)


arr = [10, 45, 2, 99, 23]
print(find_max(arr))

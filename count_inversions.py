def merge_and_count(left, right):
    merged = []
    i = j = 0
    count = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, count


def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, left_count = count_inversions(arr[:mid])
    right, right_count = count_inversions(arr[mid:])

    merged, merge_count = merge_and_count(left, right)

    total = left_count + right_count + merge_count
    return merged, total


arr = list(map(int, input("Enter numbers: ").split()))
sorted_arr, inversions = count_inversions(arr)

print("Sorted array:", sorted_arr)
print("Number of inversions:", inversions)

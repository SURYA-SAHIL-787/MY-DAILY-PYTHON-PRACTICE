def search_rotated(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


arr = list(map(int, input("Enter rotated sorted array: ").split()))
target = int(input("Enter target: "))

index = search_rotated(arr, target)

if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")

def has_pair_with_sum(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return True, arr[left], arr[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False, None, None


arr = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))

found, a, b = has_pair_with_sum(arr, target)

if found:
    print("Pair found:", a, b)
else:
    print("No pair found")

def next_greater_elements(arr):
    result = [-1] * len(arr)
    stack = []

    for index in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[index]:
            stack.pop()

        if stack:
            result[index] = stack[-1]

        stack.append(arr[index])

    return result


n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the array elements: ").split()))

if len(arr) != n:
    print("Error: Number of elements does not match n.")
else:
    result = next_greater_elements(arr)
    print("Next greater elements:", result)

def maximum_decrease(arr):
    if len(arr) < 2:
        return 0

    maximum_so_far = arr[0]
    maximum_drop = 0

    for value in arr[1:]:
        current_drop = maximum_so_far - value

        if current_drop > maximum_drop:
            maximum_drop = current_drop

        if value > maximum_so_far:
            maximum_so_far = value

    return maximum_drop


n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the array elements: ").split()))

if len(arr) != n:
    print("Error: Number of elements does not match n.")
else:
    result = maximum_decrease(arr)
    print("Maximum decrease:", result)

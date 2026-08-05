def count_odd_sum_subarrays(arr):
    even_prefix_count = 1
    odd_prefix_count = 0
    prefix_sum = 0
    odd_subarray_count = 0

    for number in arr:
        prefix_sum += number

        if prefix_sum % 2 == 0:
            odd_subarray_count += odd_prefix_count
            even_prefix_count += 1
        else:
            odd_subarray_count += even_prefix_count
            odd_prefix_count += 1

    return odd_subarray_count


n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the array elements: ").split()))

if len(arr) != n:
    print("Error: Number of elements does not match n.")
else:
    result = count_odd_sum_subarrays(arr)
    print("Number of subarrays with an odd sum:", result)

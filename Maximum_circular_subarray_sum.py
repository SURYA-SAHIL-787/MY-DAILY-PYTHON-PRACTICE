def kadane(numbers: list[int]) -> int:
    current = best = numbers[0]

    for number in numbers[1:]:
        current = max(number, current + number)
        best = max(best, current)

    return best


def maximum_circular_sum(numbers: list[int]) -> int:
    normal_maximum = kadane(numbers)

    if normal_maximum < 0:
        return normal_maximum

    total_sum = sum(numbers)
    minimum_subarray_sum = -kadane([-number for number in numbers])

    circular_maximum = total_sum - minimum_subarray_sum

    return max(normal_maximum, circular_maximum)


print(maximum_circular_sum([5, -3, 5]))
# 10

def single_number(nums):
    result = 0

    for number in nums:
        result ^= number

    return result


print(single_number([4, 1, 2, 1, 2]))  # 4

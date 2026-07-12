def product_except_self(numbers: list[int]) -> list[int]:
    length = len(numbers)
    result = [1] * length

    prefix_product = 1
    for index in range(length):
        result[index] = prefix_product
        prefix_product *= numbers[index]

    suffix_product = 1
    for index in range(length - 1, -1, -1):
        result[index] *= suffix_product
        suffix_product *= numbers[index]

    return result


print(product_except_self([1, 2, 3, 4]))
# [24, 12, 8, 6]

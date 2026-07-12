from collections import deque


def sliding_window_maximum(
    numbers: list[int],
    k: int,
) -> list[int]:
    if k <= 0 or k > len(numbers):
        raise ValueError("Invalid window size.")

    indices = deque()
    result = []

    for index, number in enumerate(numbers):
        while indices and indices[0] <= index - k:
            indices.popleft()

        while indices and numbers[indices[-1]] <= number:
            indices.pop()

        indices.append(index)

        if index >= k - 1:
            result.append(numbers[indices[0]])

    return result


print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))
# [3, 3, 5, 5, 6, 7]

import heapq


def find_kth_largest(numbers, k):
    if not numbers:
        raise ValueError("The list cannot be empty.")

    if k < 1 or k > len(numbers):
        raise ValueError("k must be between 1 and the list length.")

    min_heap = []

    for number in numbers:
        heapq.heappush(min_heap, number)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


def main():
    numbers = [12, 3, 5, 7, 19, 26, 4]
    k = 3

    result = find_kth_largest(numbers, k)

    print("Numbers:", numbers)
    print(f"{k}rd largest element:", result)


if __name__ == "__main__":
    main()

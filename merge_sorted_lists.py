import heapq


def merge_sorted_lists(sorted_lists):
    min_heap = []
    merged_list = []

    for list_index, current_list in enumerate(sorted_lists):
        if current_list:
            heapq.heappush(
                min_heap,
                (current_list[0], list_index, 0)
            )

    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(value)

        next_index = element_index + 1

        if next_index < len(sorted_lists[list_index]):
            next_value = sorted_lists[list_index][next_index]

            heapq.heappush(
                min_heap,
                (next_value, list_index, next_index)
            )

    return merged_list


def main():
    sorted_lists = [
        [1, 4, 7, 10],
        [2, 5, 8, 11],
        [3, 6, 9, 12]
    ]

    result = merge_sorted_lists(sorted_lists)

    print("Input lists:")

    for current_list in sorted_lists:
        print(current_list)

    print("Merged list:")
    print(result)


if __name__ == "__main__":
    main()

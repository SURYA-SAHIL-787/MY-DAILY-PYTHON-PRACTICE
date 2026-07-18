from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = None


def build_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def to_list(head: Optional[ListNode]) -> list[int]:
    result = []

    while head is not None:
        result.append(head.val)
        head = head.next

    return result


def merge_single_occurrences(
    list1: Optional[ListNode],
    list2: Optional[ListNode]
) -> Optional[ListNode]:

    dummy = ListNode(0)
    tail = dummy

    left = list1
    right = list2

    while left is not None or right is not None:

        if right is None or (
            left is not None and left.val < right.val
        ):
            value = left.val

        elif left is None or right.val < left.val:
            value = right.val

        else:
            value = left.val

        frequency = 0

        while left is not None and left.val == value:
            frequency += 1
            left = left.next

        while right is not None and right.val == value:
            frequency += 1
            right = right.next

        if frequency == 1:
            tail.next = ListNode(value)
            tail = tail.next

    return dummy.next


list1 = build_list([1, 2, 2, 5])
list2 = build_list([2, 3, 5, 7])

result = merge_single_occurrences(list1, list2)

print(to_list(result))
# Output: [1, 3, 7]

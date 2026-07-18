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


def remove_every_nth_from_end(
    head: Optional[ListNode],
    n: int
) -> Optional[ListNode]:

    if n <= 0:
        raise ValueError("n must be positive")

    length = 0
    current = head

    while current is not None:
        length += 1
        current = current.next

    dummy = ListNode(0, head)

    previous = dummy
    current = head
    position_from_start = 1

    while current is not None:
        position_from_end = length - position_from_start + 1

        if position_from_end % n == 0:
            previous.next = current.next
        else:
            previous = current

        current = current.next
        position_from_start += 1

    return dummy.next


head = build_list([1, 2, 3, 4, 5, 6, 7])
result = remove_every_nth_from_end(head, 3)

print(to_list(result))
# Output: [1, 3, 4, 6, 7]

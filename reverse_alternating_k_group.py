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


def reverse_alternating_k_group(
    head: Optional[ListNode],
    k: int
) -> Optional[ListNode]:

    if k <= 0:
        raise ValueError("k must be positive")

    if head is None or k == 1:
        return head

    dummy = ListNode(0, head)
    previous_group_tail = dummy
    reverse_group = True

    while True:
        kth_node = previous_group_tail

        for _ in range(k):
            kth_node = kth_node.next

            if kth_node is None:
                return dummy.next

        next_group_head = kth_node.next
        group_head = previous_group_tail.next

        if reverse_group:
            previous = next_group_head
            current = group_head

            while current is not next_group_head:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node

            previous_group_tail.next = kth_node
            previous_group_tail = group_head

        else:
            previous_group_tail = kth_node

        reverse_group = not reverse_group


head = build_list([1, 2, 3, 4, 5, 6, 7, 8])
result = reverse_alternating_k_group(head, 2)

print(to_list(result))
# Output: [2, 1, 3, 4, 6, 5, 7, 8]

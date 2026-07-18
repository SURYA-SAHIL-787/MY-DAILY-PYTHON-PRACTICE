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


def is_palindrome_after_one_deletion(
    head: Optional[ListNode]
) -> bool:

    values = []
    current = head

    while current is not None:
        values.append(current.val)
        current = current.next

    def is_palindrome_range(left: int, right: int) -> bool:
        while left < right:

            if values[left] != values[right]:
                return False

            left += 1
            right -= 1

        return True

    left = 0
    right = len(values) - 1

    while left < right:

        if values[left] == values[right]:
            left += 1
            right -= 1

        else:
            delete_left = is_palindrome_range(left + 1, right)
            delete_right = is_palindrome_range(left, right - 1)

            return delete_left or delete_right

    return True


head = build_list([1, 2, 3, 2, 2, 1])

print(is_palindrome_after_one_deletion(head))
# Output: True

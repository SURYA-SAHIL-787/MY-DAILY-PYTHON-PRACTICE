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


def get_digits(head: Optional[ListNode]) -> list[int]:
    digits = []

    while head is not None:

        if head.val < 0 or head.val > 9:
            raise ValueError(
                "Each node must contain a digit from 0 to 9"
            )

        digits.append(head.val)
        head = head.next

    return digits if digits else [0]


def remove_leading_zeroes(digits: list[int]) -> list[int]:
    index = 0

    while index < len(digits) - 1 and digits[index] == 0:
        index += 1

    return digits[index:]


def absolute_difference(
    number1: Optional[ListNode],
    number2: Optional[ListNode]
) -> Optional[ListNode]:

    first = remove_leading_zeroes(get_digits(number1))
    second = remove_leading_zeroes(get_digits(number2))

    if (len(first), first) < (len(second), second):
        first, second = second, first

    first_index = len(first) - 1
    second_index = len(second) - 1

    borrow = 0
    reversed_result = []

    while first_index >= 0:
        upper_digit = first[first_index] - borrow

        if second_index >= 0:
            lower_digit = second[second_index]
        else:
            lower_digit = 0

        if upper_digit < lower_digit:
            upper_digit += 10
            borrow = 1
        else:
            borrow = 0

        reversed_result.append(upper_digit - lower_digit)

        first_index -= 1
        second_index -= 1

    while (
        len(reversed_result) > 1
        and reversed_result[-1] == 0
    ):
        reversed_result.pop()

    reversed_result.reverse()

    return build_list(reversed_result)


number1 = build_list([7, 2, 4, 3])
number2 = build_list([5, 6, 4])

result = absolute_difference(number1, number2)

print(to_list(result))
# Output: [6, 6, 7, 9]

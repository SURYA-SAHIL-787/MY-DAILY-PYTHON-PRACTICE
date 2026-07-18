from dataclasses import dataclass
from typing import Optional


@dataclass(eq=False)
class ListNode:
    val: int
    next: Optional["ListNode"] = None


def get_length(head: Optional[ListNode]) -> int:
    length = 0

    while head is not None:
        length += 1
        head = head.next

    return length


def intersection_with_distances(
    head_a: Optional[ListNode],
    head_b: Optional[ListNode]
) -> tuple[Optional[ListNode], int, int]:

    length_a = get_length(head_a)
    length_b = get_length(head_b)

    current_a = head_a
    current_b = head_b

    distance_a = 0
    distance_b = 0

    if length_a > length_b:

        for _ in range(length_a - length_b):
            current_a = current_a.next
            distance_a += 1

    elif length_b > length_a:

        for _ in range(length_b - length_a):
            current_b = current_b.next
            distance_b += 1

    while current_a is not current_b:
        current_a = current_a.next
        current_b = current_b.next

        distance_a += 1
        distance_b += 1

    if current_a is None:
        return None, length_a, length_b

    return current_a, distance_a, distance_b


shared1 = ListNode(8)
shared2 = ListNode(9)
shared3 = ListNode(10)

shared1.next = shared2
shared2.next = shared3

head_a = ListNode(1)
head_a.next = ListNode(2)
head_a.next.next = ListNode(3)
head_a.next.next.next = shared1

head_b = ListNode(4)
head_b.next = ListNode(5)
head_b.next.next = shared1

intersection, distance_a, distance_b = intersection_with_distances(
    head_a,
    head_b
)

if intersection is not None:
    print("Intersection value:", intersection.val)
    print("Distance from list A:", distance_a)
    print("Distance from list B:", distance_b)
else:
    print("No intersection")

# Output:
# Intersection value: 8
# Distance from list A: 3
# Distance from list B: 2

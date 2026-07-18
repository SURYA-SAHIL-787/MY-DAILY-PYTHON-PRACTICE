from dataclasses import dataclass
from typing import Optional


@dataclass(eq=False)
class ListNode:
    val: int
    next: Optional["ListNode"] = None


def cycle_entry_and_length(
    head: Optional[ListNode]
) -> tuple[Optional[ListNode], int]:

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            cycle_length = 1
            current = slow.next

            while current is not slow:
                cycle_length += 1
                current = current.next

            cycle_entry = head
            meeting_node = slow

            while cycle_entry is not meeting_node:
                cycle_entry = cycle_entry.next
                meeting_node = meeting_node.next

            return cycle_entry, cycle_length

    return None, 0


node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)
node4 = ListNode(40)
node5 = ListNode(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3

entry, length = cycle_entry_and_length(node1)

if entry is not None:
    print("Cycle entry:", entry.val)
    print("Cycle length:", length)
else:
    print("No cycle")

# Output:
# Cycle entry: 30
# Cycle length: 3

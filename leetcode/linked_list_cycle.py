"""
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list
has a cycle in it.
There is a cycle in a linked list if there is some node in the list
that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's
next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise,
return false.

Example:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail
connects to the 1st node (0-indexed).
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        current = head
        while current:
            if current not in s:
                s.add(current)
            else:
                return True
            current = current.next
        return False


def test_solution(head, result):
    solution = Solution.hasCycle(Solution, head)
    assert solution == result, \
        "Wrong answer {}, should be {}".format(solution, result)
    return "assepted - {} equal to {}".format(solution, result)


# Create cycled linked list
ln3 = ListNode(-4, None)
ln2 = ListNode(0, ln3)
ln1 = ListNode(2, ln2)
ln0 = ListNode(3, ln1)
ln3.next = ln1
print("Test #1: " + test_solution(ln0, True))

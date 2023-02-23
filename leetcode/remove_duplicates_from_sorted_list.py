"""
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates
such that each element appears only once.
Return the linked list sorted as well.

Example:

Input: head = [1,1,2]
Output: [1,2]
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current:
            while current.next and current.next.val == current.val:
                current.next = current.next.next
            current = current.next
        return head


def test_solution(head, result):
    solution = Solution.deleteDuplicates(Solution, head)
    sol, res = "", ""
    while solution:
        sol += str(solution.val)
        solution = solution.next
    while result:
        res += str(result.val)
        result = result.next
    assert sol == res, \
        "Wrong answer {}, should be {}".format(sol, res)
    return "assepted - {} equal to {}".format(sol, res)


print("Test #1: " + test_solution(
    ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(3, None))))),
    ListNode(1, ListNode(2, ListNode(3, None))))
)

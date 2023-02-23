"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list,
and return the reversed list.

Example:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(
        self,
        head: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr = head
        first = None
        while curr:
            temp = curr.next
            curr.next = first
            first = curr
            curr = temp
        return first


def test_solution(head, result):
    solution = Solution.reverseList(Solution, head)
    sol, res = "", ""
    while solution:
        sol += str(solution.val)
        solution = solution.next
    while result:
        res += str(result.val)
        result = result.next
    assert solution == result, \
        "Wrong answer {}, should be {}".format(sol, res)
    return "assepted - {} equal to {}".format(sol, res)


print("Test #1: " + test_solution(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))),
    ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1, None))))),
))

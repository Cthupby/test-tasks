"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their
nodes contains a single digit. Add the two numbers and return the sum
as a linked list.
You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1_list, l2_list = "", ""
        while l1 or l2:
            l1_list += str(l1.val) if l1 else '0'
            l2_list += str(l2.val) if l2 else '0'
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        sum_l = str(int(l1_list[::-1]) + int(l2_list[::-1]))
        result_list = [int(i) for i in sum_l]
        result = None
        for n in result_list:
            result = ListNode(n, result)
        return result


def test_solution(l1, l2, result):
    solution = Solution.addTwoNumbers(Solution, l1, l2)
    sol = ""
    res = ""
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
    ListNode(2, ListNode(4, ListNode(3, None))),
    ListNode(5, ListNode(6, ListNode(4, None))),
    ListNode(7, ListNode(0, ListNode(8, None))))
)

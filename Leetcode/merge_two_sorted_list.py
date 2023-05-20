"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made
 by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""
from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result_list = []
        while list1:
            result_list.append(list1.val)
            list1 = list1.next
        while list2:
            result_list.append(list2.val)
            list2 = list2.next

        sorted_result = sorted(result_list)
        result = None
        for i in sorted_result[::-1]:
            result = ListNode(i, result)
        return result


def test_solution(list1, list2, result):
    solution = Solution.mergeTwoLists(Solution, list1, list2)
    sol, res = "", ""
    while solution:
        sol += str(solution.val)
        solution = solution.next
    while result:
        res += str(result.val)
        result = result.next
    if sol != res:
        assert solution == result, \
            "Wrong answer {}, should be {}".format(sol, res)
    return "assepted - {} equal to {}".format(solution, result)


print("Test #1: " + test_solution(
    ListNode(1, ListNode(2, ListNode(4, None))),
    ListNode(1, ListNode(3, ListNode(4, None))),
    ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(
        4,
        ListNode(4, None))))))
    )
)

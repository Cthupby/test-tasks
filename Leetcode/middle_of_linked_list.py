"""
876. Middle of the Linked List

Given the head of a singly linked list, return the middle
node of the linked list.

If there are two middle nodes, return the second middle node.

Example:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        h = head
        n = 0
        while h:
            n += 1
            h = h.next
        result = head
        for i in range(n // 2):
            result = result.next
        return result


def test_solution(head, result):
    solution = Solution.middleNode(Solution, head)
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
    ListNode(3, ListNode(4, ListNode(5, None))),
))

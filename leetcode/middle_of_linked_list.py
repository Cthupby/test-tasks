"""
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

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
        l = 0
        while h:
            l += 1
            h = h.next
        result = head
        for i in range(l // 2):
            result = result.next
        return result


def test_solution(head, result):
    solution = Solution.middleNode(Solution, head)
    while solution:
        if solution.val != result.val:
            assert solution == result, \
                "Wrong answer {}, should be {}".format(solution, result)
        solution, result = solution.next, result.next
    return "assepted - {} equal to {}".format(solution, result)


print("Test #1: " + test_solution(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), ListNode(3, ListNode(4, ListNode(5, None)))))

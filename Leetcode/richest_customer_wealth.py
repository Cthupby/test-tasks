"""
1672. Richest Customer Wealth

You are given an m x n integer grid accounts where accounts[i][j] is the amount
of money the i...th​customer has in the j...th​bank. Return the wealth that
the richest customer has.

A customer's wealth is the amount of money they have in all their bank
accounts.
The richest customer is the customer that has the maximum wealth.

Example:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
"""
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])


def test_solution(accounts, result):
    solution = Solution.maximumWealth(Solution, accounts)
    assert solution == result, \
        "Wrong answer {}, should be {}".format(solution, result)
    return "assepted - {} equal to {}".format(solution, result)


print("Test #1: " + test_solution([[1, 2, 3], [3, 2, 1]], 6))
print("Test #2: " + test_solution([[1, 5], [7, 3], [3, 5]], 10))
print("Test #3: " + test_solution([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17))

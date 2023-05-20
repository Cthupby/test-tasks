"""
1497. Check If Array Pairs Are Divisible by k

Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that
the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.

Example:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
"""
from collections import defaultdict


class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        hash_map = defaultdict(int)
        count = 0

        for i in arr:
            temp = i % k
            if temp == 0:
                count += 1
            elif k - temp in hash_map and hash_map[k - temp] != 0:
                count += 2
                hash_map[k - temp] -= 1
            else:
                hash_map[temp] += 1
        return count == len(arr)


def test_solution(arr, k, result):
    solution = Solution.canArrange(Solution, arr, k)
    assert solution == result, \
        "Wrong answer {}, should be {}".format(solution, result)
    return "assepted - {} equal to {}".format(solution, result)


print("Test #1: " + test_solution([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5, True))
print("Test #2: " + test_solution([1, 2, 3, 4, 5, 6], 7, True))
print("Test #3: " + test_solution([1, 2, 3, 4, 5, 6], 10, False))

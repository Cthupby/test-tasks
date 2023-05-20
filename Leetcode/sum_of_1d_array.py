"""
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as
runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        i = 0
        result = []
        for v in nums:
            i += v
            result.append(i)
        return result


def test_solution(nums, result):
    solution = Solution.runningSum(Solution, nums)
    assert solution == result, \
        "Wrong answer {}, should be {}".format(solution, result)
    return "assepted - {} equal to {}".format(solution, result)


print("Test #1: " + test_solution([1, 2, 3, 4], [1, 3, 6, 10]))
print("Test #2: " + test_solution([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]))
print("Test #3: " + test_solution([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]))

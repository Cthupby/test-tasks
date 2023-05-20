"""
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote
can be constructed by using the letters from magazine and false
otherwise.
Each letter in magazine can only be used once in ransomNote.

Example:

Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = Counter(ransomNote)
        mag = Counter(magazine)
        for k, v in note.items():
            if k not in mag:
                return False
            elif mag[k] < v:
                return False
        return True


def test_solution(ransomNote, magazine, result):
    solution = Solution.canConstruct(Solution, ransomNote, magazine)
    assert solution == result, \
        "Wrong answer {}, should be {}".format(solution, result)
    return "assepted - {} equal to {}".format(solution, result)


print("Test #1: " + test_solution("a", "b", False))
print("Test #2: " + test_solution("aa", "ab", False))
print("Test #3: " + test_solution("aa", "aab", True))

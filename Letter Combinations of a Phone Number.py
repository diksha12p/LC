"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
from typing import List


class Solution:
    def __init__(self):
        self.KEYBOARD = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
                         "9": "wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        result = []
        self.dfs(digits, 0, "", result)
        return result

    def dfs(self, digits, idx, path, result):
        if len(path) == len(digits):
            result.append(path)
            return
        for char in self.KEYBOARD[digits[idx]]:
            self.dfs(digits, idx + 1, path + char, result)


if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCombinations('23'))

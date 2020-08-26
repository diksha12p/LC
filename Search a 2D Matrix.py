"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            mid_ele = matrix[mid // cols][mid % cols]
            if mid_ele == target:
                return True
            elif mid_ele > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    sol = Solution()
    arr = [[1,   3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]]
    assert (sol.searchMatrix(arr, 13)) is False
    assert (sol.searchMatrix(arr, 11)) is True

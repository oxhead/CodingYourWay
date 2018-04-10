"""
https://leetcode.com/problems/search-a-2d-matrix

Related:
  - lt_240_search-a-2d-matrix-ii
"""

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

Given target = 3, return true.
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Time: O(log(m*n))
        # Space: O(1)
        num_rows = len(matrix) if matrix else -1
        num_cols = len(matrix[0]) if num_rows >= 1 else -1
        if num_rows < 1 or num_cols < 1: return False
        left, right = 0, num_rows * num_cols - 1
        while left <= right:
            mid = left + (right - left) // 2
            val = matrix[mid//num_cols][mid%num_cols]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix_v2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def to_coordinate(num_rows, num_cols, index):
            i = index // num_cols
            j = index - i * num_cols
            return i, j
        num_rows = len(matrix) if matrix else -1
        num_cols = len(matrix[0]) if num_rows >= 1 else -1
        if num_rows < 1 or num_cols < 1: return False
        left = 0
        right = num_rows * num_cols - 1
        while left <= right:
            mid = (left + right) >> 1
            i, j = to_coordinate(num_rows, num_cols, mid)
            if matrix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid - 1
            else: return True
        return False


if __name__ == '__main__':
    test_cases = [
        (([], 0), False),
        (([[1],[3]], 0), False),
        (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3), True),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().searchMatrix(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


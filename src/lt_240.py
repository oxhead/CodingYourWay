"""
https://leetcode.com/problems/search-a-2d-matrix-ii

Related:
  - lt_74_search-a-2d-matrix
"""

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Time: O(mlogn)
        # Space: O(1)
        m = len(matrix) if matrix else -1
        n = len(matrix[0]) if m > 0 else -1
        if m < 1 or n < 1: return False

        for row in range(m):
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) >> 1
                if matrix[row][mid] < target: left = mid + 1
                elif matrix[row][mid] > target: right = mid -1
                else: return True

        return False

    def searchMatrix_v2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Time: O(m + n)
        # Space: O(1)
        m = len(matrix) if matrix else -1
        n = len(matrix[0]) if m > 0 else -1
        if m < 1 or n < 1: return False
        i, j = m - 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] == target: return True
            elif matrix[i][j] > target: i -= 1
            else: j += 1
        return False


if __name__ == '__main__':
    test_cases = [
        (([], 0), False),
        (([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5), True),
        (([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20), False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().searchMatrix(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


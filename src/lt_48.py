"""
https://leetcode.com/problems/rotate-image

Related:
"""

"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # Time: O(n^2)
        # Space: O(1)
        # Hints:
        # 1) 90 degree: transpose + flip alone the central vertical line
        # 2) 180 degree: flip alone the central vertial line + flip alone the central horizontal line
        # 3) 270 degree: transpose + flip alone the central horizontal line
        # Examples:
        #  1 2 3
        #  4 5 6
        #  7 8 9
        # TRANSPOSE
        #  1 4 7
        #  2 5 8
        #  3 6 9
        # FLIP (along the central vertial line 4-5-6
        #  7 4 1
        #  8 5 2
        #  9 6 3
        n = len(matrix[0])
        # transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # flip along the vertial line
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n-j-1], matrix[i][j]

    def rotate_v2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # transpose
        for i in range(n - 1):
            for j in range(n - i):
                matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]
        # flip vertically
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]

    def rotate_fourway(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in range(n // 2):
            for col in range(row, n - row - 1):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[n - 1 - col][row]
                matrix[n - 1 - col][row] = matrix[n - 1 - row][n - 1 - col]
                matrix[n - 1 - row][n - 1 - col] = matrix[col][n - 1 - row]
                matrix[col][n - 1 - row] = tmp


if __name__ == '__main__':
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]], [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        matrix = test_case[0]
        Solution().rotate(matrix)
        #Solution().rotate_fourway(matrix)
        print('output:', matrix)
        assert matrix == test_case[1]


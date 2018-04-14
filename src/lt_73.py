"""
https://leetcode.com/problems/set-matrix-zeroes

Related:
  - lt_289_game-of-life
"""

"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.
Follow up:

Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # Time: O(m * n)
        # Space: O(1)
        # http://www.cnblogs.com/higerzhang/p/4099114.html
        row, col = -1, -1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row, col = i, j

        if row == -1 or col == -1: return

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][col] = 0
                    matrix[row][j] = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i != row and j != col:
                    if matrix[i][col] == 0 or matrix[row][j] == 0:
                        matrix[i][j] = 0

        for i in range(len(matrix)):
            matrix[i][col] = 0
        for j in range(len(matrix[0])):
            matrix[row][j] = 0

    def setZeroes_v2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix)):
                        if k != i and matrix[k][j] != 0:
                            matrix[k][j] = None
                    for k in range(len(matrix[i])):
                        if k != j and matrix[i][k] != 0:
                            matrix[i][k] = None
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j]:
                    matrix[i][j] = 0


if __name__ == '__main__':
    test_cases = [
        ([], []),
        ([[0]], [[0]]),
        ([[0],[1]], [[0],[0]]),
        ([[0, 1], [1, 1]], [[0, 0], [0, 1]]),
        ([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]], [[0,0,0,0],[0,0,0,4],[0,0,0,0],[0,0,0,3],[0,0,0,0]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        matrix = test_case[0]
        Solution().setZeroes(matrix)
        print('output:', matrix)
        assert matrix == test_case[1]

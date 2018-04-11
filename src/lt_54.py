"""
https://leetcode.com/problems/spiral-matrix

Related:
  - lt_59_spiral-matrix-ii
"""

"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

You should return [1,2,3,6,9,8,7,4,5].
"""

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Time: O(m * n)
        # Space: O(1)
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0: return []
        output = []
        left, right, up, down = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left <= right and up <= down:
            for j in range(left, right + 1):
                output.append(matrix[up][j])
            for i in range(up + 1, down + 1):
                output.append(matrix[i][right])
            for j in range(right - 1, left - 1, -1):
                if up < down:
                    output.append(matrix[down][j])
            for i in range(down - 1, up, -1):
                if left < right:
                    output.append(matrix[i][left])
            left += 1
            right -= 1
            up += 1
            down -= 1
        return output


if __name__ == '__main__':
    test_cases = [
        ([[2, 3]], [2, 3]),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().spiralOrder(test_case[0])
        print('output:', output)
        assert output == test_case[1]

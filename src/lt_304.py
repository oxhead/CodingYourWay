"""
https://leetcode.com/problems/range-sum-query-2d-immutable

Related:
  - lt_303_range-sum-query-immutable
  - lt_308_range-sum-query-2d-mutable
"""

"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:

    You may assume that the matrix does not change.
    There are many calls to sumRegion function.
    You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

class NumMatrix:

    # http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-304-range-sum-query-2d-immutable/
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # Time: O(m * n)
        # Space: O(m * n)
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        self.cum_sums = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.cum_sums[i][j] = matrix[i - 1][j - 1] + self.cum_sums[i - 1][j] + self.cum_sums[i][j - 1] - self.cum_sums[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # Time: O(1)
        return self.cum_sums[row2+1][col2+1] - self.cum_sums[row2+1][col1] - self.cum_sums[row1][col2+1] + self.cum_sums[row1][col1] 
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


if __name__ == '__main__':
    test_cases = [
        (([[]], []), []),
        (([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]], [(2, 1, 4, 3), (1, 1, 2, 2), (1, 2, 2, 4)]), [8, 11, 12]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        obj = NumMatrix(test_case[0][0])
        for index_pair, expected_result in zip(test_case[0][1], test_case[1]):
            output = obj.sumRegion(*index_pair)
            print('output:', index_pair, output)
            assert output == expected_result


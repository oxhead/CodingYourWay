"""
https://leetcode.com/problems/maximal-square

Related:
  - lt_85_maximal-rectangle
  - lt_764_largest-plus-sign
"""

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4.
"""

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # Time: O(m * n)
        # Space: O(m * n) 
        # http://www.cnblogs.com/thoupin/p/4780352.html
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0: return 0
        dp = []
        for row in matrix:
            dp.append([int(n) for n in row])
        max_n = 0
        max_n = max(dp[0] + [dp[i][0] for i in range(len(dp))])
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if dp[i][j]:
                    dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + dp[i][j]
                max_n = max(max_n, dp[i][j])
        return max_n ** 2
        

    def maximalSquare_failed(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0: return 0
        dp = [[(0, 0) for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        dp[0][0] = (int(matrix[0][0]), int(matrix[0][0]))
        for i in range(1, len(matrix)):
            if matrix[i][0] == "1":
                dp[i][0] = (1, dp[i-1][0][1] + 1)
        max_square = max([dp[i][0][0] for i in range(len(matrix))])
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == "1":
                dp[0][j] = (dp[0][j-1][0] + 1, 1)
        max_square = max([dp[0][j][1] for j in range(len(matrix[0]))])
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == "1":
                    dp[i][j] = (dp[i][j-1][0] + 1, dp[i-1][j][1] + 1)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # m, n = dp[i][j][1], dp[i][j][0]
                n = min(dp[i][j])
                m = 0
                record = (n, n)
                for k in range(n):
                    if dp[i-k][j-k] >= record:
                        m += 1
                        record = (record[0] - 1, record[1] - 1)
                    else:
                        break
                max_square = max(max_square, m * m)
        return max_square


if __name__ == '__main__':
    test_cases = [
        ([], 0),
        ([["1"]], 1),
        ([["1", "1"]], 1),
        ([["1","1"],["1","1"]], 4),
        ([["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]], 9),
        ([["0","0","0","0","0"],["1","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]], 1),
        ([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]], 4),
        ([["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],["0","1","1","1","1","1"],["1","1","0","1","1","1"]], 4),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().maximalSquare(test_case[0])
        print('output:', output)
        assert output == test_case[1]


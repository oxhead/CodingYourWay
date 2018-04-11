"""
https://leetcode.com/problems/spiral-matrix-ii

Related:
  - lt_54_spiral-matrix
"""

"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:

[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # Time: O(n^2)
        # Space: O(1)
        output = [[0] * n for _ in range(n)]
        left, right, up, down = 0, n - 1, 0, n - 1
        count = 1
        while left <= right and up <= down:
            for j in range(left, right + 1):
                output[up][j] = count
                count += 1 
            for i in range(up + 1, down):
                output[i][right] = count
                count += 1
            for j in range(right, left, -1):
                output[down][j] = count
                count += 1
            for i in range(down, up, -1):
                output[i][left] = count
                count += 1
            left += 1
            right -= 1
            up += 1
            down -= 1
        return output
        
    def generateMatrix_verbose(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        output = [[0] * n for _ in range(n)]
        i, j = 0, 0
        direction = 'right'
        count = 0
        while count < n*n:
            count += 1
            output[i][j] = count
            if direction == 'right':
                if j < n - 1 and output[i][j+1] == 0:
                    j += 1
                else:
                    i += 1
                    direction = 'down'
            elif direction == 'down':
                if i < n -1 and output[i+1][j] == 0:
                    i += 1
                else:
                    j -= 1
                    direction = 'left'
            elif direction == 'left':
                if j > 0 and output[i][j-1] == 0:
                    j -= 1
                else:
                    i -= 1
                    direction = 'up'
            else:
                if i > 0 and output[i-1][j] == 0:
                    i -= 1
                else:
                    j += 1
                    direction = 'right'
        return output
        

if __name__ == '__main__':
    test_cases = [
        (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().generateMatrix(test_case[0])
        print('output:', output)
        assert output == test_case[1]

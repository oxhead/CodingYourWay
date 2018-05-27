"""
https://leetcode.com/problems/magic-squares-in-grid
"""

"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an N x N grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

 

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.

Note:

    1 <= grid.length = grid[0].length <= 10
    0 <= grid[i][j] <= 15
"""

class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def check_valid(a, b):
            for i in range(a, a+3):
                for j in range(b, b+3):
                    if grid[i][j] <= 0 or grid[i][j] >= 10: return False
            return True
            
        def is_magic_square(a, b):
            if not check_valid(a, b): return False
            s = sum(grid[a][b:b+3])
            for m in range(a, a + 3):
                if sum([x for x in grid[m][b:b+3]]) != s: return False
            for n in range(b, b + 3):
                if sum([x[n] for x in grid[a:a+3]]) != s: return False
            
            if sum([grid[a+i][b+i] for i in range(3)]) != s: return False
            if sum([grid[a+2-i][b+i] for i in range(3)]) != s: return False 
            return True
        m = len(grid) if grid else - 1
        n = len(grid[0]) if m > 0 else -1
        if m < 3 or n < 3: return 0
        total = 0
        a = 0
        while a + 3 <= m:
            b = 0
            while b + 3 <= n:
                if is_magic_square(a, b): total += 1
                b += 1
            a += 1
        return total
        

if __name__ == '__main__':
    test_cases = [
        ([[4,3,8,4], [9,5,1,9], [2,7,6,2]], 1),
        ([[10,3,5],[1,6,11],[7,9,2]], 0),
        ([[2,7,6,9],[9,5,1,6],[4,3,8,8],[1,4,10,1]], 1),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().numMagicSquaresInside(test_case[0])
        print('output:', output)
        assert output == test_case[1]

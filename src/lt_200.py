"""
https://leetcode.com/problems/number-of-islands

Related:
  - lt_130
  - lt_286
  - lt_305
  - lt_323
  - lt_694
  - lt_695

Complexity:
  - Time:
  - Space:
"""

"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000

Answer: 1

Example 2:

11000
11000
00100
00011

Answer: 3
"""

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j):
            grid[i][j] = WATER
            if i + 1 < len(grid) and grid[i+1][j] == LAND:
                dfs(i + 1, j)
            if j + 1 < len(grid[0]) and grid[i][j + 1] == LAND:
                dfs(i, j + 1)
            if i - 1 >= 0 and grid[i - 1][j] == LAND:
                dfs(i - 1, j)
            if j - 1 >= 0 and grid[i][j - 1] == LAND:
                dfs(i, j - 1)
        if not grid or len(grid) == 0 or len(grid[0]) == 0: return 0
        WATER, LAND = '0', '1'
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == LAND:
                    dfs(i, j) 
                    count += 1
        return count
        
    def numIslands_dfs(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleMedium/200.html
        def dfs(i, j):
            if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])): return
            if visited[i][j] or grid[i][j] != LAND: return
            visited[i][j] = True
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)

        if not grid or len(grid) == 0 or len(grid[0]) == 0: return 0
        LAND = '1'
        count = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == LAND:
                    dfs(i, j)
                    count += 1
        return count

    def numIslands_fail(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # failed attempt
        if not grid or len(grid) == 0: return 0
        WATER = '0'
        LAND = '1'
        count = 0
        for row in grid:
            previous = 0
            for i in range(len(row)):
                if row[i] == LAND and previous != row[i]:
                    count += 1
                previous = row[i]
        for i in range(1, len(grid)):
            row = grid[i]
            left = right = 0
            while left < len(row):
                while left < len(row) and row[left] != LAND:
                    left += 1
                if left >= len(row): break
                right = left + 1
                while right < len(row) and row[left] == row[right]:
                    right += 1
                right -= 1

                for j in range(left, right+1):
                    if grid[i-1][j] == LAND:
                        count -= 1
                        break
                left = right + 1
        return count


if __name__ == '__main__':
    test_cases = [
        ([['1']], 1),
        ([['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']], 1),
        ([['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']], 3),
        ([['1', '0', '1', '1', '1'], ['1', '0', '1', '0', '1'], ['1', '1', '1', '0', '1']], 1),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().numIslands(test_case[0])
        print('output:', output)
        assert output == test_case[1]


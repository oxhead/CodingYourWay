"""
https://leetcode.com/problems/number-of-islands

Related:
  - lt_130_surrounded-regions
  - lt_286_walls-and-gates
  - lt_305_number-of-islands-ii
  - lt_323_number-of-connected-components-in-an-undirected-graph
  - lt_694_number-of-distinct-islands
  - lt_695_max-area-of-island
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

import collections

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Time: O(m*n)
        # Space: O(m*n), call stack
        # Hints:
        # 1) DFS
        def search(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1'): return 0
            grid[i][j] = 0
            count = 1
            for a, b in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                count += search(a, b)
            return count
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if search(i, j) > 0: count += 1
        return count

    def numIslands_v2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # https://www.tangjikai.com/algorithms/leetcode-200-number-of-islands
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

    def numIslands_v2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        stack = []
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != "1": continue
                count += 1
                stack.append((i, j))
                while stack:
                    m, n = stack.pop() 
                    if grid[m][n] != "1": continue
                    grid[m][n] = "0"
                    if m < len(grid) - 1 and grid[m + 1][n] == "1":
                        stack.append((m + 1, n))
                    if n < len(grid[m]) - 1 and grid[m][n + 1] == "1":
                        stack.append((m, n + 1))
                    if m > 0 and grid[m - 1][n] == "1":
                        stack.append((m - 1, n))
                    if n > 0 and grid[m][n - 1] == "1":
                        stack.append((m, n - 1))
        return count

    def numIslands_bfs(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Time: O(m * n)
        # Space: (m * n)
        # Hints:
        # 1) BFS
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0': continue
                count += 1
                grid[i][j] = '0'
                queue = collections.deque([(i, j)])
                while queue:
                    a, b = queue.popleft()
                    for r, c in (a-1, b), (a+1, b), (a, b-1), (a, b+1):
                        if not (0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] == '1'): continue 
                        queue.append((r, c))
                        grid[r][c] = '0'
        return count

    def numIslands_unionfind(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Time: O(m * n)
        # Space: O(m * n)
        # Hints:
        # 1) Union find
        # Notice:
        # 1) I didn't initialize self.count to the number of 1s; instead, I count how many union operations
        # 2) Substract the number of union operations from the number of 1s = the number of connected components
        class UnionFind:
            def __init__(self, n):
                self.set = list(range(n))
                self.count = 0

            def find_set(self, x):
                if self.set[x] != x:
                    self.set[x] = self.find_set(self.set[x])
                return self.set[x]

            def union_set(self, x, y):
                x_root, y_root = map(self.find_set, (x, y))
                if x_root != y_root:
                    self.set[min(x_root, y_root)] = max(x_root, y_root)
                    self.count += 1

        if not any(grid): return 0
        num_1s = sum(sum(list(map(int, row))) for row in grid)
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0': continue
                for a, b in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                    if not ( 0 <= a < m and 0 <= b < n and grid[a][b] == '1'): continue
                    uf.union_set(i * n + j, a * n + b)
        return num_1s - uf.count


if __name__ == '__main__':
    test_cases = [
        ([['1']], 1),
        ([["1", "1", "1"],["0", "1", "0"],["0", "1", "0"]], 1),
        ([['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']], 1),
        ([['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']], 3),
        ([['1', '0', '1', '1', '1'], ['1', '0', '1', '0', '1'], ['1', '1', '1', '0', '1']], 1),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().numIslands(test_case[0])
        print('output:', output)
        assert output == test_case[1]


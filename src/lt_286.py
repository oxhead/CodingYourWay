"""
https://leetcode.com/problems/walls-and-gates

Related:
  - lt_130_surrounded-regions
  - lt_200_number-of-islands
  - lt_317_shortest-distance-from-all-buildings
"""

"""
You are given a m x n 2D grid initialized with these three possible values.

    -1 - A wall or an obstacle.
    0 - A gate.
    INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""

INF=2147483647

import collections

class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # Time: O(m * n)
        # Space: O(g)
        # Hints:
        # 1) BFS
        # 2) Start from 0 (gate) and move to neighbor door
        # 3) Put those neighbor cells into the queue (+1 distance)
        # 4) Put those neighbor's neighbor cells (+2 distance)
        q = collections.deque([(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if r == 0])
        while q:
            (i, j) = q.popleft()
            for a, b in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= a < len(rooms) and 0 <= b < len(rooms[a]) and rooms[a][b] == 2147483647:
                    rooms[a][b] = rooms[i][j] + 1
                    q.append((a, b))
 
    def wallsAndGates_dfs(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # Time: O(m * n)
        # Space: O(m * n), call stack
        # Hints:
        # 1) The key is to compare with the current minimum distance, d
        def search(i, j, d):
            if not ( 0 <= i < len(rooms) and 0 <= j < len(rooms[i])): return
            if rooms[i][j] < d: return
            rooms[i][j] = d
            search(i - 1, j, d + 1)
            search(i + 1, j, d + 1)
            search(i, j - 1, d + 1)
            search(i, j + 1, d + 1)
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    search(i, j, 0)
        for row in rooms: print(row)

    def wallsAndGates_failed(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        def search(i, j, d):
            if not ( 0 <= i < len(rooms) and 0 <= j < len(rooms[i])): return
            if rooms[i][j] < 0: return
            rooms[i][j] = min(rooms[i][j], d + 1)
            if i > 0 and rooms[i-1][j] > 0: search(i - 1, j, rooms[i][j])
            if i < len(rooms) - 1 and rooms[i+1][j] > 0: search(i + 1, j, rooms[i][j])
            if j > 0 and rooms[i][j-1] > 0: search(i, j-1, rooms[i][j])
            if j < len(rooms[0]) - 1 and rooms[i][j+1] > 0: search(i, j+1, rooms[i][j])
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    search(i, j, 0)
        for row in rooms: print(row)
        

if __name__ == '__main__':
    test_cases = [
        ([[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]], [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        rooms = test_case[0]
        Solution().wallsAndGates(rooms)
        print('output:', rooms)
        assert rooms == test_case[1]

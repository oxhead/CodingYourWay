"""
https://leetcode.com/problems/surrounded-regions

Related:
  - lt_200_number-of-islands
  - lt_286_walls-and-gates
"""

"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""

class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # Time: O(m * n)
        # Space: O(m * n), call stack
        if not any(board): return
        def dfs(board, i, j, m, n):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O': return
            board[i][j] = 'M'
            dfs(board, i + 1, j, m, n)
            dfs(board, i - 1, j, m, n)
            dfs(board, i, j + 1, m, n)
            dfs(board, i, j - 1, m, n)
        m, n = len(board), len(board[0])
        for i in range(m):
            if board[i][0] == 'O':
                dfs(board, i, 0, m, n)
            if board[i][n-1] == 'O':
                dfs(board, i, n-1, m, n)
        for j in range(n):
            if board[0][j] == 'O':
                dfs(board, 0, j, m, n)
            if board[m-1][j] == 'O':
                dfs(board, m-1, j, m, n)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
 
           
    def solve_verbose(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(1, len(board) - 1):
            for j in range(1, len(board[i]) - 1):
                if board[i][j] != "O": continue
                if visited[i][j]: continue
                stack = [(i, j)]
                trace = set(stack)
                failed = False
                while stack:
                    m, n = stack.pop()
                    visited[i][j] = True
                    board[m][n] = "X"
                    if (m == 1 and board[m-1][n] == "O") or (m == len(board) - 2 and board[m+1][n] == "O") or (n == 1 and board[m][n-1] == "O") or (n == len(board[m]) - 2 and board[m][n+1] == "O"):
                        failed = True
                        break
                    if board[m-1][n] == "O":
                        stack.append((m-1, n))
                        trace.add((m-1, n))
                    if board[m+1][n] == "O":
                        stack.append((m+1, n))
                        trace.add((m+1, n))
                    if board[m][n-1] == "O":
                        stack.append((m, n-1))
                        trace.add((m, n-1))
                    if board[m][n+1] == "O":
                        stack.append((m, n+1))
                        trace.add((m, n+1))
                if failed:
                    for m, n in trace:
                        board[m][n] = "O"
                    
        

if __name__ == '__main__':
    test_cases = [
        ([], []),
        ([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]], [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]),
        ([["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]], [["X","O","X","X"],["O","X","X","X"],["X","X","X","O"],["O","X","X","X"],["X","X","X","O"],["O","X","O","X"]]),
        ([["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]], [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        board = test_case[0]
        Solution().solve(board)
        print('output:', board)
        assert board == test_case[1]


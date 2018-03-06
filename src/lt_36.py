"""
https://leetcode.com/problems/valid-sudoku

Related:
  - lt_37

Complexity:
  - Time:
  - Space:
"""

"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated. 
"""

import itertools

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def is_valid(nums):
            records = set()
            for n in nums:
                if n == '.': continue
                if n in records:
                    return False
                else:
                    records.add(n)
            return True

        n = 9
        for i in range(n):
            if not is_valid(board[i]): return False 
        for j in range(n):
            if not is_valid([board[i][j] for i in range(n)]): return False
        for i, j in itertools.product(range(3), range(3)):
            nums = []
            for a, b in itertools.product(range(3), range(3)):
                nums.append(board[i*3+a][j*3+b])
            if not is_valid(nums): return False
        return True

if __name__ == '__main__':
    test_cases = [
        # ([[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]], True)
        ([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]], False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isValidSudoku(test_case[0])
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/word-search

Related:
  - lt_212_word-search-ii
"""

"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # Time: O(m * n * l), board(m*n) and word(l)
        # Space: O(l)
        def search(i, j, index, records):
            if (i, j) in records: return False
            elif board[i][j] != word[index]: return False
            
            if index == len(word) - 1:
                return True
            
            records.add((i, j))
            if i + 1 < len(board) and search(i + 1, j, index + 1, records):
                return True
            elif i - 1 >= 0 and search(i-1, j, index + 1, records):
                return True
            elif j + 1 < len(board[i]) and search(i, j + 1, index + 1, records):
                return True
            elif j - 1 >= 0 and search(i, j - 1, index + 1, records):
                return True
            records.remove((i, j))
            return False
                        
        if not word: return False
        elif len(word) == 0: return True
        elif not board: return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if search(i, j, 0, set()):
                    return True
        return False


if __name__ == '__main__':
    test_cases = [
        (([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], "ABCCED"), True),
        (([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], "SEE"), True),
        (([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], "ABCB"), False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().exist(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


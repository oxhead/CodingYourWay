"""
https://leetcode.com/problems/word-search

Related:
  - lt_79_word-search
"""

"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Return ["eat","oath"].

Note:
You may assume that all inputs are consist of lowercase letters a-z.

click to show hint.

You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.
"""

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.leaves = {}

    def insert(self, word):
        current = self
        for c in word:
            if c not in current.leaves:
                current.leaves[c] = TrieNode()
            current = current.leaves[c]
        current.is_word = True


class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Time: O(m * n * l)
        # Space: O(l)
        def search(trie, i, j, current_word):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or (i, j) in records:
                return

            if board[i][j] not in trie.leaves:
                return 

            current_word.append(board[i][j])
            trie = trie.leaves[board[i][j]] 
            if trie.is_word:
                output.add("".join(current_word))
            records.add((i, j))
            search(trie, i - 1, j, current_word)
            search(trie, i + 1, j, current_word)
            search(trie, i, j - 1, current_word)
            search(trie, i, j + 1, current_word)
            records.remove((i, j))
            current_word.pop()

        trie = TrieNode()
        for word in words:
            trie.insert(word)

        output = set()
        records = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                search(trie, i, j, [])
        return list(output)

    def findWords_TLE(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def search(i, j, index, word, records):
            if index == len(word): return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or (i, j) in records or board[i][j] != word[index]: return False
            records.add((i, j))
            if search(i - 1, j, index + 1, word, records) or search(i + 1, j, index + 1, word, records) or search(i, j - 1, index + 1, word, records) or search(i, j + 1, index + 1, word, records):
                return True
            records.remove((i, j))

        output = []
        for word in set(words):
            found = False
            i = 0
            while i < len(board) and not found:
                j = 0
                while j < len(board[i]) and not found:
                    if search(i, j, 0, word, set()):
                        found = True
                    j += 1
                i += 1
            if found:
                output.append(word)
        return output
                       


if __name__ == '__main__':
    test_cases = [
        (([['a']], ['a', 'a']), ['a']),
        (([['o','a','a','n'], ['e','t','a','e'], ['i','h','k','r'], ['i','f','l','v']], ["oath","pea","eat","rain"]), ["eat","oath"]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findWords(*test_case[0])
        print('output:', output)
        assert sorted(output) == sorted(test_case[1])


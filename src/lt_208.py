"""
https://leetcode.com/problems/implement-trie-prefix-tree

Related:
  - lt_211_add-and-search-word-data-structure-design
  - lt_642_design-search-autocomplete-system
  - lt_648_replace-words
  - lt_676_implement-magic-dictionary
"""

"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.leaves = {}
        self.is_word = False
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self
        for c in word:
            if c not in node.leaves:
                node.leaves[c] = Trie()
            node = node.leaves[c]
        node.is_word = True
        
    def find(self, word):
        node = self
        for c in word:
            if c not in node.leaves: return None
            node = node.leaves[c]
        return node

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.find(word)
        return node.is_word if node else False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.find(prefix)
        return node is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    test_cases = [
        ([('p', 'a')], [False]),
        ([('i', 'a'), ('s', 'a'), ('p', 'a')], [None, True, True]),
        ([('i', 'ab'), ('s', 'a'), ('p', 'a')], [None, False, True]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        obj = Trie()
        for cmd, ans in zip(test_case[0], test_case[1]):
            op, val = cmd
            if op == 'i':
                obj.insert(val)
            elif op == 's':
                assert obj.search(val) == ans
            elif op == 'p':
                assert obj.startsWith(val) == ans

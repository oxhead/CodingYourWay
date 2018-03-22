"""
https://leetcode.com/problems/longest-word-in-dictionary

Related:
  - lt_524_longest-word-in-dictionary-through-deleting
  - lt_676_implement-magic-dictionary
"""

"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.

Example 1:

Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:

Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Note:
All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
"""

import collections
from functools import reduce

class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Time: O(n * k)
        # Space: O(n)
        records = set(words)
        output = ''
        for word in words:
            if len(word) > len(output) or (len(word) == len(output) and word < output):
                if all([word[:i] in records for i in range(1, len(word))]):
                    output = word
        return output

    def longestWord_trie(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)["_end"] = i 
        stack = list(trie.values())
        result = ""
        while stack:
            curr = stack.pop()
            if "_end" in curr:
                word = words[curr["_end"]]
                if len(word) > len(result) or (len(word) == len(result) and word < result):
                    result = word
                stack += [curr[letter] for letter in curr if letter != "_end"]
        return result 


if __name__ == '__main__':
    test_cases = [
        (["w","wo","wor","worl", "world"], "world"),
        (["a", "banana", "app", "appl", "ap", "apply", "apple"], "apple"),
        (["k","lg","it","oidd","oid","oiddm","kfk","y","mw","kf","l","o","mwaqz","oi","ych","m","mwa"], "oiddm"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().longestWord(test_case[0])
        print('output:', output)
        assert output == test_case[1]


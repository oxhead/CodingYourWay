"""
https://leetcode.com/problems/number-of-matching-subsequences

Related:
  - lt_392_is-subsequence
"""

"""
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

Note:

    All words in words and S will only consists of lowercase letters.
    The length of S will be in the range of [1, 50000].
    The length of words will be in the range of [1, 5000].
    The length of words[i] will be in the range of [1, 50].
"""

import collections

class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        # Time: O(n + w), n=len(S) and w=len(words)
        # Space: O(w)
        # https://leetcode.com/problems/number-of-matching-subsequences/discuss/117634/Efficient-and-simple-go-through-words-in-parallel-with-explanation
        # Hints:
        # 1) Similar to trie
        # Examples:
        # S = "abcde"
        # words = ["a", "bb", "acd", "ace"]
        #
        # step 1: initialize
        # 'a': ['(a)', '(a)cd', '(a)ce'],
        # 'b': ['(b)b']
        #
        # step 2: match'a'
        # 'b': ['(b)b']
        # 'c': ['a(c)d', 'a(c)e']
        # 'None': ['a']
        #
        # step 3: match 'b'
        # 'b': ['b(b)']
        # 'c': ['a(c)d', 'a(c)e']
        # 'None': ['a']
        #
        # step 4: match 'c'
        # 'b': ['b(b)']
        # 'd': ['ac(d)']
        # 'e': ['ac(e)']
        # 'None': ['a']
        #
        # step 5: match 'd'
        # 'b': ['b(b)']
        # 'e': ['ac(e)']
        # 'None': ['a', 'acd']
        #
        # step 6: match 'e'
        # 'b': ['b(b)']
        # 'None': ['a', 'acd', 'ace']

        prefixs = collections.defaultdict(list)
        for word in words:
            prefixs[word[0]].append(iter(word[1:]))
        for c in S:
            for it in prefixs.pop(c, ()):
                # next(x, default_value)
                prefixs[next(it, None)].append(it)
        return len(prefixs[None])

    def numMatchingSubseq_TLE(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """ 
        def match(word):
            i, j = len(S) - 1, len(word) - 1
            while i >= 0 and j >= 0:
                if S[i] == word[j]: j -= 1
                i -= 1
            return j == -1
        return sum([match(word) for word in words])

if __name__ == '__main__':
    test_cases = [
        (("abcde", ["a", "bb", "acd", "ace"]), 3),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().numMatchingSubseq(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


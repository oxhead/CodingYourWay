"""
https://leetcode.com/problems/word-break-ii

Related:
  - lt_139_word-break
  - lt_472_concatenated-words
"""

"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"]. 
"""

from collections import defaultdict

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # Time: O(?)
        # Space: O(?)
        # https://shenjie1993.gitbooks.io/leetcode-python/140%20Word%20Break%20II.html
        def dfs(s):
            if not s: return [None]
            if s in records:
                return records[s]
            results = []
            for word in wordDict:
                n = len(word)
                if s[:n] == word:
                    for r in dfs(s[n:]):
                        if r:
                            results.append(word + " " + r)
                        else:
                            results.append(word)
                        
            records[s] = results
            return results
        records = defaultdict(list)
        return dfs(s)
        

if __name__ == '__main__':
    test_cases = [
        (("catsanddog", ["cat", "cats", "and", "sand", "dog"]), ["cats and dog", "cat sand dog"]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().wordBreak(*test_case[0])
        print('output:', output)
        assert sorted(output) == sorted(test_case[1])


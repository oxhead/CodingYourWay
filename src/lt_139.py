"""
https://leetcode.com/problems/word-break

Related:
  - lt_140_word-break-ii
"""

"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes. 
"""

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # https://shenjie1993.gitbooks.io/leetcode-python/139%20Word%20Break.html
        # https://github.com/algorhythms/LeetCode/blob/master/139%20Word%20Break.py
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i, -1, -1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i + 1] = True
                    break
        return dp[n]


if __name__ == '__main__':
    test_cases = [
        (('leetcode', {'leet', 'code'}), True),
        (('thetabledownthere', {'the', 'theta', 'table', 'down', 'there', 'bled', 'own'}), True),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().wordBreak(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


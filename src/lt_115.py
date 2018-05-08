"""
https://leetcode.com/problems/distinct-subsequences

Related:
"""

"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""

class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # Time: O(m * n)
        # Space: O(m * n)
        # Hints:
        # 1) dp(i, j) = dp(i-1, j), for s[:i] and t[:j]
        # 2) if s[i-1] == t[j-1], dp(i, j) = dp(i-1, j) + dp(i-1, j-1)
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[len(s)][len(t)]

    def numDistinct_optimized(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # Time: O(m * n)
        # Space: O(n)
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        for i in range(len(s)):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]
        return dp[len(t)]

    def numDistinct_TLE(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        def search(s1, s2):
            if s1 == s2: return 1
            elif not s2: return 1
            count = 0
            for i, c in enumerate(s1):
                if len(s1) - i + 1 < len(s2): continue
                if s1[i] != s2[0]: continue
                count += search(s1[i+1:], s2[1:])
            return count
        return search(s, t)
        

if __name__ == '__main__':
    test_cases = [
        (("ba", "g"), 0),
        (("rabbbit", "rabbit"), 3),
        (("babgbag", "bag"), 5),
        (("aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe", "bddabdcae"), 10582116),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().numDistinct(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


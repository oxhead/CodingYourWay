"""
https://leetcode.com/problems/regular-expression-matching

Related:
  - lt_10_wildcard-matching
"""

"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Time: O(m * n)
        # Space: O(m * n)
        # https://github.com/kamyu104/LeetCode/blob/master/Python/regular-expression-matching.py
        # http://jianlu.github.io/2016/11/07/leetcode10-Regular-Expression-Matching/
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(2, len(p) + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                else:
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        return dp[len(s)][len(p)]

    def isMatch_recursive(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Time: O(?)
        # Space: O(m + n)
        # https://github.com/kamyu104/LeetCode/blob/master/Python/regular-expression-matching.py
        # https://articles.leetcode.com/regular-expression-matching/
        if not p: return not s
        if len(p) == 1 or p[1] != '*':
            if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
           while len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                if self.isMatch(s, p[2:]):
                    return True
                s = s[1:]
           return self.isMatch(s, p[2:])


if __name__ == '__main__':
    test_cases = [
        (("aa", "a"), False),
        (("aa", "aa"), True),
        (("aaa", "aa"), False),
        (("aa", "a*"), True),
        (("aa", ".*"), True),
        (("ab", ".*"), True),
        (("aab", "c*a*b"), True),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isMatch(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/regular-expression-matching

Related:
  - lt_10_wildcard-matching
"""

"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Time: O(m + n)
        # Space: O(1)
        # https://shenjie1993.gitbooks.io/leetcode-python/044%20Wildcard%20Matching.html
        s_left, s_last, s_len, p_left, p_last, p_len = 0, -1, len(s), 0, -1, len(p)
        while s_left < s_len:
            if p_left < p_len and (s[s_left] == p[p_left] or p[p_left] == '?'):
                s_left += 1
                p_left += 1
            elif p_left < p_len and p[p_left] == '*':
                p_left += 1
                s_last = s_left
                p_last = p_left
            elif p_last != -1:
                s_last += 1
                s_left = s_last
                p_left = p_last
            else:
                return False
        while p_left < p_len and p[p_left] == '*':
            p_left += 1
        return p_left == p_len

    def isMatch_failed(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_left = p_left = 0
        s_len, p_len = len(s), len(p)
        while s_left < s_len and p_left < p_len:
            print('#-----')
            print(s_left, s[s_left])
            print(p_left, p[p_left])
            if p_left + 1 < p_len and s[s_left] == p[p_left + 1]:
                p_left += 1
            elif p[p_left] == '*':
                s_left += 1
            elif p[p_left] == '?':
                s_left += 1
                p_left += 1
            else:
                if s[s_left] != p[p_left]:
                    return False
                s_left += 1
                p_left += 1
        print(s_left, s[s_left])
        print(p_left, p[p_left])
        if p_left < p_len and len(p[p_left:].replace('*', '')) > 0:
            return False
        elif s_left < s_len:
            return False
        return True

if __name__ == '__main__':
    test_cases = [
        #(("aa", "a"), False),
        #(("aa", "aa"), True),
        #(("aaa", "aa"), False),
        #(("aa", "*"), True),
        #(("aa", "a*"), True),
        #(("ab", "?*"), True),
        #(("aab", "c*a*b"), False),
        #(("aa", "a*b"), False),
        (("abefcdgiescdfimde", "ab*cd?i*de"), True)
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isMatch(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/is-subsequence

Related:
  - lt_792_number-of-matching-subsequences
"""

"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
"""

class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(1)
        # Hints:
        # 1) Greedy
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 and j >= 0:
            if s[i] == t[j]:
                i -= 1
            j -= 1
        return i == -1
        

if __name__ == '__main__':
    test_cases = [
        (("abc", "ahbgdc"), True),
        (("axc", "ahbgdc"), False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isSubsequence(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/palindromic-substrings

Related:
  - lt_5_longest-palindromic-substring
  - lt_516_longest-palindromic-subsequence
"""

"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:

    The input string length won't exceed 1000.
"""

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(1)
        def count(s, l, r):
            total = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1
            return total
        total = 0
        for i in range(len(s)):
            total += count(s, i, i)
            total += count(s, i, i+1)
        return total
 
    def countSubstrings_dp(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(n^2) 
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for size in range(1, len(s)):
            for i in range(len(s)):
                if i + size >= len(s): continue
                j = i + size
                if s[i] == s[j]:
                    if j - i == 1: dp[i][j] = 1
                    elif dp[i+1][j-1] == 1: dp[i][j] = 1 
        return sum([sum(row) for row in dp])


if __name__ == '__main__':
    test_cases = [
        ("abc", 3),
        ("aaa", 6),
        ("aaaaa", 15),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().countSubstrings(test_case[0])
        print('output:', output)
        assert output == test_case[1]


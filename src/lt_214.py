"""
https://leetcode.com/problems/shortest-palindrome

Related:
  - lt_5_longest-palindromic-substring
  - lt_28_implement-strstr
  - lt_336_palindrome-pairs
"""

"""
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"

Example 2:

Input: "abcd"
Output: "dcbabcd"
"""

class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Time: O(n)
        # Space: O(1)
        # https://leetcode.com/problems/shortest-palindrome/discuss/60099/AC-in-288-ms-simple-brute-force
        # Hints:
        # 1) Using str.startswith to check whether a substring is a palindrome
        # Examples:
        # r       s
        # ()baa   aab
        # (b)aa   aab  : matched -> shortest palindrom (b)aab
        # r       s
        # ()aba   aba  : matched -> shortest palindrom aba
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s

    def shortestPalindrome_v2(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Time: O(n^2)
        # Space: O(1)
        # Hints:
        # 1) Added words to form a plindrom only when the cut-out words (from the end) form a palindrom
        # Examples:
        # aab
        # *aab is a palindrome only when aa is a palindrom
        # aabc
        # *aabc is a palindrom only when aab is a palindrome
        # **aabc is a palindrome only wehn aa is a palindrome
        if not s: return s
        r = s[::-1]
        for i in range(len(s)):
            s2 = s[:len(s)-i]
            if s2 == s2[::-1]: return s[len(s)-i:][::-1] + s


if __name__ == '__main__':
    test_cases = [
        ("", ""),
        ("aacecaaa", "aaacecaaa"),
        ("abcd", "dcbabcd"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().shortestPalindrome(test_case[0])
        print('output:', output)
        assert output == test_case[1]


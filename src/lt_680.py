"""
https://leetcode.com/problems/valid-palindrome-ii
https://leetcode.com/problems/valid-palindrome

Related:
  - lt_125_valid-palindrome
"""

"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True

Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:

    The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(1)
        # Hints:
        # 1) Find the character that does not form a valid palindrome
        # 2) Check the palindrome for both the cases (normal order and reverse order)
        if s == s[::-1]: return True
        r = s[::-1]
        for i in range(len(s)):
            if r[i] != s[i]: break
        r = r[:i] + r[i+1:]
        if r == r[::-1]: return True
        s = s[:i] + s[i+1:]
        return s == s[::-1]

    def validPalindrome_v2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_valid(left, right):
            while left < right:
                if s[left] != s[right]: return False
                left += 1
                right -= 1
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_valid(left, right - 1) or is_valid(left + 1, right)
            left += 1
            right -= 1
        return True

    def validPalindrome_TLE(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i, c in enumerate(s):
            p = s[:i] + s[i+1:]
            if p == p[::-1]: return True
        return s == s[::-1]
        

if __name__ == '__main__':
    test_cases = [
        ("aba", True),
        ("abca", True),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().validPalindrome(test_case[0])
        print('output:', output)
        assert output == test_case[1]


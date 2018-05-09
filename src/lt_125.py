"""
https://leetcode.com/problems/valid-palindrome

Related:
  - lt_234_palindrome-linked-list
  - lt_680_valid-palindrome-ii
"""

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome. 
"""

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(1)
        # Hints:
        # 1) Use two pointers
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower(): return False
            left += 1
            right -= 1
        return True

    def isPalindrome_builtin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True

        ss = [c.lower() for c in s if c.isalnum()]
        return ss == ss[::-1]


if __name__ == '__main__':
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("0P", False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isPalindrome(test_case[0])
        print('output:', output)
        assert output == test_case[1]


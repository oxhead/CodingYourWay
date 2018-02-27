"""
https://leetcode.com/problems/valid-palindrome

Related:
  - lt_234
  - lt_680

Complexity:
  - Time: O()
  - Space: O()
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
        i = 0
        j = len(s)-1
        while i < j:
            while i < len(s) and not s[i].isalnum(): i += 1
            if i >= len(s): return True
            while j >= 0 and not s[j].isalnum(): j -= 1
            if j < 0: return True
            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1
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


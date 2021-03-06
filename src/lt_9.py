"""
https://leetcode.com/problems/palindrome-number

Related:
  - lt_234_palindrome-linked-list
"""

"""
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.
Some hints:

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Time: O(1)
        # Space: O(1)
        # Hints:
        # 1) Reverse the integer and compare with the original x
        # 2) Using module and shift to reverse the integer
        if x < 0: return False
        n, y = x, 0
        while n:
            y *= 10
            y += n % 10
            n //= 10
        return x == y

    def isPalindrome_string(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        s = str(x)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]: return False
            left += 1
            right -= 1
        return True

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n, y = x, 0
        while n:
            y *= 10
            y += n % 10
            n //= 10
        return x == y

if __name__ == '__main__':
    test_cases = [
        (1, True),
        (11, True),
        (121, True),
        (1221, True),
        (1231, False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isPalindrome(test_case[0])
        print('output:', output)
        assert output == test_case[1]


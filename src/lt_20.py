"""
https://leetcode.com/problems/valid-parentheses

Related:
  - lt_22
  - lt_32
  - lt_301
"""

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if len(stack) == 0: return False
                c_left = stack.pop()
                if c_left == '(' and c != ')': return False
                if c_left == '{' and c != '}': return False
                if c_left == '[' and c != ']': return False
        return len(stack) == 0

if __name__ == '__main__':
    test_cases = [
        ('()', True),
        ('()[]{}', True),
        ('(]', False),
        ('([)]', False),
        ('{(()[])}{()[]}', True),
        ('())', False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isValid(test_case[0])
        print('output:', output)
        assert output == test_case[1]


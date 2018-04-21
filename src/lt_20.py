"""
https://leetcode.com/problems/valid-parentheses

Related:
  - lt_22_generate-parentheses
  - lt_32_longest-valid-parentheses
  - lt_301_remove-invalid-parentheses
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
            if c in ('(', '[', '{'):
                stack.append(c)
            elif not stack: return False
            else:
                p = stack.pop()
                if (p, c) not in (('(', ')'), ('[', ']'), ('{', '}')): return False
        return True


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


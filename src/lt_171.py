"""
https://leetcode.com/problems/excel-sheet-column-number

Related:
  - lt_168

Complexity:
  - Time: O(1)
  - Space: O(1)
"""

"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum([26**i * (ord(c) - 64) for i, c in enumerate(reversed(s.upper()))])

if __name__ == '__main__':
    test_cases = [
        ('A', 1),
        ('B', 2),
        ('C', 3),
        ('Z', 26),
        ('AA', 27),
        ('AB', 28),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().titleToNumber(test_case[0])
        print('output:', output)
        assert output == test_case[1]


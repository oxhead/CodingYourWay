"""
https://leetcode.com/problems/excel-sheet-column-number

Related:
  - lt_168_excel-sheet-column-title
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

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = reversed(s)
        count = 0
        for i, c in enumerate(s):
            count += (ord(c) - ord('A') + 1) * 26**i
        return count


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


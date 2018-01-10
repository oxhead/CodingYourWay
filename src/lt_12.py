"""
https://leetcode.com/problems/integer-to-roman

Related:
  - lt_13
  - lt_273

Complexity:
  - Time: O(1)
  - Space: O(1)
"""

"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    def intToRoman(self, num):
        """
        :type s: str
        :rtype: int
        """
        symbols = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
                   40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
                   400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        sorted_symbols = reversed(sorted(symbols.keys()))
        result = []

        for key in sorted_symbols:
            if num // key > 0:
                result += symbols[key] * (num // key)
            num -= key * (num // key)

        return "".join(result)


if __name__ == '__main__':
    test_cases = [
        (1, "I"),
        (5, "V"),
        (10, "X"),
        (50, "L"),
        (100, "C"),
        (500, "D"),
        (1000, "M"),
        (400, "CD"),
        (900, "CM"),
        (495, "CDXCV"),
        (99, "XCIX"),
        (1776, "MDCCLXXVI"),
        (1954, "MCMLIV"),
        (1990, "MCMXC"),
        (2014, "MMXIV"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().intToRoman(test_case[0])
        print('output:', output)
        assert output == test_case[1]


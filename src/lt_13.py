"""
https://leetcode.com/problems/roman-to-integer

Related:
  - lt_12

Complexity:
  - Time: O(n)
  - Space: O(1)
"""

"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        value = 0
        for i in range(len(s)):
            # cases: IV, IX, CD, CM
            # need to substract one more time because it is already added before
            if i > 0 and symbols[s[i]] > symbols[s[i-1]]:
                value += symbols[s[i]] - 2 * symbols[s[i-1]]
            else:
                value += symbols[s[i]] 
        
        return value


if __name__ == '__main__':
    test_cases = [
        ("I", 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
        ("CD", 400),
        ("CM", 900),
        ("CDXCV", 495),
        ("DCXXI", 621),
        ("XCIX", 99),
        ("MDCCLXXVI", 1776),
        ("MCMLIV", 1954),
        ("MCMXC", 1990),
        ("MMXIV", 2014),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().romanToInt(test_case[0])
        print('output:', output)
        assert output == test_case[1]


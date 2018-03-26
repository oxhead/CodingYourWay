"""
https://leetcode.com/problems/string-to-integer-atoi

Related:
  - lt_7_reverse-integer
  - lt_65_valid-number
"""

"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

 

Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        s = str.strip()
        if not s: return 0
        if s.startswith('-'):
            sign = -1
            s = s[1:]
        elif s.startswith('+'):
            sign = 1
            s = s[1:]
        else:
            sign = 1
        if len(s) == 0: return 0
        for i, d in enumerate(s):
            if not d.isdigit():
                s = s[:i]
                break
        
        if not s.isdecimal(): return 0
        n = int(s)
        if sign == 1 and n > 2147483647: return 2147483647
        elif sign == -1 and n > 2147483648: return -2147483648
        return sign * int(s)
        

if __name__ == '__main__':
    test_cases = [
        ("", 0),
        ("+", 0),
        ("-", 0),
        ("1", 1),
        ("-1", -1),
        (" 1 ", 1),
        (" -1 ", -1),
        ("+1", 1),
        ("+-2", 0),
        ("2147483648", 2147483647),
        ("-2147483649", -2147483648),
        ("  -0012a42", -12),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().myAtoi(test_case[0])
        print('output:', output)
        assert output == test_case[1]


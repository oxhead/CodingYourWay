"""
https://leetcode.com/problems/divide-two-integers

Related:
"""

"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT. 
"""

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Time: O(1)
        # Space: O(1)
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while dividend >= divisor:
            inc = divisor
            i = 0
            while dividend >= inc:
                dividend -= inc
                ans += 1 << i
                inc <<= 1
                i += 1
        # handling overflow
        if ans >= 0x7FFFFFFF and sign == 1:
            return 0x7FFFFFFF
        return sign * ans


if __name__ == '__main__':
    test_cases = [
        ((29, 3), 9),
        ((4, 2), 2),
        ((15, 7), 2),
        ((-2147483648, -1), 2147483647),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().divide(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


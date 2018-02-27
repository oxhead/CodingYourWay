"""
https://leetcode.com/problems/reverse-integer

Related:
  - lt_8

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows. 
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >= 0 else -1
        x *= sign
        output = 0
        while x:
            output = output * 10 + x % 10
            x = x // 10
        if output > 2**31 - 1:
            return 0
        else:
            return output * sign

    def reverse_naive(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x: return x
        sign = 1 if x >= 0 else -1
        digits = str(x * sign)[::-1]
        index_zeros = -1
        for i, d in enumerate(digits):
            if d == 0: index_zeros = i
            else: break
        if index_zeros >= 0:
            digits = digits[index_zeros+1:]
        output = int(digits)
        if output > 2**31 -1:
            return 0
        else:
            return output * sign

if __name__ == '__main__':
    test_cases = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (12300, 321),
        (1534236469, 0)
    ]

    for test_case in test_cases:
        print('case:', test_case)
        # output = Solution().reverse(test_case[0])
        output = Solution().reverse_naive(test_case[0])
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/add-digits

Related:
  - lt_202_happy-number
"""

"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime? 
"""

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Time: O(k)
        # Space: O(1)
        while num >= 10:
            num = num // 10 + num % 10
        return num

    def addDigits_naive(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            num = sum([int(d) for d in str(num)])
        return num

    def addDigits_math(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Time: O(1)
        # Space: O(1)
        # Digital root
        # num = n0 * 10^0 + n1 * 10^1 + n2 * 10^2 + ...
        # addDigits(num) = n0 + n1 + n2 + ... = num % 9
        # 10 11 12 13 14 15 16 17 18 19 20 21
        #  1  2  3  4  5  6  7  8  9  1  2  3
        return (num - 1) % 9 + 1 if num > 0 else 0


if __name__ == '__main__':
    test_cases = [
        (38, 2),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().addDigits(test_case[0])
        print('output:', output)
        assert output == test_case[1]


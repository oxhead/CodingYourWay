"""
https://leetcode.com/problems/ugly-number

Related:
  - lt_202_happy-number
  - lt_204_count-primes
  - lt_264_ugly-number-ii
"""

"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note:

    1 is typically treated as an ugly number.
    Input is within the 32-bit signed integer range.
"""

class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Time: O(1)
        # Space: O(1)
        if num <= 0: return False
        for d in (2, 3, 5):
            while num % d == 0:
                num //= d
        return num == 1

    def isUgly_recursive(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        elif num in (1, 2, 3, 5): return True
        for d in (2, 3, 5):
            if num % d == 0:
                return self.isUgly(num // d)
        return False


if __name__ == '__main__':
    test_cases = [
        (0, False),
        (1, True),
        (6, True),
        (8, True),
        (14, False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isUgly(test_case[0])
        print('output:', output)
        assert output == test_case[1]


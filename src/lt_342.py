"""
https://leetcode.com/problems/power-of-two

Related:
  - lt_231_power-of-two
  - lt_326_power-of-three
"""

"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion? 
"""

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        while num > 1:
            if num & 3 != 0: return False
            num = num >> 2
        return True

    def isPowerOfFour_noloop(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num & (num - 1) == 0 and num & 0b01010101010101010101010101010101 == num

if __name__ == '__main__':
    test_cases = [
        (1, True),
        (2, False),
        (3, False),
        (4, True),
        (5, False),
        (6, False),
        (16, True),
        (-16, False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isPowerOfFour(test_case[0])
        print('output:', output)
        assert output == test_case[1]


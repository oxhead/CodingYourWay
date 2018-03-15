"""
https://leetcode.com/problems/power-of-three

Related:
  - lt_321_power-of-two
  - lt_342_power-of-four
"""

"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""

import math

class Solution:
    def isPowerOfThree(self, n):
        return n > 0 and (math.log10(n) / math.log10(3)) % 1 == 0 
        
    def isPowerOfThree_iterative(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 2:
            if n % 3 != 0: return False
            n = n // 3
        return n == 1

if __name__ == '__main__':
    test_cases = [
        (0, False),
        (1, True),
        (3, True),
        (9, True),
        (27, True),
        (4, False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isPowerOfThree(test_case[0])
        print('output:', output)
        assert output == test_case[1]


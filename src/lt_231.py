"""
https://leetcode.com/problems/power-of-two

Related:
  - lt_191_number-of-1-bits
  - lt_326_power-of-three
  - lt_342_power-of-four
"""

"""
Given an integer, write a function to determine if it is a power of two. 
"""

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        while n > 1:
            if n & 1 != 0: return False
            n = n >> 1
        return True

if __name__ == '__main__':
    test_cases = [
        (1, True),
        (2, True),
        (3, False),
        (4, True),
        (6, False),
        (-16, False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isPowerOfTwo(test_case[0])
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/single-number

Related
  - lt_137_single-number-ii
  - lt_260_single-number-iii
  - lt_268_missing-number
  - lt_287_find-the-duplicate-number
  - lt_389_find-the-difference
"""

"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 
"""

import operator
import functools

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        return functools.reduce(operator.xor, nums)


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 2, 3, 3], 1)
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().singleNumber(test_case[0])
        print('output:', output)
        assert output == test_case[1]


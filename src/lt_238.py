"""
https://leetcode.com/problems/product-of-array-except-self

Related:
  - lt_42_trapping-rain-water
  - lt_152_maximum-product-subarray
  - lt_265_paint-house-ii
"""

"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""

from operator import mul
from functools import reduce

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleMedium/238.html
        output = [None] * len(nums)
        output[0] = 1
        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]
        right = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output
 
    def productExceptSelf_naive(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # time limit exceeded
        output = [None] * len(nums)
        for i in range(len(nums)):
            product = 1
            output[i] = reduce(mul, nums[:i] + nums[i+1:], 1)
        return output

    def productExceptSelf_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        count = 0
        for n in nums:
            if n == 0:
                count += 1
                if count > 1:
                    product = 0
                    break
            product *= n
        output = []
        for n in nums:
            if n == 0 or count == 1:
                output.append(product)
            else:
                output.append(product / n)
        return output


if __name__ == '__main__':
    test_cases = [
        ([0, 0], [0, 0]),
        ([1, 2, 3, 4], [24, 12, 8, 6]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().productExceptSelf(test_case[0])
        print('output:', output)
        assert output == test_case[1]


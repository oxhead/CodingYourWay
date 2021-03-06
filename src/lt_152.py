"""
https://leetcode.com/problems/maximum-product-subarray

Related:
  - lt_53_maximum-subarray
  - lt_198_house-robber
  - lt_238_product-of-array-except-self
  - lt_628_maximum-product-of-three-numbers
  - lt_713_subarray-product-less-than-k
"""

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6. 
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        max_product, current_max, current_min = float('-inf'), 1, 1
        for n in nums:
            current_max, current_min = max(current_max * n, current_min * n, n), min(current_min * n, current_max * n, n)
            max_product = max(max_product, current_max)
        return max_product

    def maxProduct_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 1: return 0
        
        current_min = nums[0]
        current_max = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            previous_max = current_max
            current_max = max(nums[i], previous_max * nums[i], current_min * nums[i])
            current_min = min(nums[i], previous_max * nums[i], current_min * nums[i])
            result = max(result, current_max)
        return result


if __name__ == '__main__':
    test_cases = [
        ([-2], -2),
        ([2, 3, -2, 4], 6),
        ([-1, -2, -9, -6], 108),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().maxProduct(test_case[0])
        print('output:', output)
        assert output == test_case[1]


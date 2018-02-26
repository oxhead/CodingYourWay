"""
https://leetcode.com/problems/maximum-product-subarray

Related:
  - lt_53
  - lt_198
  - lt_238
  - lt_628
  - lt_713

Complexity:
  - Time: O()
  - Space: O()
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
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().maxProduct(test_case[0])
        print('output:', output)
        assert output == test_case[1]


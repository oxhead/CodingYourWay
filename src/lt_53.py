"""
https://leetcode.com/problems/maximum-subarray

Related:
  - lt_121
  - lt_152
  - lt_697
"""

"""
 Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

 For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
 the contiguous subarray [4,-1,2,1] has the largest sum = 6.

 click to show more practice.
 More practice:

     If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        max_sum = nums[0]
        current_sum = nums[0]
        for n in nums[1:]:
            current_sum = max(current_sum + n, n)
            max_sum = max(max_sum, current_sum)
        return max_sum

    def maxSubArray_verbose(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)
        global_max, local_max = float("-inf"), 0
        for x in nums:
            # best from previous numbers
            local_max = max(0, local_max + x)
            # the current best
            global_max = max(global_max, local_max)
        return global_max 

    def maxSubArray_dp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] <= 0 and nums[i] >= 0:
                dp[i] = nums[i]
                continue
            tmp = dp[i-1] + nums[i]
            if tmp >= 0: dp[i] = tmp
            else: dp[i] = nums[i]
        return max(dp)


if __name__ == '__main__':
    test_cases = [
        ([1], 1),
        ([-1], -1),
        ([-1, -1], -1),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6), 
        ([1, 2, 3, 4, 5], 15),
        ([1, 2, -1, -1, -1, 3, 4, 5], 12),
        ([1, 2, -1, -1, 3, 4, 5], 13)
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().maxSubArray(test_case[0])
        print('output:', output)
        assert output == test_case[1]


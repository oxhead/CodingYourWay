"""
https://leetcode.com/problems/house-robber

Related:
  - lt_152_maximum-product-subarray
  - lt_213_house-robber-ii
  - lt_256_paint-house
  - lt_276_paint-fence
  - lt_337_house-robber-iii
  - lt_600_non-negative-integers-without-consecutive-ones
  - lt_656_coin-path
  - lt_740_delete-and-earn
"""

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        # Hints:
        # 1) Two cases: either rob the current house i (nums[i] + dp[i - 2] or not to rob (dp[i-1]_
        if not nums or len(nums) == 0: return 0
        elif len(nums) == 1: return nums[0]

        max_previous = nums[0]
        max_current = max(max_previous, nums[1])

        for i in range(2, len(nums)):
            max_previous, max_current = max_current, max(nums[i] + max_previous, max_current)
        return max_current

    def rob_dp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        if not nums and len(nums) == 0: return 0
        elif len(nums) < 2: return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]


if __name__ == '__main__':
    test_cases = [
        ([], 0),
        ([1], 1),
        ([1, 2, 3], 4),
        ([2, 1, 1, 2], 4),
        ([0, 3, 5, 4, 1, 0], 7)
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().rob(test_case[0])
        print('output:', output)
        assert output == test_case[1]


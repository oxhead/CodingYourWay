"""
https://leetcode.com/problems/house-robber-ii

Related:
  - lt_198_house-robber
  - lt_256_paint-house
  - lt_276_paint-fence
  - lt_337_house-robber-iii
  - lt_600_non-negative-integers-without-consecutive-ones
  - lt_656_coin-path
"""

"""
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        if not nums: return 0
        elif len(nums) == 1: return nums[0]
        
        dp1 = [0] * len(nums)
        dp1[0] = nums[0]
        dp1[1] = max(nums[:2])
        for i in range(2, len(nums) - 1):
            dp1[i] = max(nums[i] + dp1[i - 2], dp1[i - 1])

        dp2 = [0] * len(nums)
        dp2[0] = 0
        dp2[1] = nums[1] 
        for i in range(2, len(nums)):
            dp2[i] = max(nums[i] + dp2[i - 2], dp2[i - 1])
        return max(dp1[-2], dp2[-1])


if __name__ == '__main__':
    test_cases = [
        ([], 0),
        ([1], 1),
        ([1, 2, 3], 3),
        ([2, 1, 1, 2], 3),
        ([0, 3, 5, 4, 1, 0], 7),
        ([1, 2, 1, 1], 3),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().rob(test_case[0])
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/4sum

Related:
  - lt_1
  - lt_15
  - lt_18
  - lt_454

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # https://www.tangjikai.com/algorithms/leetcode-18-4sum
        nums.sort()
        return [list(x) for x in set(Solution.kSum(nums, target, 4))]

    @staticmethod
    def kSum(nums, target, k):
        if k == 2:
            left = 0
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    yield (nums[left], nums[right])
                    left += 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
        else:
            left = 0
            while left < len(nums) - k + 1:
                for sub in Solution.kSum(nums[left+1:], target - nums[left], k - 1):
                    yield (nums[left],) + sub
                left += 1

if __name__ == '__main__':
    test_cases = [
        (([1, 0, -1, 0, -2, 2], 0), [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().fourSum(*test_case[0])
        print('output:', output)
        assert sorted([sorted(x) for x in output]) == sorted([sorted(x) for x in test_case[1]])


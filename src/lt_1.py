"""
https://leetcode.com/problems/two-sum

Related:
  - lt_15_3sum
  - lt_18_4sum
  - lt_167_two-sum-ii-input-array-is-sorted
  - lt_170_two-sum-iii-data-structure-design
  - lt_560_subarray-sum-equals-k
  - lt_653_two-sum-iv-input-is-a-bst
"""

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time: O(n)
        # Space: O(n)
        records = {}
        for i, n in enumerate(nums):
            if n in records:
                return [records[n], i]
            records[target - n] = i
        return []

    def twoSum_naive(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time: O(n^2)
        # Space: O(1)
        # time limit exceeded
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum_sort(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time: O(nlogn)
        # Space: O(n)
        data = [n for n in nums]
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [data.index(nums[left]), data.index(nums[right])]
            elif nums[left] + nums[right] < 0:
                left += 1
            else:
                right -= 1
        return []


if __name__ == '__main__':
    test_cases = [
        (([2, 7, 11, 15], 9), [0, 1]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().twoSum(*test_case[0])
        print('output:', output)
        assert sorted(output) == sorted(test_case[1])


"""
https://leetcode.com/problems/first-missing-positive

Related:
  - lt_268_missing-number
  - lt_287_find-the-duplicate-number
  - lt_448_find-all-numbers-disappeared-in-an-array
  - lt_765_couples-holding-hands
"""

"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        # https://www.cnblogs.com/AnnieKim/archive/2013/04/21/3034631.html
        # https://github.com/algorhythms/LeetCode/blob/master/040%20First%20Missing%20Positive.py
        if not nums: return 1
        i = 0
        while i < len(nums):
            if nums[i] <= 0 or nums[i] > len(nums) or nums[nums[i] - 1] == nums[i]:
                i += 1
            else:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return nums[-1] + 1

    def firstMissingPositive_failed(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        default_n = 0
        for n in nums:
            if n > 0:
                default_n = n
                break
        if default_n == 0: return 1

        for i in range(len(nums)):
            if nums[i] < 0: nums[i] = default_n
        print(nums)

        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
        print('#', nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1

if __name__ == '__main__':
    test_cases = [
        ([2], 1),
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([1, 2, 1, 4], 3),
        ([1, 2, 3], 4),
        ([1, 2, 3, -1], 4),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().firstMissingPositive(test_case[0])
        print('output:', output)
        assert output == test_case[1]


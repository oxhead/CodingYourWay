"""
https://leetcode.com/problems/jump-game

Related:
"""

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_position = 0
        for i, n in enumerate(nums[:-1]):
            if max_position < i: break
            max_position = max(max_position, i + n)
        return max_position >= len(nums) - 1

    def canJump_reverse(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_position = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= max_position:
                max_position = i
        return max_position == 0


if __name__ == '__main__':
    test_cases = [
        ([0], True),
        ([2, 0], True),
        ([0, 2, 3], False),
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().canJump(test_case[0])
        print('output:', output)
        assert output == test_case[1]

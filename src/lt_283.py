"""
https://leetcode.com/problems/move-zeroes

Related
lt_27
"""

"""
 Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

 For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

 Note:

         You must do this in-place without making a copy of the array.
             Minimize the total number of operations.

"""
import copy
import functools

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index_zero = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[index_zero] = nums[index_zero], nums[i]
                index_zero += 1

    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # if the current element is zero then do swap (__cmp__ < 0)
        # else do nothing
        nums.sort(key=functools.cmp_to_key(lambda x, y: 0 if y else -1))


if __name__ == '__main__':
    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([1, 0, 0, 0, 0], [1, 0, 0, 0, 0]),
        ([0, 0, 0, 0, 1], [1, 0, 0, 0, 0]),
        ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
        ([0, -1, 0, -3, -12], [-1, -3, -12, 0, 0])
    ]

    for test_case in test_cases:
        print('case:', test_case)
        nums = copy.copy(test_case[0])
        Solution().moveZeroes(nums)
        print('output:', nums)
        assert nums == test_case[1]


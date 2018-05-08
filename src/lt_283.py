"""
https://leetcode.com/problems/move-zeroes

Related:
  - lt_27_https://leetcode.com/problems/remove-element
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
        # Time: O(n)
        # Space: O(1)
        # Hints:
        # 1) index_zero starts from 0 (move non-zero elements to the front)
        # 2) increment index_zero for each movement (non-zero elements) 
        index_zero = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[index_zero] = nums[index_zero], nums[i]
                index_zero += 1

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # if the current element is zero then do swap (__cmp__ < 0)
        # else do nothing
        nums.sort(key=functools.cmp_to_key(lambda x, y: 0 if y else -1))

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for i, n in enumerate(nums):
            if n != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1

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


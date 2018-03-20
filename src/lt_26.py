"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array

Related:
  - lt_27_remove-element
"""

"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.

"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        if not nums: return 0
        if len(nums) <= 1: return len(nums)

        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        return index+1

        
if __name__ == '__main__':
    test_cases = [
        ([1], [1]),
        ([1, 1, 2], [1, 2]),
        ([1, 1, 2, 2], [1, 2]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 2, 2, 3, 3, 3, 4, 5, 5, 6], [1, 2, 3, 4, 5, 6]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        sol = Solution()
        test_input = [n for n in test_case[0]]
        output = sol.removeDuplicates(test_input)
        print('output:', output)
        print('nums:', test_input[:len(test_case[1])])
        assert output == len(test_case[1])
        assert test_input[:len(test_case[1])] == test_case[1]


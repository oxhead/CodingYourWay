"""
https://leetcode.com/problems/sort-colors

Related:
  - lt_148
  - lt_280
  - lt_324

Complexity:
  - Time:
  - Space:
"""

"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        RED, WHITE, BLUE = 0, 1, 2
        left, mid, right = 0, 0, len(nums) - 1
        while mid <= right:
            if nums[mid] == RED:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == WHITE:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1

    def sortColors_twopass(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        counter = {0: 0, 1: 0, 2: 0}
        for n in nums:
            counter[n] += 1
        for i in range(counter[0]):
            nums[i] = 0
        for i in range(counter[1]):
            nums[counter[0] + i] = 1
        for i in range(counter[2]):
            nums[counter[0] + counter[1] + i] = 2

if __name__ == '__main__':
    test_cases = [
        ([0], [0]),
        ([0, 1, 2, 0, 1, 2], [0, 0, 1, 1, 2, 2]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        nums = test_case[0]
        Solution().sortColors(nums)
        print('output:', nums)
        assert nums == test_case[1]


"""
https://leetcode.com/problems/remove-element

Related:
  - lt_26_remove-duplicates-from-sorted-array
  - lt_203_remove-linked-list-elements
  - lt_283_move-zeroes
"""

"""
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
"""

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        if not nums: return 0
        elif len(nums) == 1: return 0 if nums[0] == val else 1
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1 
            else:
                left += 1
        return right + 1
        
if __name__ == '__main__':
    test_cases = [
        (([], 3), []),
        (([3], 3), []),
        (([1], 3), [1]),
        (([3, 3], 3), []),
        (([3, 2, 2, 3], 3), [2, 2]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        sol = Solution()
        nums = [n for n in test_case[0][0]]
        val = test_case[0][1]
        output = sol.removeElement(nums, val)
        print('output:', output)
        assert output == len(test_case[1])
        assert sorted(nums[:output]) == sorted(test_case[1])


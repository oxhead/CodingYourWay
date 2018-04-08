"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

Related:
  - lt_33_search-in-rotated-sorted-array
  - lt_154_find-minimum-in-rotated-sorted-array-ii
"""

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(logn)
        # Space: O(1)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

    def findMin_verbose(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(logn)
        # Space: O(1)
        if len(nums) <= 2: return min(nums)
        left, right = 0, len(nums) - 1
        mid = left + (right - left) // 2
        if nums[left] <= nums[mid]:
            return min(nums[left], self.findMin(nums[mid+1:]))
        else:
            return min(self.findMin(nums[:mid]), nums[mid])


if __name__ == '__main__':
    test_cases = [
        ([1], 1),
        ([4, 5, 6, 7, 8, 1, 2, 3], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findMin(test_case[0])
        print('output:', output)
        assert output == test_case[1]


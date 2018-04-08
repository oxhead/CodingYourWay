"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii

Related:
  - lt_153_find-minimum-in-rotated-sorted-array
"""

"""
    Follow up for "Find Minimum in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(logn), and O(n) in the worst case
        # Space: O(1)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

    def findMin_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[left] < nums[right]:
                right = mid - 1
            elif nums[left] == nums[right]:
                right -= 1
            else:
                if nums[mid] >= nums[left]:
                    left = mid + 1
                else: 
                    right = mid
        return nums[left]
        

if __name__ == '__main__':
    test_cases = [
        ([1], 1),
        ([1, 1], 1),
        ([1, 1, 1, 1, 1], 1),
        ([3, 1], 1),
        ([3, 1, 3], 1),
        ([1, 3, 1, 1, 1], 1),
        ([4, 5, 6, 7, 8, 1, 2, 3], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findMin(test_case[0])
        print('output:', output)
        assert output == test_case[1]


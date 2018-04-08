"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii

Related:
  - lt_33_search-in-rotated-sorted-array
"""

"""
    Follow up for "Search in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.
"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # Time: O(logn) on average and O(n) for the worst case 
        # Space: O(1)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return True
            elif nums[left] == nums[mid]:
                left += 1
            elif nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

        

if __name__ == '__main__':
    test_cases = [
        (([1], 1), True),
        (([1], 2), False),
        (([3, 1], 1), True),
        (([3, 1], 3), True),
        (([1, 3, 1, 1, 1], 3), True),
        (([1, 1, 1, 3, 1], 3), True),
        (([4, 5, 6, 7, 8, 1, 2, 3], 8), True),
        (([4, 5, 6, 7, 0, 1, 2], 4), True),   
        (([4, 5, 6, 7, 0, 1, 2], 5), True),
        (([4, 5, 6, 7, 0, 1, 2], 6), True),
        (([4, 5, 6, 7, 0, 1, 2], 7), True),
        (([4, 5, 6, 7, 0, 1, 2], 0), True),
        (([4, 5, 6, 7, 0, 1, 2], 1), True),
        (([4, 5, 6, 7, 0, 1, 2], 2), True),
        (([4, 5, 6, 7, 0, 1, 2], 3), False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().search(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/search-in-rotated-sorted-array

Related:
  - lt_81_search-in-rotated-sorted-array-ii
  - lt_153_find-minimum-in-rotated-sorted-array
"""

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Time: O(logn)
        # Space: O(1)
        # https://blog.csdn.net/wwh578867817/article/details/46592851
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # This is important to have <= here but not <
            elif nums[left] <= nums[mid]:
                if nums[left] <= target <=  nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def search_v2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Time: O(logn)
        # Space: O(1)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right - 1]:
                    left = mid + 1
                else:
                    right = mid
        return -1

    def search_naive(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(left, right):
            if left > right: return -1
            mid = left + (right - left) // 2
            if target < nums[mid]:
                return binary_search(left, mid - 1)
            elif target > nums[mid]:
                return binary_search(mid + 1, right)
            else: return mid
        point = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                point = i
                break
        index = binary_search(0, point)
        if index == -1:
            index = binary_search(point + 1, len(nums) - 1)
        return index


if __name__ == '__main__':
    test_cases = [
        (([1], 1), 0),
        (([1], 2), -1),
        (([3, 1], 1), 1),
        (([3, 1], 3), 0),
        (([4, 5, 6, 7, 8, 1, 2, 3], 8), 4),
        (([4, 5, 6, 7, 0, 1, 2], 4), 0),   
        (([4, 5, 6, 7, 0, 1, 2], 5), 1),
        (([4, 5, 6, 7, 0, 1, 2], 6), 2),
        (([4, 5, 6, 7, 0, 1, 2], 7), 3),
        (([4, 5, 6, 7, 0, 1, 2], 0), 4),
        (([4, 5, 6, 7, 0, 1, 2], 1), 5),
        (([4, 5, 6, 7, 0, 1, 2], 2), 6),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().search(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


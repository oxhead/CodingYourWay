"""
https://leetcode.com/problems/search-for-a-range

Related:
  - lt_278_first-bad-version
"""

"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4]. 
"""

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time: O(logn)
        # Space: O(1)
        def binary_search(nums, target, comparator):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if comparator(nums[mid], target):
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        left = binary_search(nums, target, lambda x, y: x >= y)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        right = binary_search(nums, target, lambda x, y: x > y)
        return [left, right - 1]

    def searchRange_linear(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time: O(n)
        # Space: O(1)
        index = [-1, -1]
        i = 0
        while i < len(nums):
            if nums[i] == target:
                if index[0] == -1:
                    index[0] = index[1] = i
                else:
                    index[1] = i
            i += 1
        return index


if __name__ == '__main__':
    test_cases = [
        (([1], 1), [0, 0]),
        (([5, 7, 7, 8, 8, 10], 8), [3, 4]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        VERSION = test_case[1]
        output = Solution().searchRange(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


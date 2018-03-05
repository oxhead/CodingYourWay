"""
https://leetcode.com/problems/find-peak-element

Related:

Complexity:
  - Time:
  - Space:
"""

"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.
Note:

Your solution should be in logarithmic complexity.
"""

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://shenjie1993.gitbooks.io/leetcode-python/162%20Find%20Peak%20Element.html
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 1], 2),
        ([1, 2, 3, 4], 3),
        ([4, 3, 2, 1], 0),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findPeakElement(test_case[0])
        print('output:', output)
        assert output == test_case[1]


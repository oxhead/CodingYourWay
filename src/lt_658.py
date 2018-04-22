"""
https://leetcode.com/problems/search-for-a-range

Related:
  - lt_374_guess-number-higher-or-lower
  - lt_375_guess-number-higher-or-lower-ii
  - lt_719_find-k-th-smallest-pair-distance
"""

"""
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:

Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:

Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]

Note:

    The value k is positive and will always be smaller than the length of the sorted array.
    Length of the given array is positive and will not exceed 104
    Absolute value of elements in the array and x will not exceed 104
"""

class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # Time: O(nlogn + k)
        # Space: O(1)
        def binary_search(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target: left = mid + 1
                else: right = mid - 1
            return left
        if k >= len(arr): return arr
        index = binary_search(arr, x)
        index = len(arr) - 1 if index >= len(arr) else index
        left, right = index-1, index
        for _ in range(k):
            if left >= 0 and right < len(arr):
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    left -= 1
                else:
                    right += 1
            elif left >= 0:
                left -= 1
            else:
                right += 1
        return arr[left+1:right]
        

if __name__ == '__main__':
    test_cases = [
        (([1, 2, 3, 4, 5], 4, 3), [1, 2, 3, 4]),
        (([1, 2, 3, 4, 5], 4, -1), [1, 2, 3, 4]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findClosestElements(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


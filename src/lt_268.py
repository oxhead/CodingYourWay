"""
https://leetcode.com/problems/missing-number

Related:
  - lt_41_first-missing-positive
  - lt_136_single-number
  - lt_287_find-the-duplicate-number
  - lt_765_couples-holding-hands

"""

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2

Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8


Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)

    def missingNumber_bit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # xor each element for getting the number with odd occurance
        # 0 can be ignored
        # input:    0 1   3
        # correct:    1 2 3
        # xor:      0 0 2 0
        result = 0
        for i, n in enumerate(nums):
            result ^= (i+1) ^ nums[i]
        return result

    def missingNumber_binarysearch(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(nlogn) if nums is not sorted
        # O(logn) if nums is sorted
        nums = sorted(nums)
        left = 0
        right = len(nums)
        mid = (left + right ) // 2
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > mid: right = mid
            else: left = mid + 1
        return left


if __name__ == '__main__':
    test_cases = [
        ([3, 0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        #output = Solution().missingNumber(test_case[0])
        #output = Solution().missingNumber_xor(test_case[0])
        output = Solution().missingNumber_binarysearch(test_case[0])
        print('output:', output)
        assert output == test_case[1]


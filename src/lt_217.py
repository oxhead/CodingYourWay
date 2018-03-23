"""
https://leetcode.com/problems/contains-duplicate

Related:
  - lt_219_contains-duplicate-ii
  - lt_220_contains-duplicate-iii
"""

"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct. 
"""

from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        return len(nums) > len(set(nums))


if __name__ == '__main__':
    test_cases = [
        ([1, 1], True),
        ([1, 1, 2], True),
        ([1], False),
        ([1, 2], False)
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().containsDuplicate(test_case[0])
        print('output:', output)
        assert output == test_case[1]


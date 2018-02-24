"""
https://leetcode.com/problems/contains-duplicate

Related:
  - lt_219
  - lt_220

Complexity:
  - Time: O(n)
  - Space: O(n)
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
        return len(nums) > len(set(nums))

    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        for count in counter.values():
            if count > 1: return True
        return False


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


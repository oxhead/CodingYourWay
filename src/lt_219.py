"""
https://leetcode.com/problems/contains-duplicate-ii

Related:
  - lt_217_contains-duplicate
  - lt_220_contains-duplicate-iii
"""

"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        records = {}
        for i, n in enumerate(nums):
            if n not in records:
                records[n] = i
            else:
                if i - records[n] <= k:
                    return True
                records[n] = i
        return False

    def containsNearbyDuplicate_TLE(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k > len(nums): k = len(nums)
        print('@', k)
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and j < i + k + 1:
                if nums[i] == nums[j]: return True
                j += 1
            i += 1
        return False



if __name__ == '__main__':
    test_cases = [
        #(([], 0), False),
        #(([1, 2, 1, 1, 2, 3, 1], 2), True),
        (([1, 2, 3, 4, 5, 1], 2), False),
        (([99, 99], 2), True),
        (([-1, -1], 1), True),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().containsNearbyDuplicate(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


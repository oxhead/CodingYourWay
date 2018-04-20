"""
https://leetcode.com/problems/contains-duplicate-iii

Related:
  - lt_217_contains-duplicate
  - lt_219_contains-duplicate-ii
"""

"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k. 
"""

import collections

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        # https://github.com/kamyu104/LeetCode/blob/master/Python/contains-duplicate-iii.py
        if k < 0 or t < 0: return False
        window = collections.OrderedDict()
        for n in nums:
            if len(window) > k:
                window.popitem(last=False)
            bucket = n if t == 0 else n // t
            for m in (window.get(bucket - 1), window.get(bucket), window.get(bucket + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            window[bucket] = n
        return False

    def containsNearbyAlmostDuplicate_sort(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # Time: O(n * logn)
        # Space: O(n)
        indexs = sorted(range(len(nums)), key=lambda i: nums[i])
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums) and nums[indexs[j]] - nums[indexs[i]] <= t:
                if abs(indexs[i] - indexs[j]) <= k:
                    return True
                j += 1
        return False


if __name__ == '__main__':
    test_cases = [
        (([1, 2], 1, 1), True),
        (([1, 2], 1, 2), True),
        (([1, 2], 2, 1), True),
        (([1, 3], 1, 1), False),
        (([-3, 3], 2, 4), False),
        (([1, 2, 3, 4, 5, 1, 2, 3, 4, 5], 2, 3), True),
        (([1, 2, 1, 2, 1, 2, 1, 2], 1, 0), False),
        (([3, 8, 4, 8, 3, 8], 1, 3), False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().containsNearbyAlmostDuplicate(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


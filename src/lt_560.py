"""
https://leetcode.com/problems/subarray-sum-equals-k

Related:
  - lt_1_2sum
  - lt_523_continuous-subarray-sum
  - lt_713_subarray-product-less-than-k
  - lt_724_find-pivot-index
"""

"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Note:

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

import collections

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        records = collections.defaultdict(int)
        total = 0
        count = 0
        records[0] += 1
        for n in nums:
            total += n
            count += records[total - k]
            records[total] += 1
        return count

    def subarraySum_bruteforce(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(1)
        if not nums: return 0

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        count = 0
        for i in range(len(nums)):
            if nums[i] == k: count += 1
            for j in range(i):
                if nums[i] - nums[j] == k: count += 1
        return count

if __name__ == '__main__':
    test_cases = [
        (([1], 0), 0),
        (([1, 1, 1], 2), 2),
        (([1, 2, 3, 1, 2, 2, 1, 3, 1, 4, 2], 4), 5),
        (([-1, -1, 1], 0), 1),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().subarraySum(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


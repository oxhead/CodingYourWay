"""
https://leetcode.com/problems/subarray-product-less-than-k

Related:
  - lt_152_maximum-product-subarray
  - lt_325_maximum-size-subarray-sum-equals-k
  - lt_560_subarray-sum-equals-k
"""

"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:

Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:
0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        if k <= 1: return 0
        count, prod, start = 0, 1, 0
        for i, n in enumerate(nums):
            prod *= n
            while prod >= k:
                prod //= nums[start]
                start += 1
            count += i - start + 1
        return count

    def numSubarrayProductLessThanK_naive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(1)
        count = 0
        for i, n in enumerate(nums):
            if n < k: count += 1
            for j in range(i - 1, -1, -1):
                n *= nums[j]
                if n >= k: break
                count += 1
        return count
        

if __name__ == '__main__':
    test_cases = [
        (([1], 1), 0),
        (([1, 2, 3], 0), 0),
        (([10, 5, 2, 6], 100), 8),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().numSubarrayProductLessThanK(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


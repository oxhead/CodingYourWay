"""
https://leetcode.com/problems/range-sum-query-immutable

Related:
  - lt_304_range-sum-query-2d-immutable
  - lt_307_range-sum-query-mutable
  - lt_325_maximum-size-subarray-sum-equals-k
"""

"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:

    You may assume that the array does not change.
    There are many calls to sumRange function.
"""

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # Time: O(n)
        # Space: O(n)
        self.cum_sum = [0]
        for n in nums:
            self.cum_sum.append(self.cum_sum[-1] + n)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # Time: O(1)
        return self.cum_sum[j + 1] - self.cum_sum[i]


class NumArray_TLE:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.dp = [[None] * len(nums) for _ in range(len(nums))]
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.dp[i][j] != None:
            return self.dp[i][j]
        if i == j: return self.nums[i]
        elif j - i == 1:
            self.dp[i][j] = sum(self.nums[i:j+1])
            return self.dp[i][j]
        k = (i + j) // 2
        self.dp[i][j] = self.sumRange(i, k) + self.sumRange(k + 1, j)
        return self.dp[i][j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    test_cases = [
        (([-2, 0, 3, -5, 2, -1], [(0, 2), (2, 5), (0, 5)]), [1, -1, -3]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        obj = NumArray(test_case[0][0])
        for index_pair, expected_result in zip(test_case[0][1], test_case[1]):
            output = obj.sumRange(*index_pair)
            print('output:', index_pair, output)
            assert output == expected_result


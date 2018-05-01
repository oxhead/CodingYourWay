"""
https://leetcode.com/problems/longest-increasing-subsequence

Related:
  - lt_334_increasing-triplet-subsequence
  - lt_354_russian-doll-envelopes
  - lt_646_maximum-length-of-pair-chain
  - lt_673_number-of-longest-increasing-subsequence
  - lt_712_minimum-ascii-delete-sum-for-two-strings
"""

"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity? 
"""

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleMedium/300.html
        # Time: O(nlogn)
        # Space: O(n)
        # Approaches:
        # (1) Bruteforce
        # (2) DP
        # (3) Binary Search (similar to intersion sort?)
        # Hint: Find the index over previous elements where x >= target
        # Example: [10, 9, 2, 5, 3, 7, 101, 18]
        # i  n    results           LIS
        # 0   10  [10]              1
        # 1    9  [9]               1
        # 2    2  [2]               1
        # 3    5  [2, 5]            2
        # 4    3  [2, 3]            2
        # 5    7  [2, 3, 7]         3
        # 6  101  [2, 3, 7, 101]    4
        # 7   18  [2, 3, 7, 18]     4
        def binary_search(data, val):
            left = 0
            right = len(data) - 1
            while left < right:
                mid = (left + right) >> 1
                if val == data[mid]: return mid
                elif val < data[mid]: right = mid
                else: left = mid + 1
            return left

        if not nums: return 0
        elif len(nums) <= 1: return len(nums)

        max_val = 0x7FFFFFFF
        results = [max_val] * len(nums)
        for i in range(len(nums)):
            index = binary_search(results, nums[i])
            results[index] = nums[i]
        return len([n for n in results if n != max_val]) 

    def lengthOfLIS_dp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleMedium/300.html
        # time limit exceeded 
        # O(n^2)
        if not nums or len(nums) < 1: return 0
        dp = [0] * len(nums)
        dp[0] = 1

        current_max = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
                else:
                    dp[i] = max(1, dp[i])
            current_max = max(current_max, dp[i])        
        return current_max

    def lengthOfLIS_dp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(n)
        if not nums: return 0
        count = 1
        lis = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            c = lis[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    if  c + lis[j] > lis[i]: lis[i] = c + lis[j]
            count = max(count, lis[i])
        return count


if __name__ == '__main__':
    test_cases = [
        ([0], 1),
        ([2, 2], 1),
        ([10, 9, 2, 5, 3, 4], 3),
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().lengthOfLIS(test_case[0])
        print('output:', output)
        assert output == test_case[1]


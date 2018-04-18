"""
https://leetcode.com/problems/minimum-size-subarray-sum

Related:
  - lt_76_minimum-window-substring
  - lt_325_maximum-size-subarray-sum-equals-k
  - lt_718_maximum-length-of-repeated-subarray
"""

"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.
More practice:

If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = -1, 0
        min_length = float('inf')
        total = 0
        while right < len(nums):
            total += nums[right]
            while left < right and total >= s:
                min_length = min(min_length, right - left)
                left += 1
                total -= nums[left]
            right += 1
        return min_length if min_length != float('inf') else 0

    def minSubArrayLen_v2(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        min_length = float('inf')
        current_sum = 0
        left = 0
        for i, n in enumerate(nums):
            current_sum += n
            while current_sum >= s:
                min_length = min(min_length, i - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0

    def minSubArrayLen_v3(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        if not nums: return 0
        left, right = 0, 0
        current_sum = 0
        min_length = float('inf')
        while right < len(nums):
            while current_sum < s and right < len(nums):
                current_sum += nums[right]
                right += 1
            while current_sum >= s and left <= right:
                min_length = min(min_length, right - left)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0

    def minSubArrayLen_binarysearch(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(nlong)
        # Space: O(1)
        def binary_search(nums, left, right, target, comparator):
            while left < right:
                mid = left + (right - left) // 2
                if comparator(nums[mid], target):
                    left = mid + 1
                else:
                    right = mid
            return left
        if not nums: return 0
        sums = [n for n in nums]
        for i in range(1, len(sums)):
            sums[i] += sums[i - 1]
        min_length = float('inf')
        for i, n in enumerate(sums):
            index = binary_search(sums, i, len(sums), sums[i] - nums[i] + s, lambda x, y: x < y)
            if index < len(sums):
                min_length = min(min_length, index - i + 1)
        return min_length if min_length != float('inf') else 0

    def minSubArrayLen_failed(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        sums = [n for n in nums]
        for i in range(1, len(sums)):
            sums[i] += sums[i - 1]
        min_length = float('inf')
        left, right = 0, len(nums) - 1
        while left < right:
            if sums[right] - sums[left] >= s:
                min_length = min(min_length, right - left)
                if nums[left] <= nums[right]:
                    left += 1
                else:
                    right -= 1
            else:
                if nums[left] <= nums[right]:
                    right -= 1
                else:
                    left += 1
        return min_length if min_length < float('inf') else len(nums) if sum(nums) >= s else 0


if __name__ == '__main__':
    test_cases = [
        ((100, []), 0),
        ((3, [1, 1]), 0),
        ((7, [2, 3, 1, 2, 4, 3]), 2),
        ((15, [1, 2, 3, 4, 5]), 5),
        ((15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]), 2),
        ((213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]), 8),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().minSubArrayLen(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

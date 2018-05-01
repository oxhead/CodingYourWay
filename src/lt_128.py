"""
https://leetcode.com/problems/longest-consecutive-sequence

Related:
  - lt_298_binary-tree-longest-consecutive-sequence
"""

"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        # http://rainykat.blogspot.com/2017/01/leetcodefg-128-longest-consecutive.html
        # Hints:
        # 1) only maintain the farest range
        # Approaches:
        # 1) hash table
        # Examples:
        # 4 1 3 2
        # 1
        # 1 1
        # 2 1 2
        # 4 4 2 4 (no need to update element 3 because it's between 1 - 4
        records = {}
        max_length = 0
        for n in nums:
            if n in records: continue
            left = records[n-1] if n-1 in records else 0
            right = records[n+1] if n+1 in records else 0
            length = left + right + 1
            records[n] = length
            max_length = max(max_length, length)
            records[n - left] = length
            records[n + right] = length
        return max_length 


if __name__ == '__main__':
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([1, 2, 0, 1], 3),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().longestConsecutive(test_case[0])
        print('output:', output)
        assert output == test_case[1]


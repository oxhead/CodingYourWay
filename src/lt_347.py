"""
https://leetcode.com/problems/top-k-frequent-elements

Related:
  - lt_192_word-frequency
  - lt_215_kth-largest-element-in-an-array
  - lt_451_sort-characters-by-frequency
  - lt_659_split-array-into-consecutive-subsequences
  - lt_692_top-k-frequent-words
"""

"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

import collections

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Time: O(nlogn)
        # Space: O(n)
        counters = collections.Counter(nums)
        return sorted(counters.keys(), key=lambda x: counters[x], reverse=True)[:k]

    def topKFrequent_bucketsort(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Time: O(n)
        # Space: O(n)
        counters = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for i, count in counters.items():
            buckets[count].append(i)

        output = []
        for i in range(len(buckets) - 1, -1, -1):
            for j in range(len(buckets[i])):
                output.append(buckets[i][j])
                if len(output) == k: return output
        return output


if __name__ == '__main__':
    test_cases = [
        (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().topKFrequent(*test_case[0])
        print('output:', output)
        assert list(sorted(output)) == test_case[1]


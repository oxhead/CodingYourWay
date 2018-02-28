"""
https://leetcode.com/problems/top-k-frequent-elements

Related:
  - lt_192
  - lt_215
  - lt_451
  - lt_659
  - lt_692

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counters = {}
        for n in nums:
            if n not in counters:
                counters[n] = 0
            counters[n] += 1
        sorted_counters = sorted(counters.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in sorted_counters][:k]

if __name__ == '__main__':
    test_cases = [
        (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().topKFrequent(*test_case[0])
        print('output:', output)
        assert list(sorted(output)) == test_case[1]


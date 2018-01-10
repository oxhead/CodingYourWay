"""
https://leetcode.com/problems/majority-element

Related:
  - lt_229

Complexity:
  - Time: O(n)
  - Space: O(n)
"""

"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

import operator

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        return max(counts.items(), key=operator.itemgetter(1))[0]


if __name__ == '__main__':
    test_cases = [
        ([1], 1),
        ([1, 1, 2], 1),
        ([1, 1, 2, 1, 1], 1),
        ([1, 1, 1, 1, 1], 1)
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().majorityElement(test_case[0])
        print('output:', output)
        assert output == test_case[1]


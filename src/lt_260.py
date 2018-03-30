"""
https://leetcode.com/problems/single-number-iii

Related
  - lt_136_single-number
  - lt_137_single-number-ii
"""

"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:

    The order of the result is not important. So in the above example, [5, 3] is also correct.
    Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

import collections

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Time: O(n)
        # Space: O(1)
        # https://segmentfault.com/a/1190000004886431
        diff = 0
        for n in nums:
            diff ^= n
        # diff &= ~(diff - 1)
        # get the rightmost bit that is different in n1 and n2
        diff &= -diff

        n1, n2 = 0, 0
        for n in nums:
            # the diff above will separate n1 and n2
            if n & diff == 0: n1 ^= n
            else: n2 ^= n
        return [n1, n2]

    def singleNumber_hashmap(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        return [k for k, v in counter.items() if v == 1]
            

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 3, 4, 4], [1, 2]),
        ([-2, -2, 1, 1, -3, 0], [-3, 0]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().singleNumber(test_case[0])
        print('output:', output)
        assert sorted(output) == sorted(test_case[1])


"""
https://leetcode.com/problems/array-partition-i

Related:
"""

"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:

Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

Note:

    n is a positive integer, which is in the range of [1, 10000].
    All the integers in the array will be in the range of [-10000, 10000].
"""

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(nlogn)
        # Space: O(1)
        nums.sort()
        return sum(nums[::2])

    def arrayPairSum_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum([nums[i] for i in range(0, len(nums), 2)])


if __name__ == '__main__':
    test_cases = [
        ([1,4,3,2], 4),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().arrayPairSum(test_case[0])
        print('output:', output)
        assert output == test_case[1]


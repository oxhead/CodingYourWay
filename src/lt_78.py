"""
https://leetcode.com/problems/subsets

Related:
  - lt_8

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return [nums]
        sub = self.subsets(nums[1:])
        return sub + [[nums[0]] + x for x in sub]

    def subsets_sequential(sefl, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        for n in nums:
            output += [[n] + sub for sub in output]
        return output

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().subsets(test_case[0])
        print('output:', output)
        assert sorted([tuple(sorted(x)) for x in output]) == sorted([tuple(sorted(x)) for x in test_case[1]])


"""
https://leetcode.com/problems/permutations

Related:
  - lt_31
  - lt_47
  - lt_60
  - lt_77

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        elif len(nums) == 1: return [nums]
        elif len(nums) == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        else:
            output = []
            for i, n in enumerate(nums):
                output.extend([[n] + sub for sub in self.permute(nums[:i] + nums[i+1:])])
            return output


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().permute(test_case[0])
        print('output:', output)
        assert sorted([tuple(x) for x in output]) == sorted([tuple(x) for x in test_case[1]])


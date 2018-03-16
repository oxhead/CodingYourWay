"""
https://leetcode.com/problems/permutations

Related:
  - lt_31
  - lt_47
  - lt_60
  - lt_77
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

import itertools

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time: O(n * n!)
        # Space: O(n * n!)
        output = [[]]
        for n in nums:
            tmp = []
            print(n)
            print('before:', output)
            for sub in output:
                for i in range(len(sub) + 1):
                    tmp.append(sub[:i] + [n] + sub[i:])
            output = tmp
            print('after:', output)
        return output

    def permute_recursive(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time: O(n * n!)
        # Space: O(n)
        if not nums: return [[]]
        elif len(nums) == 1: return [nums]

        output = []
        for i in range(len(nums)):
            for sub in self.permute_recursive(nums[:i] + nums[i+1:]):
                output.append([nums[i]] + sub)
        return output

    def permute_verbose(self, nums):
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
                output.extend([[n] + sub for sub in self.permute_verbose(nums[:i] + nums[i+1:])])
            return output


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], None),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().permute(test_case[0])
        print('output:', output)
        assert sorted([tuple(x) for x in output]) == sorted([tuple(x) for x in itertools.permutations(test_case[0])])


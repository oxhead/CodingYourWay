"""
https://leetcode.com/problems/combination-sum

Related:
  - lt_17_letter-combinations-of-a-phone-number
  - lt_40_combination-sum-ii
  - lt_77_combinations
  - lt_216_combination-sum-iii
  - lt_254_factor-combinations
  - lt_377_combination-sum-iv
"""

"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:

[
  [7],
  [2, 2, 3]
]
"""

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Time: O(?)
        # Space: O(?)
        if target == 0: return [[]]
        elif not candidates: return []
        elif target < min(candidates): return []
        choices = []
        n = candidates[0]
        for i in range(target//n + 1):
            for sub in self.combinationSum(candidates[1:], target - n * i):
                choices.append([n for _ in range(i)] + sub)
        return choices


if __name__ == '__main__':
    test_cases = [
        #(([1], 1), [[1]]),
        (([2, 3, 6, 7], 7), [[7], [2, 2, 3]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().combinationSum(*test_case[0])
        print('output:', output)
        assert sorted(output) == sorted(test_case[1])


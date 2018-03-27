"""
https://leetcode.com/problems/combination-sum-ii

Related:
  - lt_39_combination-sum
"""

"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:

[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Time: O(?)
        # Space: O(?)
        def produce(nums, target, current, output):
            if target == 0:
                output.append(list(current))
                return
            for i, n in enumerate(nums):
                if i > 0 and nums[i] == nums[i-1]: continue
                if n > target: continue
                current.append(n)
                produce(nums[i+1:], target - n, current, output)
                current.pop()

        output = []
        candidates.sort()
        produce(candidates, target, [], output)
        return output
        

    def combinationSum2_TLE(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates and target > 0: return []
        elif target < 0: return [] 
        elif target == 0: return [[]]
        
        output = []
        candidates = sorted(candidates)
        for sub in self.combinationSum2(candidates[1:], target):
            output.append(sub)
        for sub in self.combinationSum2(candidates[1:], target - candidates[0]):
            output.append([candidates[0]] + sub)
        return [list(s) for s in set([tuple(sub) for sub in output])]
        

if __name__ == '__main__':
    test_cases = [
        (([1], 1), [[1]]),
        (([10, 1, 2, 7, 6, 1, 5], 8), [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().combinationSum2(*test_case[0])
        print('output:', output)
        assert sorted(output) == sorted(test_case[1])


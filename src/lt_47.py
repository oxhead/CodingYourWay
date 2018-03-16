"""
https://leetcode.com/problems/permutations-ii

Related:
  - lt_31_next-permutation
  - lt_46_permutations
  - lt_267_palindrome-permutation-ii
"""

"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:

[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time: O(n * n !)
        # Space: O(n)
        output = [[]]
        for n in nums:
            tmp = []
            for sub in output:
                for i in range(len(sub) + 1):
                    tmp.append(sub[:i] + [n] + sub[i:])
                    if i < len(sub) and sub[i] == n:
                        break
            output = tmp
        return output

    def permuteUnique_recursive(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time: O(n * n!)
        # Space: O(n)
        def generate(nums, current):
            if not nums:
                output.append(current)
            for i, n in enumerate(nums):
                if i - 1 >= 0 and nums[i - 1] == n:
                    continue
                generate(nums[:i] + nums[i+1:], [n] + current)
        output = []
        nums.sort()
        generate(nums, [])
        return output

    def permuteUnique_slow(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def generate(nums):
            if not nums: return []
            elif len(nums) == 1: return [nums]
            output = []
            for i in range(len(nums)):
                for sub in generate(nums[:i] + nums[i+1:]):
                    output.append([nums[i]] + sub)           
            return output
        output = generate(nums)
        return [list(s) for s in set([tuple(o) for o in output])]
        

if __name__ == '__main__':
    test_cases = [
        ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().permuteUnique(test_case[0])
        print('output:', output)
        assert sorted([tuple(x) for x in output]) == sorted([tuple(x) for x in test_case[1]])


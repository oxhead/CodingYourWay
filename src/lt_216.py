"""
https://leetcode.com/problems/combination-sum-iii

Related:
  - lt_39_combination-sum
"""

"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]


Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""

class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # Time: O(k * C(n, k))
        # Space: O(k)
        def build(nums, current, k, target):
            if len(current) == k and target == 0:
                output.append(list(current))
            else:
                for i, n in enumerate(nums):
                    if n > target: continue
                    current.append(n)
                    build(nums[i+1:], current, k, target - n)
                    current.pop()
        output = []
        nums = [i for i in range(1, 10)]
        build(nums, [], k, n) 
        return output


if __name__ == '__main__':
    test_cases = [
        ((3, 7), [[1,2,4]]),
        ((3, 9), [[1,2,6], [1,3,5], [2,3,4]]),
        ((2, 18), []), 
        ((3, 15), [[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().combinationSum3(*test_case[0])
        print('output:', output)
        assert sorted(output) == sorted(test_case[1])


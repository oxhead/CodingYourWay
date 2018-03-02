"""
https://leetcode.com/problems/combinations

Related:
  - lt_39
  - lt_46

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # https://shenjie1993.gitbooks.io/leetcode-python/077%20Combinations.html
        if k == 1: return [[n] for n in range(1, n + 1)]
        if n == k:
            return [sub + [n] for sub in self.combine(n - 1, k - 1)]
        else:
            return [sub + [n] for sub in self.combine(n - 1, k - 1)] + self.combine(n - 1, k)

if __name__ == '__main__':
    test_cases = [
        ((4, 2), [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().combine(*test_case[0])
        print('output:', output)
        assert sorted([tuple(sorted(x)) for x in output]) == sorted([tuple(sorted(x)) for x in test_case[1]])


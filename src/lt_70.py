"""
https://leetcode.com/problems/climbing-stairs

Related:
  - lt_746_min-cost-climbing-stairs
"""

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    def __init__(self):
        self.records = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        if not n: return 0
        elif n == 1: return 1
        elif n == 2: return 2
        dp = [0] * 3
        dp[0], dp[1] = 1, 2
        for _ in range(2, n):
            dp[2] = dp[1] + dp[0]
            dp[0], dp[1] = dp[1], dp[2]
        return dp[-1]

    def climbStairs_verbose(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return n if n > 0 else 0

        dp = [0, 1, 2]

        for i in range(3, n+1):
            dp.insert(i, dp[i-1] + dp[i-2])

        return dp[n]

    def climbStairs_recursive_dp(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1: return 0
        elif n == 1: return 1
        elif n == 2: return 2

        if n - 1 not in self.records:
            self.records[n-1] = self.climbStairs(n-1)
        if n - 2 not in self.records:
            self.records[n-2] = self.climbStairs(n-2)

        return self.records[n-1] + self.records[n-2]

    def climbStairs_recursive(self, n):
        """
        :type n: int
        :rtype: int
        """
        # exceed time limit
        if n < 1: return 0
        elif n == 1: return 1
        elif n == 2: return 2

        return self.climbStairs(n-1) + self.climbStairs(n-2)

        
if __name__ == '__main__':
    test_cases = [
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().climbStairs(test_case[0])
        print('output:', output)
        assert output == test_case[1]


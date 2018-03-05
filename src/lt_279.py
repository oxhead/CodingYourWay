"""
https://leetcode.com/problems/perfect-squares

Related:
  - lt_204
  - lt_264

Complexity:
  - Time:
  - Space:
"""

"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9. 
"""

import math

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # https://leetcode.com/problems/perfect-squares/discuss/71533/osqrtn-in-ruby-c-c
        while n % 4 == 0: n = n // 4
        if n % 8 == 7: return 4
        x = 0
        while x * x <= n:
           y = int(math.sqrt(n - x * x))
           if x*x + y*y == n:
               if x == 0 or y == 0: return 1
               else: return 2
           x += 1
        return 3

    def numSquares_dp1(self, n):
        """
        :type n: int
        :rtype: int
        """
        # https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleMedium/279.html
        # time limit exceeded
        dp = [0x7FFFFFFF for _ in range(n+1)]
        dp[0] = 0
        for i in range(n+1):
            j = 1
            while i + j*j <= n:
                dp[i + j*j] = min(dp[i + j*j], dp[i] + 1)
                j += 1
        return dp[n]

    def numSquares_dp2(self, n):
        """
        :type n: int
        :rtype: int
        """
        # https://www.youtube.com/watch?v=NFFM1G6xEfU
        dp = [0x7FFFFFFF for _ in range(n+1)]
        dp[0] = 0
        for i in range(n+1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]

if __name__ == '__main__':
    test_cases = [
        (1, 1),
        (4, 1),
        (12, 3),
        (13, 2),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().numSquares(test_case[0])
        print('output:', output)
        assert output == test_case[1]


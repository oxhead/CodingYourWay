"""
https://leetcode.com/problems/perfect-squares

Related:
  - lt_204
  - lt_264
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
        # Time: O(sqrt(n))
        # Space: O(1)
        # Hints:
        # 1) Lagrange's Four Square theorem
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

    def numSquares_dp(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time: O(n * sqrt(n))
        # Space: O(n)
        # Hints:
        # 1) dp[i] = d[i - j*j] + 1, for 1 <= i <= n, j <= sqrt(i)
        # Notice:
        # 1) TLE
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        return dp[-1] 

    def numSquares_dp_static(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time: O(n * sqrt(n))
        # Space: O(n)
        # https://leetcode.com/problems/perfect-squares/discuss/71512/Static-DP-C++-12-ms-Python-172-ms-Ruby-384-ms
        # Notice:
        # 1) TLE
        dp = [0]
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]

    def numSquares_bfs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        # https://leetcode.com/problems/perfect-squares/discuss/71475/Short-Python-solution-using-BFS
        # Approaches:
        # 1) Build a list of square numbers (<=n), e.g., [1, 4, 9] for 12
        # 2) Build a list of candidates, e.g., {12}
        # 2) Once there is a square equal to a number in the candidate list, we finf the minimum solution
        # 3) If not, update the candidates list with differences
        # Examples:
        # n = 2
        # ps = [1, 4, 9]
        # candidates = {12}
        # step 1:
        # candidates = {11, 8, 3}
        # count = 1 
        # step 2:
        # candidates = {10, 7, 4, 2}
        # count = 2
        # step 3:
        # found 4 in candidates, equal to 4 in ps
        # count = 3, return
       
        if n <= 1: return n
        ps = [i*i for i in range(1, int(math.sqrt(n))+1)] 
        candidates = {n}
        count = 0
        while candidates:
            count += 1
            tmp = set()
            for candidate in candidates:
                for square in ps:
                    if candidate == square: return count
                    # not sure when this case happens
                    # this line does not affect correctness but improves performance
                    if candidate < square:
                        break
                    tmp.add(candidate - square)
            candidates = tmp
        return count


if __name__ == '__main__':
    test_cases = [
        (1, 1),
        (4, 1),
        (5, 2),
        (6, 3),
        (7, 4),
        (12, 3),
        (13, 2),
        (100, 1),
        (474, 3),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().numSquares(test_case[0])
        print('output:', output)
        assert output == test_case[1]


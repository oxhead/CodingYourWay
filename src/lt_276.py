"""
https://leetcode.com/problems/paint-fence

Related:
  - lt_198_house-robber
  - lt_213_house-robber-ii
  - lt_256_paint-house
  - lt_265_paint-house-ii
"""

"""
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers. 
"""

class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        # Hints:
        # 1) two cases: same with the previous one or not
        # Examples:
        # n = 3, k = 3
        # fence   0  1  2
        # colors  3  9
        #               2 * (9 + 3)
        #                    9 = same with fence 1 = (k - 1) * dp[n - 1]
        #                        3 = different with fence 1 = (k - 1) * dp[n - 2]
        if n == 1: return k
        dp = [0] * n
        dp[0] = k
        dp[1] = (k - 1) * dp[0] + k
        for i in range(2, n):
            dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])
        return dp[-1]


if __name__ == '__main__':
    test_cases = [
        ((1, 1), 1),
        ((1, 2), 2),
        ((1, 3), 3),
        ((2, 1), 1),
        ((2, 2), 4),
        ((2, 3), 9),
        ((3, 3), 24),
        ((3, 1), 0),
        ((3, 2), 6),
        ((3, 3), 24),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().numWays(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


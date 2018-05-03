"""
https://leetcode.com/problems/unique-binary-search-trees

Related:
  - lt_95_unique-binary-search-trees-ii
"""

"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time: O(?)
        # Space: O(n^2)
        def build(start, end):
            if start >= end: return 1
            if dp[start][end]: return dp[start][end]

            count = 0
            for root_val in range(start, end + 1):
                count += build(start, root_val - 1) * build(root_val + 1, end)
            dp[start][end] = count
            return count
            
        dp = [[0] * n for _ in range(n)]
        return build(0, n - 1)

    def numTrees_math(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(n)
        # https://www.jianshu.com/p/a7cbbfcff9a0
        # f(5) = g(n1, [], [n2...n5]) +
        #        g(n2, [n1], [n3...n5]) +
        #        g(n3, [n1, n2], [n4, n5]) +
        #        g(n4, [n1...n3], [n5]) +
        #        g(n5, [n1...n4], [])
        #      = g(j) * g(i - j - 1) for i <= n, j < i
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]


if __name__ == '__main__':
    test_cases = [
        (3, 5),
        (19, 1767263190),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().numTrees(test_case[0])
        print('output:', output)
        assert output == test_case[1]


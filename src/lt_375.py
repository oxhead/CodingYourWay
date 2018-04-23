"""
https://leetcode.com/problems/guess-number-higher-or-lower-ii
https://leetcode.com/problems/guess-number-higher-or-lower

Related:
  - lt_294_flip-game-ii
  - lt_374_guess-number-higher-or-lower
  - lt_464_can-i-win
  - lt_658_find-k-closest-elements
"""

"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.

Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
"""

class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        # Time: O(n^2)
        # Space: O(n^2)
        # https://github.com/kamyu104/LeetCode/blob/master/Python/guess-number-higher-or-lower-ii.py
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n, 0, -1):
            for j in range(i + 1, n + 1):
                dp[i][j] = min(k + max(dp[i][k-1], dp[k+1][j]) for k in range(i, j))
        return dp[1][n]

    def getMoneyAmount_recursive(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(n^2)
        # https://www.hrwhisper.me/leetcode-guess-number-higher-lower-ii/
        def search(left, right):
            if left >= right: return 0
            if dp[left][right]: return dp[left][right]
            dp[left][right] = min(i + max(search(left, i - 1), search(i + 1, right)) for i in range(left, right + 1))
            return dp[left][right]
        dp = [[0] * (n+1) for _ in range(n + 1)] 
        return search(1, n)
        

if __name__ == '__main__':
    test_cases = [
        (1, 0),
        (3, 2),
        (10, 16),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().getMoneyAmount(test_case[0])
        print('output:', output)
        assert output == test_case[1]


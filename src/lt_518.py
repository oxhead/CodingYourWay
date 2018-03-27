"""
https://leetcode.com/problems/coin-change-2

Related:
  - lt_322_coin-change
"""

"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Note: You can assume that

    0 <= amount <= 5000
    1 <= coin <= 5000
    the number of coins is less than 500
    the answer is guaranteed to fit into signed 32-bit integer 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10] 
Output: 1
"""

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # Time: O(m * n), m = amount, n = len(coins)
        # Space: O(m)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for n in range(c, amount + 1):
                dp[n] += dp[n - c]
        return dp[-1]

    def change_failed(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        for n in range(amount + 1):
            for coin in coins:
                if coin + n <= amount:
                    dp[coin + n] = dp[n] + 1 
            print(n, dp)
        return dp[-1]

    def change_TLE(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        def search(coins, amount):
            if amount == 0: return 1
            count = 0
            for i, n in enumerate(coins):
                if n > amount: continue
                count += search(coins[i:], amount - n)
            return count 
        if not coins and amount > 0: return 0
        return search(coins, amount)


if __name__ == '__main__':
    test_cases = [
        ((5, [1, 2, 5]), 4),
        ((3, [2]), 0),
        ((10, [10]), 1),
        ((500, [3,5,7,8,9,10,11]), 35502874),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().change(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


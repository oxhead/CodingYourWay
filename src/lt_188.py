"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

Related:
  - lt_121_best-time-to-buy-and-sell-stock
  - lt_122_best-time-to-buy-and-sell-stock-ii
  - lt_123_best-time-to-buy-and-sell-stock-iii
"""

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # Time: O(k*n)
        # Space: O(k)
        # https://github.com/kamyu104/LeetCode/blob/master/Python/best-time-to-buy-and-sell-stock-iv.py
        # https://github.com/algorhythms/LeetCode/blob/master/188%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20IV.py
        def max_profit_unlimited(prices):
            max_profit = 0
            for i in range(1, len(prices)):
                max_profit += max(0, prices[i] - prices[i-1])
            return max_profit

        if not prices or len(prices) <= 1: return 0
        # avoid timeout
        if k >= len(prices) // 2:
            return max_profit_unlimited(prices)

        max_buy = [float('-inf')] * (k + 1)
        max_sell = [0] * (k + 1)
        for i, price in enumerate(prices):
            for j in range(1, min(k, i//2+1) + 1):
                max_buy[j] = max(max_buy[j], max_sell[j-1] - price)
                max_sell[j] = max(max_sell[j], max_buy[j] + price)
        return max_sell[k]


if __name__ == '__main__':
    test_cases = [
        ((2, [1]), 0),
        ((2,[1, 2]), 1),
        ((2,[2, 1]), 0),
        ((2,[3, 2, 4, 1]), 2),
        ((2,[3, 2, 1, 4, 2, 5, 6]), 7),
        ((2, [2, 1, 2, 0, 1]), 2),
        ((4, [5, 7, 2, 7, 3, 3, 5, 3, 0]), 9),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().maxProfit(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


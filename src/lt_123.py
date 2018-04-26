"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

Related:
  - lt_121_best-time-to-buy-and-sell-stock
  - lt_122_best-time-to-buy-and-sell-stock-ii
  - lt_188_best-time-to-buy-and-sell-stock-iv
  - lt_689_maximum-sum-of-3-non-overlapping-subarrays
"""

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        # https://github.com/kamyu104/LeetCode/blob/master/Python/best-time-to-buy-and-sell-stock-iii.py
        # https://blog.csdn.net/MebiuW/article/details/52764801
        buy_1, buy_2 = float('-inf'), float('-inf')
        sell_1, sell_2 = 0, 0
        for price in prices:
            buy_1 = max(buy_1, -price)
            sell_1 = max(sell_1, buy_1 + price)
            buy_2 = max(buy_2, sell_1 - price)
            sell_2 = max(sell_2, buy_2 + price)
            print(price, buy_1, sell_1, buy_2, sell_2)
        return sell_2

    def maxProfit_atmostk(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def max_profit(prices, k):
            max_buy = [float('-inf')] * (k + 1)
            max_sell = [0] * (k + 1)
            for i in range(len(prices)):
                for j in range(1, min(k, i//2+1) + 1):
                    max_buy[j] = max(max_buy[j], max_sell[j - 1] - prices[i])
                    max_sell[j] = max(max_sell[j], max_buy[j] + prices[i])
            return max_sell[k]

        if len(prices) >= 3: 
            return max_profit(prices, 2)
        else:
            return max_profit(prices, 1)

    def maxProfit_dp(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # https://www.jianshu.com/p/91f2359e69f4
        # https://www.tangjikai.com/algorithms/leetcode-123-best-time-to-buy-and-sell-stock-iii1 
        if not prices or len(prices) <= 1: return 0
        dp1 = [0] * len(prices)
        dp2 = [0] * len(prices)

        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            dp1[i] = max(dp1[i - 1], prices[i] - min_price)

        max_price = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            max_price = max(max_price, prices[i])
            dp2[i] = max(dp2[i + 1], max_price - prices[i])
        return max([d1 + d2 for d1, d2 in zip(dp1, dp2)])

    def maxProfit_TLE(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(1)
        def max_profit(start, end):
            min_price = float('inf')
            max_profit = 0
            for i in range(start, end + 1):
                min_price = min(min_price, prices[i])
                max_profit = max(max_profit, prices[i] - min_price)
            return max_profit
        profit = 0
        for i in range(len(prices)):
            profit = max(profit, max_profit(0, i) + max_profit(i + 1, len(prices) - 1))
        return profit

    def maxProfit_v2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_1 = buy_2 = float('-inf')
        sell_1 = sell_2 = 0
        for price in prices:
            if buy_1 < -price: buy_1 = -price
            if sell_1 < buy_1 + price: sell_1 = buy_1 + price
            if buy_2 < sell_1 - price: buy_2 = sell_1 - price
            if sell_2 < buy_2 + price: sell_2 = buy_2 + price
        return sell_2


if __name__ == '__main__':
    test_cases = [
        ([1], 0),
        ([1, 2], 1),
        ([2, 1], 0),
        ([1, 2, 3], 2),
        ([3, 2, 4, 1], 2),
        ([3, 2, 1, 4, 2, 5, 6], 7),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().maxProfit(test_case[0])
        print('output:', output)
        assert output == test_case[1]


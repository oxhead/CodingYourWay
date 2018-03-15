"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock

Related:
  - lt_53
  - lt_122
  - lt_123
  - lt_188
  - lt_309
"""

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:

Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:

Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = 0x7FFFFFFF
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit

    def maxProfit_verbose(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best_profit = 0
        if not prices or len(prices) < 1: return best_profit
        min_price =  prices[0]
        for i in range(1, len(prices)):
            if prices[i] > min_price:
                best_profit = max(best_profit, prices[i] - min_price)
            else:
                min_price = prices[i]
        return best_profit

    def maxProfit_naive(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # will exceed time limit
        best_profit = 0
        for i, n1 in enumerate(prices[:-1]):
            for j, n2 in enumerate(prices[i+1:][::-1]):
                current_profit = n2 - n1
                best_profit = current_profit if current_profit > best_profit else best_profit
        return best_profit


if __name__ == '__main__':
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 1, 2, 0, 1], 1),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().maxProfit(test_case[0])
        print('output:', output)
        assert output == test_case[1]


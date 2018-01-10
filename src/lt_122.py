"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

Related:
  - lt_121
  - lt_123
  - lt_188
  - lt_309
  - lt_714

Complexity:
  - Time:
  - Space:
"""

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(map(lambda n: max(prices[n+1] - prices[n], 0), range(len(prices)-1)))


if __name__ == '__main__':
    test_cases = [
        ([1], 0),
        ([1, 2], 1),
        ([2, 1], 0),
        ([3, 2, 4, 1], 2)
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().maxProfit(test_case[0])
        print('output:', output)
        assert output == test_case[1]


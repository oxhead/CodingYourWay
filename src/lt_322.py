'''
https://leetcode.com/problems/coin-change
'''
import sys

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        sols = [sys.maxsize-1] * (amount+1)
        sols[0] = 0

        for total in range(amount+1):
            for coin in coins:
                if (total + coin <= amount):
                    sols[total + coin] = min(sols[total+coin], sols[total] + 1)
                
        return -1 if sols[amount] == sys.maxsize-1 else sols[amount]



if __name__ == '__main__':
    test_cases = [
        ([25, 20, 5, 1], 127, 7),
        ([25, 20, 4, 1], 121, 6),
        ([50, 45, 10, 2], 3, -1),
        ([50, 45, 10, 2], 92, 3)
    ]

    for test_case in test_cases:
        coins, amount, expected = test_case
        result = Solution().coinChange(coins, amount)
        print(coins, amount, expected, result)
        assert result == expected

    
        

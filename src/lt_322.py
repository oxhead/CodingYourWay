"""
https://leetcode.com/problems/coin-change

Related:

Complexity:
  - Time: O()
  - Space: O()
"""

"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin. 
"""

import sys

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleMedium/322.html
        sols = [sys.maxsize-1] * (amount+1)
        sols[0] = 0

        for total in range(amount+1):
            for coin in coins:
                if (total + coin <= amount):
                    sols[total + coin] = min(sols[total+coin], sols[total] + 1)
                
        return -1 if sols[amount] == sys.maxsize-1 else sols[amount]

    def coinChange_search(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # much faster
        def search(amount, count, index):
            if amount == 0:
               self.output = min(self.output, count)
               return
            if amount < 0: return
            for i in range(index, len(coins)):
                # restric search space
                if coins[i] <= amount < coins[i] * (self.output - count):
                    search(amount - coins[i], count + 1, i) 
        self.output = float('inf')
        coins.sort(reverse=True)
        search(amount, 0, 0)
        return self.output if self.output < float('inf') else -1
        
if __name__ == '__main__':
    test_cases = [
        #(([1], 0), 0),
        #(([25, 20, 5, 1], 127), 7),
        (([25, 20, 4, 1], 121), 6),
        #(([50, 45, 10, 2], 3), -1),
        #(([50, 45, 10, 2], 92), 3),
        #(([176, 6, 366, 357, 484, 226, 1, 104, 160, 331], 5557), 13),
        #(([370,417,408,156,143,434,168,83,177,280,117], 9953), 24),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().coinChange(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

    
        

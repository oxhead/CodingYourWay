"""
https://leetcode.com/problems/min-cost-climbing-stairs

Related:
  - lt_70

Complexity:
  - Time:
  - Space:
"""

"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:

Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:

Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:

    cost will have a length in the range [2, 1000].
    Every cost[i] will be an integer in the range [0, 999].
"""

class Solution:
    def __init__(self):
        self.records = {0: 0, 1: 0}

    def minCostClimbingStairs(self, cost):
        dp = [0, 0, 0]
        for i in range(2, len(cost)+1):
            dp[2] = min(cost[i-2] + dp[0], cost[i-1] + dp[1])
            dp[0], dp[1] = dp[1], dp[2]
        return dp[2]

    def minCostClimbingStairs_recursive(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        return self.findCost(cost, len(cost))

    def findCost(self, cost, index):
        if index in self.records:
            return self.records[index]
        
        self.records[index] = min(cost[index-2] + self.findCost(cost, index-2),
                                  cost[index-1] + self.findCost(cost, index-1)) 

        return self.records[index]


if __name__ == '__main__':
    test_cases = [
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
        ([0, 0, 0, 0], 0),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().minCostClimbingStairs(test_case[0])
        print('output:', output)
        assert output == test_case[1]


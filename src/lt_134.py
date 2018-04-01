"""
https://leetcode.com/problems/gas-station

Related:
"""

"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""

class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        start, current_sum, total_sum = 0, 0, 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            current_sum += diff
            total_sum += diff
            if current_sum < 0:
                current_sum = 0
                start = i + 1
        if total_sum >= 0: return start
        else: return -1

    def canCompleteCircuit_TLE(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(n)
        for i in range(len(gas)):
            dp = [0] * len(gas)
            dp[0] = gas[i] - cost[i]
            if dp[0] < 0: continue
            for j in range(i+1, i + len(gas)):
                k = (j - i) % len(gas)
                dp[k] += dp[k-1] + (gas[j%len(gas)] - cost[j%len(gas)])
                if dp[k] < 0:
                    dp[-1] = -1
                    break
            if dp[-1] >= 0: return i
        return -1

if __name__ == '__main__':
    test_cases = [
        (([4], [5]), -1),
        (([1, 2], [2, 1]), 1),
        (([1, 2, 3], [3, 2, 1]), 1),
        (([1, 2, 3], [2, 2, 2]), 1),
        (([1, 2, 3], [1, 2, 3]), 0),
        (([1, 2, 3], [1, 2, 4]), -1),
        (([1, 2, 3, 3], [2, 1, 5, 1]), 3),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().canCompleteCircuit(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

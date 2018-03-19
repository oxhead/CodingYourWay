"""
https://leetcode.com/problems/burst-balloons

Related:
"""

"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""

class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n ^ 3)
        # Space: O(n ^ 2)
        # Explain (invariant):
        # 1. For the first burst at the i balloon: nums[i-1]*nums[i]*nums[i+1] 
        # 2. For the last burst at the i balloon: nums[-1]*nums[i]*nums[n]
        # dp[i][j]: the maximum coins between the ith and jth balloon (no burst previously)
        # dp[i][j] = max(dp[i][j], dp[i][k-1] + coins[i-1] * coins[k] * coins[j+1] + dp[k+1][r]), where i <= k <= j
        # i: left
        # j: right
        # k: mid
        # Algorithms:
        # nums =  [   1, 2, 3   ]
        # coins = [1, 1, 2, 3, 1]
        # num_balloons = 1
        #   left = 1
        #       right = 1 (=left + num_balloons - 1)
        #   left = 2
        #       right = 2
        #   left = 3
        #       right = 3
        # num_balloons = 2
        #   left = 1
        #       right = 2
        #           mid = 1, max(dp[1][2], dp[1][0] + coins[0] * coins[1] * coins[3] + dp[2][2]) 
        #           mid = 2, max(dp[1][2], dp[1][1] + coins[0] * coins[2] * coins[3] + dp[3][2])
        #   left = 2
        #       right = 3
        # num_balloons = 3
        #   left = 1
        #       right = 3

        coins = [1] + nums + [1]
        n = len(coins)
        dp = [[0] * n for _ in range(n)]
        for num_balloons in range(1, n-1):
            for left in range(1, n - num_balloons):
                # inclusive: [l x x x r],  k = 5
                right = left + num_balloons - 1
                for mid in range(left, right+1):
                    dp[left][right] = max(dp[left][right], dp[left][mid-1] + coins[left-1] * coins[mid] * coins[right+1] + dp[mid+1][right])
        for row in dp:
            print(row)
        return dp[1][-2]

    def maxCoins_recursive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n ^ 3)
        # Space: O(n ^ 2)
        coins = [1] + nums + [1]
        n = len(coins)
        dp = [[0] * n for _ in range(n)]
        def recursive(left, right):
            # already computed
            if dp[left][right] > 0: return dp[left][right]
            for mid in range(left, right + 1):
                dp[left][right] = max(dp[left][right], recursive(left, mid - 1) + coins[left - 1] * coins[mid] * coins[right + 1] + recursive(mid + 1, right))
            return dp[left][right]
        recursive(1, n - 2)
        return recursive(1, n - 2)

    def maxCoins2(self, nums):
        nums = [1] + nums + [1] # build the complete array 
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
    
        for gap in range(2, n):
            for i in range(n-gap):
                j = i + gap
                print(i, j)
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        for row in dp:
            print(row)
        return dp[0][n-1]

    def maxCoins_dp1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n ^ 3)
        # Space: O(n ^ 2)
        # https://github.com/algorhythms/LeetCode/blob/master/312%20Burst%20Balloons.py
        n = len(nums)
        def get(i):
            return nums[i] if 0 <= i < n else 1
        dp = [[0] * (n + 1) for _ in range(n + 1)] 
        for i in range(n + 1, -1, -1):
            for j in range(i + 1, n + 1):
                print(i, j)
                for k in range(i, j):
                    print('k={}'.format(k), dp[i][k], get(i - 1) * get(k) * get(j), dp[k + 1][j])
                dp[i][j] = max(dp[i][k] + get(i - 1) * get(k) * get(j) + dp[k + 1][j] for k in range(i, j))
        for row in dp:
            print(row)
        return max(map(max, dp))

    def maxCoins_failed(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        elif len(nums) == 1: return nums[0]
        counts = []
        while len(counts) < len(nums):
            records = {}
            print('#', nums)
            for i in range(len(nums)): 
                if nums[i] < 0:
                    continue
                left = -1
                for j in range(i - 1, -1, -1):
                    if nums[j] >= 0:
                        left = j
                        break
                right = -1
                for j in range(i + 1, len(nums)):
                    if nums[j] >= 0:
                        right = j
                        break
                n_prev = nums[left] if left >= 0 else 1
                n_next = nums[right] if right >= 0 else 1
                records[i] = n_prev * n_next
                print(i, left, right, records[i])
            print(len(counts), records)
            index_max, coins_max = -1, 0
            for index, coins in records.items():
                if coins > coins_max or (coins == coins_max and nums[index] < nums[index_max]):
                    index_max = index
                    coins_max = coins * nums[index]
            print('index:', index_max) 
            counts.append(coins_max)
            nums[index_max] = -1
        return sum(counts)


if __name__ == '__main__':
    test_cases = [
        #([3, 1, 5, 8], 167),
        #([9, 76, 64], 44416),
        ([1, 2, 3], 12),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().maxCoins(test_case[0])
        print('output:', output)
        assert output == test_case[1]


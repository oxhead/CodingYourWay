"""
https://leetcode.com/problems/consecutive-numbers-sum
"""

"""
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3

Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4

Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

Note: 1 <= N <= 10 ^ 9.
"""

class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Time: O(sqrt(N))
        # Space: O(1)
        count = 0
        for d in range(1, int((2 * N) ** 0.5) + 1):
            if (N - (d * (d - 1) / 2)) % d == 0: count += 1
        return count
        
    def consecutiveNumbersSum_v2(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        # Hints:
        # N = 15
        # N = n + (n + 1) + (n + 2) + ... + (n + d - 1)
        #   = n * d + d * (d - 1) / 2
        # valid d = {1, 4, 7, 15}
        # vaild d, where N - dsum > 0 and n*d % d == 0 (n is an integer)
        count = 0
        # if the qeustions ask at least two consecutive numbers,
        # we should start from 2 here
        for d in range(1, N + 1):
            dsum = d * (d - 1) / 2
            nd = N - dsum
            if nd <= 0: break
            if nd % d == 0: count += 1
        return count

    def consecutiveNumbersSum_twopointer(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(n)
        sums = [n for n in range(N + 1)]
        for i in range(1, len(sums)):
            sums[i] += sums[i-1]
        count = 0
        i, j = 0, 1
        while j <= N and j - i >= 1:
            total = sums[j] - sums[i]
            if total == N:
                count += 1
                j += 1
            elif total > N: i += 1
            else: j += 1
        return count

        
if __name__ == '__main__':
    test_cases = [
        (5, 2),
        (9, 3),
        (15, 4),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().consecutiveNumbersSum(test_case[0])
        print('output:', output)
        assert output == test_case[1]

"""
https://leetcode.com/problems/arranging-coins

Related:
"""

"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""

class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time: O(logn)
        # Space: O(1)
        if n == 0: return 0
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            total = (1 + mid) * mid // 2
            if total > n: right = mid - 1
            else: left = mid + 1 
        return left - 1


if __name__ == '__main__':
    test_cases = [
        (0, 0),
        (2, 1),
        (5, 2),
        (8, 3),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().arrangeCoins(test_case[0])
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/sqrtx

Related:
  - lt_50
  - lt_367

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.
"""

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1: return x
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            remaining = x // mid
            if remaining == mid: return mid
            elif remaining < mid: right = mid -1
            else: left = mid + 1
        return right

if __name__ == '__main__':
    test_cases = [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 2),
        (8, 2),
        (10, 3),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().mySqrt(test_case[0])
        print('output:', output)
        assert output == test_case[1]


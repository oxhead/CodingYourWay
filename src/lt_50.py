"""
https://leetcode.com/problems/powx-n

Related:
  - lt_69_sqrtx
  - lt_372_super-pow

"""

"""
Implement pow(x, n).

Example 1:

Input: 2.00000, 10
Output: 1024.00000

Example 2:

Input: 2.10000, 3
Output: 9.26100
"""

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Time: O(logn)
        # Space: O(1)
        m = abs(n)
        ans = 1
        while m > 0:
            if m & 1 == 1:
                ans *= x
            x *= x
            m >>= 1
        return ans if n >= 0 else 1 / ans

    def myPow_dp(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Time: O(logn)
        # Space: O(logn)
        def dp(n):
            if n in record:
                return record[n]
            else:
                if n == 1:
                    return x
                if n == 2:
                    record[n] = x * x
                elif n % 2 == 0:
                    record[n] = dp(n // 2) * dp(n // 2)
                else:
                    record[n] = x * dp(n // 2) * dp(n // 2)
                return record[n] 
        record = {}
        if n > 0:
            return dp(n)
        elif n < 0:
            return 1 / dp(-n)
        else:
            return 1


if __name__ == '__main__':
    test_cases = [
        ((2, 5), 32),
        ((2.00000, 10), 1024.00000),
        ((2.10000, 3), 9.26100),
        ((34.00515, -3), 0.0000254311)
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().myPow(*test_case[0])
        print('output:', output)
        assert abs(output - test_case[1]) <= 0.000000001


"""
https://leetcode.com/problems/valid-perfect-square
https://leetcode.com/problems/sqrtx

Related:
  - lt_69_sqrtx
  - lt_633_sum-of-square-numbers
"""

"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True

Example 2:

Input: 14
Returns: False
"""

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Time: O(logn)
        # Space: O(1)
        left, right = 1, num // 2 + 1
        while left <= right:
            mid = left + (right - left) // 2
            val = mid ** 2
            if val == num:
                return True
            elif val > num:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    test_cases = [
        (1, True),
        (2, False),
        (3, False),
        (4, True),
        (8, False),
        (10, False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isPerfectSquare(test_case[0])
        print('output:', output)
        assert output == test_case[1]


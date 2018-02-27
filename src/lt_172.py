"""
https://leetcode.com/problems/factorial-trailing-zeroes

Related:
  - lt_233

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""

class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n >= 5:
            count += n // 5
            n = n // 5
        return count

if __name__ == '__main__':
    test_cases = [
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 1),
        (25, 6),
        (30, 7),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().trailingZeroes(test_case[0])
        print('output:', output)
        assert output == test_case[1]


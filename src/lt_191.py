"""
https://leetcode.com/problems/number-of-1-bits

Related:
  - lt_190
  - lt_231
  - lt_338
  - lt_401
  - lt_461
  - lt_693
  - lt_762

Complexity:
  - Time:
  - Space:
"""

"""
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = []
        while n > 0:
            bits.append(n % 2)
            n = n // 2
            
        return sum(bits)

if __name__ == '__main__':
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (11, 3),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().hammingWeight(test_case[0])
        print('output:', output)
        assert output == test_case[1]


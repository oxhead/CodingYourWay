"""
https://leetcode.com/problems/count-primes

Related:
  - lt_263
  - lt_264
  - lt_279

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Description:

    Count the number of prime numbers less than a non-negative number, n.
"""

import math

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # https://github.com/algorhythms/LeetCode/blob/master/204%20Count%20Primes.py
        if n <= 2: return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        return sum(is_prime)

if __name__ == '__main__':
    test_cases = [
        (2, 0),
        (3, 1),
        (4, 2),
        (5, 2),
        (1500000, 114155),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().countPrimes(test_case[0])
        print('output:', output)
        assert output == test_case[1]


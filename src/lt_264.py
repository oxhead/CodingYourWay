"""
https://leetcode.com/problems/ugly-number-ii

Related:
  - lt_23_merge-k-sorted-lists
  - lt_204_count-primes
  - lt_263_ugly-number
  - lt_279_perfect-squares
  - lt_313_super-ugly-number
"""

"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
"""

import heapq

class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(?)
        heap = []
        heapq.heappush(heap, 1)
        for _ in range(n):
            ugly = heapq.heappop(heap)
            if ugly % 2 == 0:
                heapq.heappush(heap, ugly * 2)
            elif ugly % 3 == 0:
                heapq.heappush(heap, ugly * 2)
                heapq.heappush(heap, ugly * 3)
            else:
                heapq.heappush(heap, ugly * 2)
                heapq.heappush(heap, ugly * 3)
                heapq.heappush(heap, ugly * 5)
        return ugly

    def nthUglyNumber_TLE(self, n):
        """
        :type n: int
        :rtype: int
        """
        records = set()
        records |= set([1, 2, 3, 5])
        count = 0
        nth_num = 0
        num = 0
        while count < n:
            nth_num += 1
            num = nth_num
            for d in (2, 3, 5):
                while num % d == 0:
                    n_new = num // d
                    if n_new in records:
                        num = 1
                        break
                    num = n_new
            if num == 1:
                count += 1
                records.add(nth_num)
        return nth_num


if __name__ == '__main__':
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 8),
        (254, 40960),
        (1960, 6834375000),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().nthUglyNumber(test_case[0])
        print('output:', output)
        assert output == test_case[1]


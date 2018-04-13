"""
https://leetcode.com/problems/happy-number

Related:
  - lt_258_add-digits
  - lt_263_ugly-number
"""

"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1
"""

class Solution:
    def __init__(self):
        self.records = set()

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = sum([int(d) ** 2 for d in str(n)])
        if s == 1: return True
        else:
            if s in self.records: return False
            else:
                self.records.add(s)
                return self.isHappy(s)


    def isHappy_v2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def is_happy(n, records):
            if n in records: return False
            count = 0
            d = n
            while d > 0:
                count += (d % 10) ** 2
                d //= 10
            if count == 1: return True
            records[n] = count
            return is_happy(count, records)
        records = {}
        return is_happy(n, records)

if __name__ == '__main__':
    test_cases = [
        (19, True),
        (1, True),
        (0, False),
        (4, False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isHappy(test_case[0])
        print('output:', output)
        assert output == test_case[1]


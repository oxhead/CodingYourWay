"""
https://leetcode.com/problems/sum-of-two-integers

Related:
  - lt_2_add-two-numbers


Reference:
  - https://github.com/kamyu104/LeetCode/blob/master/Python/sum-of-two-integers.py

"""

"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
    Given a = 1 and b = 2, return 3. 
"""

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # Time: O(1)
        # Space: O(1)
        # https://github.com/kamyu104/LeetCode/blob/master/Python/sum-of-two-integers.py
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        #print('a: {0:032b}'.format(a & mask))
        #print('b: {0:032b}'.format(b & mask))
        while b:
            # use XOR to get different bits
            # use AND and left shift to get carry bits
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            #print('a: {0:032b}'.format(a))
            #print('b: {0:032b}'.format(b))
        # print('X: {0:032b}'.format(a))
        # ~: -x - 1
        # a ^ mask: x 
        return a if a <= MAX else ~(a ^ mask)


if __name__ == '__main__':
    test_cases = [
        ((1, 2), 3),
        ((1, -2), -1),
        ((-1, 2), 1),
        ((-1, -1), -2)
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().getSum(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


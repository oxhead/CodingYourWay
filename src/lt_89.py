"""
https://leetcode.com/problems/gray-code

Related:
  - lt_717_1-bit-and-2-bit-characters
"""

"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2

Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
"""

class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Time: O(2^n)
        # Space: O(1)
        result = [0]
        for i in range(n):
            for n in reversed(result):
                result.append(1 << i | n)
        return result


if __name__ == '__main__':
    test_cases = [
        (2, [0, 1, 3, 2]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().grayCode(test_case[0])
        print('output:', output)
        assert output == test_case[1]


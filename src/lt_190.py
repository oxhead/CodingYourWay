"""
https://leetcode.com/problems/reverse-bits

Related:
  - lt_191
"""

"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
    If this function is called many times, how would you optimize it?

    Related problem: Reverse Integer
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # Time: O(1)
        # Space: O(1)
        # https://github.com/algorhythms/LeetCode/blob/master/190%20Reverse%20Bits.py
        output = 0
        BITS = 32
        for i in range(BITS):
            # n % 2
            output += n & 1
            # the last bit does not need to multiply 2
            if i == BITS - 1: break
            output <<= 1
            n >>= 1
        return output

    def reverseBits_naive(self, n):
        output = [0] * 32
        index = -1
        while n:
            # b = n % 2
            b = n & 1
            # n = n // 1
            n = n >> 1
            output[index] = b
            index -= 1
        n_reversed = 0
        for i, b in enumerate(output):
            n_reversed += (2 << (i-1) if i > 0 else 1) * b
        return n_reversed

if __name__ == '__main__':
    test_cases = [
        (43261596, 964176192),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().reverseBits(test_case[0])
        print('output:', output)
        assert output == test_case[1]


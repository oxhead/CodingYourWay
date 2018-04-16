"""
https://leetcode.com/problems/counting-bits

Related:
  - lt_191_number-of-1-bits
"""

"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # Time: O(n)
        # Space: O(1)
        output = [0]
        for i in range(1, num + 1):
            # i is even: count = i/2's count
            # i is odd: count = i/2's count + 1
            output.append((i & 1) + output[i >> 1])
        return output

    def countBits_v2(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # Time: O(n)
        # Space: O(1)
        output = [0]
        while len(output) < num + 1:
            output += [1 + x for x in output]
        return output[:num+1]
        
    def countBits_naive(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # Time: O(n * k), k is the size of integer
        # Space: O(1)
        def count_bits(n):
            count = 0
            while n > 0:
                count += n & 1
                n >>= 1
            return count
        return [count_bits(n) for n in range(num + 1)]


if __name__ == '__main__':
    test_cases = [
         (5, [0, 1, 1, 2, 1, 2]),
         (8, [0, 1, 1, 2, 1, 2, 2, 3, 1]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().countBits(test_case[0])
        print('output:', output)
        assert output == test_case[1]


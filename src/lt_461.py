"""
https://leetcode.com/problems/hamming-distance

Related:
  - lt_191_number-of-1-bits 
  - lt_477_total-hamming-distance
"""

"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Time: O(1)
        # Space: O(1)
        count = 0
        for i in range(32):
            count += (x & 1) ^ (y & 1)
            x >>= 1
            y >>= 1
        return count
        

if __name__ == '__main__':
    test_cases = [
        ((1, 4), 2),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().hammingDistance(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


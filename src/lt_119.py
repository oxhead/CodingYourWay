"""
https://leetcode.com/problems/pascals-triangle-ii
https://leetcode.com/problems/pascals-triangle

Related:
  - lt_118_pascals-triangle
"""

"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space? 
"""

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # Time: O(n^2)
        # Space: O(1)
        output = [0] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            previous = output[0] = 1
            for j in range(1, i + 1):
                previous, output[j] = output[j], previous + output[j]
        return output

    def getRow_verbose(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0: return []
        output = [None] * (rowIndex + 1)
        output[0] = 1
        for i in range(1, rowIndex+1):
            tmp = [n for n in output]
            for j in range(i+1):
                if j == i:
                     output[j] = tmp[j-1]
                elif 0 < j < i:
                     output[j] = tmp[j-1] + output[j]
        return output

if __name__ == '__main__':
    test_cases = [
        (-1, []),
        (0, [1]),
        (1, [1, 1]),
        (2, [1, 2, 1]),
        (4, [1, 4, 6, 4, 1]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().getRow(test_case[0])
        print('output:', output)
        assert output == test_case[1]


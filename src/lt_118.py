"""
https://leetcode.com/problems/pascals-triangle

Related:
  - lt_119

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows: return []
        output = [[1]]
        for i in range(1, numRows):
            row = []
            for j in range(i+1):
                if j == 0: row.append(output[i-1][0])
                elif j == i: row.append(output[i-1][-1])
                else: row.append(output[i-1][j-1] + output[i-1][j])
            output.append(row)
        return output


if __name__ == '__main__':
    test_cases = [
        (0, []),
        (1, [[1]]),
        (2, [[1], [1, 1]]),
        (3, [[1], [1, 1], [1, 2, 1]]),
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().generate(test_case[0])
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/maximal-rectangle

Related:
  - lt_84_largest-rectangle-in-histogram
  - lt_221_maximal-square
"""

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 6.
"""

class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # Time: O(m * n)
        # Space: O(n)
        def find_max_rectangle(heights):
            heights.append(0)
            stack = []
            max_rectangle = 0
            for i, n in enumerate(heights):
                while stack and heights[i] <= heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1 if stack else i
                    max_rectangle = max(max_rectangle, h * w)
                stack.append(i)
            return max_rectangle

        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0: return 0
        max_rectangle = 0
        heights = [0] * len(matrix[0])
        for row in matrix:
           heights = [(h + int(n)) if n == '1' else 0 for h, n in zip(heights, row)] 
           max_rectangle = max(max_rectangle, find_max_rectangle(heights))
        return max_rectangle

if __name__ == '__main__':
    test_cases = [
        ([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]], 6),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().maximalRectangle(test_case[0])
        print('output:', output)
        assert output == test_case[1]


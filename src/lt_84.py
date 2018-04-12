"""
https://leetcode.com/problems/largest-rectangle-in-histogram

Related:
  - lt_85_maximal-rectangle
"""

"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
"""

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        if not heights: return 0
        heights.append(0)
        max_area = 0
        stack = []
        for i, n in enumerate(heights):
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                max_area = max(max_area, heights[index] * ( i - 1 - (stack[-1] if stack else -1)))
            stack.append(i)
        return max_area


    def largestRectangleArea_bruteforce(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(heights)):
            min_height = heights[i]
            for j in range(i, -1, -1):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height * (i - j + 1))
        return max_area


if __name__ == '__main__':
    test_cases = [
        ([1], 1),
        ([2, 6, 5, 2], 10),
        ([2, 1, 5, 6, 2, 3], 10),
        ([1, 1, 1, 1, 1, 1, 1, 4, 5, 2], 10),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().largestRectangleArea(test_case[0])
        print('output:', output)
        assert output == test_case[1]


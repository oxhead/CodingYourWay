"""
https://leetcode.com/problems/container-with-most-water

Related:
  - lt_42
"""

"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2. 
"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area

    def maxArea_naive(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # time limit exceeded
        area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = max(area, (j - i) * min(height[i], height[j]))
        return area


if __name__ == '__main__':
    test_cases = [
        ([1, 1], 1),    
        ([1, 3, 2, 4, 2, 3], 12),
        ([1, 3, 4, 2, 1, 1, 1, 4, 5], 24),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().maxArea_naive(test_case[0])
        print('output:', output)
        assert output == test_case[1]


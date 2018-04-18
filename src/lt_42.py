"""
https://leetcode.com/problems/trapping-rain-water

Related:
  - lt_11_container-with-most-water
  - lt_238_product-of-array-except-self
  - lt_407_trapping-rain-water-ii
  - lt_755_pour-water
"""

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        stack = []
        vol = 0
        for i, h in enumerate(height):
            while stack and h > stack[-1][1]:
                previous = stack.pop()
                if not stack: continue
                vol += (min(h, stack[-1][1]) - previous[1]) * (i - stack[-1][0] - 1)
            stack.append((i, h))
        return vol

    def trap_twosides(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        # https://github.com/algorhythms/LeetCode/blob/master/041%20Trapping%20Rain%20Water.py
        left_maxs = [0 for _ in height]
        right_maxs = [0 for _ in height]
        
        left_max = 0
        for i, h in enumerate(height):
            left_max = max(left_max, h)
            left_maxs[i] = left_max

        right_max = 0
        for i, h in reversed(list(enumerate(height))):
            right_max = max(right_max, h)
            right_maxs[i] = right_max

        # print('left :', left_maxs)
        # print('right:', right_maxs)
        # print('vol  :', [max(0, min(left_maxs[i], right_maxs[i]) - h) for i, h in enumerate(height)])
        volume = 0
        for i, h in enumerate(height):
            volume += min(left_maxs[i], right_maxs[i]) - h
            # this won't happen
            # volume += max(0, min(left_maxs[i], right_maxs[i]) - h)
        return volume

    def trap_twopointers(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        # https://www.jianshu.com/p/7bca16941cea
        left, right, total, max_height = 0, len(height) - 1, 0, 0
        while left < right:
            while left < right and height[left] <= max_height:
                total += max_height - height[left]
                left += 1
            while left < right and height[right] <= max_height:
                total += max_height - height[right]
                right -= 1
            max_height = min(height[left], height[right])
        return total

    def trap_failed(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left, right = 0, 1
        while right < len(height):
            if height[right] >= height[left]:
                if left != 0:
                    total = height[right] * (right - left - 1)
                    volume = (height[right] - height[left]) * (right - left - 1)
                    print('left={}, right={}, vol={}'.format(left, right, total-volume))
                    area += total - volume
                left = right
            right += 1
        return area


if __name__ == '__main__':
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([2, 1, 0, 2], 3),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().trap(test_case[0])
        print('output:', output)
        assert output == test_case[1]


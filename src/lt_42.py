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
            volume += max(0, min(left_maxs[i], right_maxs[i]) - h)
        return volume


if __name__ == '__main__':
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().trap(test_case[0])
        print('output:', output)
        assert output == test_case[1]


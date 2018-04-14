"""
https://leetcode.com/problems/rectangle-area

Related:
"""

"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Assume that the total area is never beyond the maximum possible value of int.
"""

class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # Time: O(1)
        # Space: O(1)
        return (C - A) * (D - B) + (G - E) * (H - F) - max(0, (min(C, G) - max(A, E))) * max(0, (min(H, D) - max(F, B)))
        

if __name__ == '__main__':
    test_cases = [
        ((-3, 0, 3, 4, 0, -1, 9, 2), 45),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().computeArea(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

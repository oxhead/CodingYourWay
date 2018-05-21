"""
https://leetcode.com/problems/rectangle-overlap
"""

"""
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two rectangles, return whether they overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true

Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false

Notes:

    Both rectangles rec1 and rec2 are lists of 4 integers.
    All coordinates in rectangles will be between -10^9 and 10^9.
"""

class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # Time: O(1)
        # Space: O(1)
        # https://www.geeksforgeeks.org/find-two-rectangles-overlap/
        L1, R1 = (rec1[0], rec1[1]), (rec1[2], rec1[3])
        L2, R2 = (rec2[0], rec2[1]), (rec2[2], rec2[3])
        if L1[0] >= R2[0] or L2[0] >= R1[0]: return False
        if L1[1] >= R2[1] or L2[1] >= R1[1]: return False
        return True

    def isRectangleOverlap_v2(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # https://leetcode.com/problems/rectangle-overlap/discuss/132340/C++JavaPython-1-line-Solution-1D-to-2D
        return max(rec1[0], rec2[0]) < min(rec1[2], rec2[2]) and max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
 
    def isRectangleOverlap_failed(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        points = ((rec2[0], rec2[1]), (rec2[2], rec2[1]), (rec2[0], rec2[3]), (rec2[2], rec2[3]), ((rec2[0] + rec2[2]) / 2, (rec2[1] + rec2[3]) / 2))
        for x, y in points:
            print(rec1[0], x, rec1[2])
            print(rec1[1], y, rec1[3])
            if rec1[0] < x < rec1[2] and rec1[1] < y < rec1[3]: return True
            if rec1[0] < x < rec1[2] and rec1[1] <= y <= rec1[3]: return True
            if rec1[0] <= x <= rec1[2] and rec1[1] < y < rec1[3]: return True
        return False 
       
        
if __name__ == '__main__':
    test_cases = [
        (([0,0,2,2], [1,1,3,3]), True),
        (([0,0,1,1], [1,0,2,1]), False),
        (([7,8,13,15], [10,8,12,20]), True),
        (([4,4,14,7], [4,3,8,8]), True),
        (([4,0,6,6], [-5,-3,4,2]),False),
        (([2,17,6,20], [3,8,6,20]), True),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isRectangleOverlap(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

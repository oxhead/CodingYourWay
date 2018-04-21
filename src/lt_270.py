"""
https://leetcode.com/problems/closest-binary-search-tree-value

Related:
  - lt_222_count-complete-tree-nodes
  - lt_272_closest-binary-search-tree-value-ii
"""

"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

    Given target value is a floating point.
    You are guaranteed to have only one unique value in the BST that is closest to the target.
"""

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        node = root
        closet_value = node.val
        while node:
            if node.val == target: return node.val
            else:
                if abs(node.val - target) < abs(closet_value - target): closet_value = node.val
                if node.val > target: node = node.left
                else: node = node.right
        return closet_value


if __name__ == '__main__':
    test_cases = [
        (([2, 1, 3], 0), 1),
        (([2, 1, 3], 1), 1),
        (([2, 1, 3], 2), 2),
        (([2, 1, 3], 3), 3),
        (([2, 1, 3], 4), 3),
        (([28,12,45,4,24,35,47,2,9,14,25,31,42,46,48,0,3,8,11,13,20,None,26,30,33,41,43,None,None,None,49,None,1,None,None,7,None,10,None,None,None,17,22,None,27,29,None,32,34,36,None,None,44,None,None,None,None,6,None,None,None,16,18,21,23,None,None,None,None,None,None,None,None,None,37,None,None,5,None,15,None,None,19,None,None,None,None,None,40,None,None,None,None,None,None,39,None,38], 2.000000), 2),
        (([36,13,37,4,20,None,48,1,5,17,33,43,49,0,2,None,9,14,18,22,34,40,46,None,None,None,None,None,3,7,11,None,16,None,19,21,27,None,35,39,42,45,47,None,None,6,8,10,12,15,None,None,None,None,None,26,32,None,None,38,None,41,None,44,None,None,None,None,None,None,None,None,None,None,None,None,None,24,None,28,None,None,None,None,None,None,None,23,25,None,29,None,None,None,None,None,31,30], 3.142857), 3),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().closestValue(parse_tree(test_case[0][0]), test_case[0][1])
        print('output:', output)
        assert output == test_case[1]


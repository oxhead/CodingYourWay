"""
https://leetcode.com/problems/maximum-depth-of-binary-tree

Related:
  - lt_110_balanced-binary-tree
  - lt_111_minimum-depth-of-binary-tree
"""

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

from base import TreeNode
from utils import print_tree, parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(h)
        # Hint: return the maximum length of the left and right subtrees recursively
        return 0 if not root else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == '__main__':
    test_cases = [
        ([1, None, 2, 3], 3)
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().maxDepth(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


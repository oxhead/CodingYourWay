"""
https://leetcode.com/problems/minimum-depth-of-binary-tree

Related:
  - lt_102_binary-tree-level-order-traversal
  - lt_104_maximum-depth-of-binary-tree
"""

"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(h)
        if not root: return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def minDepth_verbose(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(h)
        def traverse(node, height, min_height):
            if not node: min_height
            elif not node.left and not node.right:
                return min(min_height, height + 1)
            elif node.left and node.right:
                return min(traverse(node.left, height + 1, min_height), traverse(node.right, height + 1, min_height))
            elif node.left:
                return traverse(node.left, height + 1, min_height)
            else:
                return traverse(node.right, height + 1, min_height)
        if not root: return 0
        elif not root.left and not root.right: return 1
        return traverse(root, 0, float('inf'))


if __name__ == '__main__':
    test_cases = [
        ([], 0),
        ([0], 1),
        ([1, None, 2, 3], 3),
        ([1, 2, 3, None, None, 4, 5, 6], 2),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().minDepth(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


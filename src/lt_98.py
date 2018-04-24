"""
https://leetcode.com/problems/validate-binary-search-tree

Related:
  - lt_94_binary-tree-inorder-traversal
  - lt_501_find-mode-in-binary-search-tree
"""

"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:

    2
   / \
  1   3

Binary tree [2,1,3], return true.

Example 2:

    1
   / \
  2   3

Binary tree [1,2,3], return false. 
"""

import operator

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBST_inorder(root)

    def isValidBST_inorder(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        previous = float('-inf')
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val <= previous:
                return False
            previous = node.val
            node = node.right
        return True

    def isValidBST_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleMedium/98.html
        def is_valid_bst(node, min_value, max_value):
            if not node: return True
            if min_value < node.val < max_value:
                return is_valid_bst(node.left, min_value, node.val) and is_valid_bst(node.right, node.val, max_value)
            else:
                return False
        return is_valid_bst(root, float('-inf'), float('inf'))

    def isValidBST_failed(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_valid_tree(node, val, op):
            if not node: return True
            if not op(node.val, val): return False
            return is_valid_tree(node.left, node.val, operator.lt) and is_valid_tree(node.right, node.val, operator.gt)
        if not root: return True
        return is_valid_tree(root.left, root.val, operator.lt) and is_valid_tree(root.right, root.val, operator.gt)


if __name__ == '__main__':
    test_cases = [
        ([2, 1, 3], True),
        ([1, 2, 3], False),
        ([10, 5, 15, None, None, 6, 20], False),
        ([3, 1, 5, 0, 2, 4, 6], True),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isValidBST(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


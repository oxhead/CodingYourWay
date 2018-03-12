"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

Related:
  - lt_105_construct-binary-tree-from-preorder-and-inorder-traversal
"""

"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

from base import TreeNode
from utils import parse_tree, tree_traversal_inorder, is_bst_equal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # https://github.com/kamyu104/LeetCode/blob/master/Python/construct-binary-tree-from-inorder-and-postorder-traversal.py
        def _build_tree(post_end, in_start, in_end):
            if in_start == in_end: return None
            node = TreeNode(postorder[post_end - 1])
            i = records[postorder[post_end - 1]]
            node.left = _build_tree(post_end - 1 - (in_end - i - 1), in_start, i)
            node.right = _build_tree(post_end - 1, i + 1, in_end)
            return node
        records = {}
        for i, n in enumerate(inorder):
            records[n] = i
        return _build_tree(len(postorder), 0, len(inorder))


if __name__ == '__main__':
    test_cases = [
        (([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]), [3, 9, 20, None, None, 15, 7]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().buildTree(*test_case[0])
        print('output:', tree_traversal_inorder(output))
        assert is_bst_equal(output, parse_tree(test_case[1]))

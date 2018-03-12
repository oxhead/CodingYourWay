"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

Related:
  - lt_106_construct-binary-tree-from-inorder-and-postorder-traversal
"""

"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # https://github.com/kamyu104/LeetCode/blob/master/Python/construct-binary-tree-from-preorder-and-inorder-traversal.py
        def _build_tree(pre_start, in_start, in_end):
            if in_start == in_end: return None
            node = TreeNode(preorder[pre_start])
            i = records[preorder[pre_start]]
            node.left = _build_tree(pre_start + 1, in_start, i)
            node.right = _build_tree(pre_start + 1 + i - in_start, i + 1, in_end)
            return node
        
        records = {}
        for i, n in enumerate(inorder):
            records[n] = i
        return _build_tree(0, 0, len(inorder))


if __name__ == '__main__':
    test_cases = [
        (([3, 9, 20, 15, 7], [9,3,15,20,7]), [3, 9, 20, None, None, 15, 7]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().buildTree(*test_case[0])
        print('output:', tree_traversal_inorder(output))
        assert is_bst_equal(output, parse_tree(test_case[1]))

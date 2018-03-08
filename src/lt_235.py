"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

Related:
  - lt_236_lowest-common-ancestor-of-a-binary-tree
"""

"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5

For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""

from base import TreeNode
from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        while root:
            if root.val > p.val and root.val > q.val: root = root.left
            elif root.val < p.val and root.val < q.val: root = root.right
            else: return root

    def lowestCommonAncestor_recursive(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return root

        if p.val > q.val: return self.lowestCommonAncestor(root, q, p)
        if root.val >= p.val and root.val <= q.val: return root
        if p.val < root.val: return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val: return self.lowestCommonAncestor(root.right, p, q)

if __name__ == '__main__':
    test_cases = [
        (([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8), 6),
        (([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4), 2),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        root = parse_tree(test_case[0][0])
        p = TreeNode(test_case[0][1])
        q = TreeNode(test_case[0][2])
        output = Solution().lowestCommonAncestor(root, p, q)
        print('output:', output.val)
        assert output.val == test_case[1]


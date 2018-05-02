"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

Related:
  - lt_235_lowest-common-ancestor-of-a-binary-search-tree
"""

"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
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
        # Time: O(n)
        # Space: O(h)
        # Hints:
        # 1) Check the left and right subtrees separately.
        # 2) If p and q are in the two subtrees, the root the LCA
        # 3) Else, returns the non-empty subtree (both p and q in the subtree)
        if not root: return root
        if p == root or q == root: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        return left if left else right

    def lowestCommonAncestor_shortest(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(child, p, q) for child in (root.left, root.right))
        return root if left and right else left or right

    def lowestCommonAncestor_failed(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def in_tree(node, target):
            if not node or not target: return False
            if node.val == target.val: return True
            return in_tree(node.left, target) or in_tree(node.right, target)
        if in_tree(root.left, p) and in_tree(root.right, q):
            return root
        elif in_tree(root.right, p) and in_tree(root.left, q):
            return root
        elif root == p and in_tree(root, q):
            return p
        elif root == q and in_tree(root, p):
            return q
        elif in_tree(root.left, p) and in_tree(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        elif in_tree(root.right, p) and in_tree(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        return None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        elif root == p: return p
        elif root == q: return q
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)
        if left_lca and right_lca: return root
        return left_lca if left_lca else right_lca


if __name__ == '__main__':
    test_cases = [
        (([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 1, 2), 0),
        (([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 1, 10), 1),
        (([37, -34, -48, None, -100, -100, 48, None, None, None, None, -54, None, -71, -22, None, None, None, 8], 5, -13), 2),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        root, nodes = parse_tree(test_case[0][0], return_nodes=True)
        p = nodes[test_case[0][1]]
        q = nodes[test_case[0][2]]
        ans = nodes[test_case[1]]
        output = Solution().lowestCommonAncestor(root, p, q)
        print('output:', output.val)
        assert output.val == ans.val


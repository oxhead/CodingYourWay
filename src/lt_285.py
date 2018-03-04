"""
https://leetcode.com/problems/inorder-successor-in-bst

Related:
  - lt_94
  - lt_173

Complexity:
  - Time:
  - Space:
"""

"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
"""

from utils import parse_tree, search_node_by_value

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        successor = None
        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor

    def inorderSuccessor_recursive(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        if root == p:
            node = root.right
            while node and node.left: node = node.left
            return node
        elif p.val > root.val:
            return self.inorderSuccessor_recursive(root.right, p)
        else:
            node = self.inorderSuccessor_recursive(root.left, p)
        return node if node else root


if __name__ == '__main__':
    test_cases = [
        (([5, 2, 6, 1, 3], 2), 3),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        root, nodes = parse_tree(test_case[0][0], return_nodes=True)
        p = search_node_by_value(nodes, test_case[0][1])
        successor = Solution().inorderSuccessor(root, p)
        # successor = Solution().inorderSuccessor_recursive(root, p)
        print('output:', successor.val if successor else None)
        if test_case[1]:
            if successor:
                assert successor.val == test_case[1]
            else:
                assert False
        else:
            assert successor == test_case[1]

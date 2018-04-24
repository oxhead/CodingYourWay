"""
https://leetcode.com/problems/binary-tree-preorder-traversal

Related:
  - lt_94_binary-tree-inorder-traversal
  - lt_255_verify-preorder-sequence-in-binary-search-tree
"""

"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3

return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output, stack = [], [(root, False)]
        while stack:
            node, is_visited = stack.pop()
            if not node: continue
            if is_visited:
                output.append(node.val)
            else:
                stack.append((node.right, False))
                stack.append((node.left, False))
                stack.append((node, True))
        return output

    def preorderTraversal_iterative2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        path_list = []
        stack = []
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            path_list.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return path_list

    def preorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder_recursive(node, path_list):
            if not node: return
            path_list.append(node.val)
            preorder_recursive(node.left, path_list)
            preorder_recursive(node.right, path_list)
        path_list = []
        preorder_recursive(root, path_list)
        return path_list

    def preorderTraversal_morris(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output, node = [], root
        while node:
            if node.left is None:
                output.append(node.val)
                node = node.right
            else:
                previous = node.left
                while previous.right and previous.right != node:
                    previous = previous.right
                if previous.right is None:
                    output.append(node.val)
                    previous.right = node
                    node = node.left
                else:
                    previous.right = None
                    node = node.right
        return output

if __name__ == '__main__':
    test_cases = [
        ([1, None, 2, 3], [1, 2, 3]),
        ([1, 2, 5, 3, 4, None, 6, None, None, None, None, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().preorderTraversal(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


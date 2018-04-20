"""
https://leetcode.com/problems/binary-tree-inorder-traversal

Related:
  - lt_98_validate-binary-search-tree
  - lt_144_binary-tree-preorder-traversal
  - lt_145_binary-tree-postorder-traversal
  - lt_173_binary-search-tree-iterator
  - lt_230_kth-smallest-element-in-a-bst
  - lt_272_closest-binary-search-tree-value-ii
  - lt_285_minimum-distance-between-bst-nodes
"""

"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3

return [1,3,2].

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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Time: O(n)
        # Space: O(n)
        node = root
        stack = []
        output = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            current = stack.pop()
            output.append(current.val)
            node = current.right
        return output

    def inorderTraversal_stack(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """ 
        # Simulate call stack
        output, stack = [], [(root, False)]
        while stack:
            node, is_visited = stack.pop()
            if not node: continue
            if is_visited:
                output.append(node.val)
            else:
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
        return output

    def inorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Time: O(n)
        # Space: O(1)
        def inorder_recursive(node, path_list):
            if not node: return
            inorder_recursive(node.left, path_list)
            path_list.append(node.val)
            inorder_recursive(node.right, path_list)
        path_list = []
        inorder_recursive(root, path_list)
        return path_list

    def inorderTraversal_morris(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Time: O(n)
        # Space: O(1)
        # https://en.wikipedia.org/wiki/Threaded_binary_tree
        # https://github.com/algorhythms/LeetCode/blob/master/095%20Binary%20Tree%20Inorder%20Traversal.py
        output = []
        node = root
        while node:
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                previous = node.left
                while previous.right and previous.right != node:
                    previous = previous.right
                if not previous.right:
                    previous.right = node
                    node = node.left
                else:
                    previous.right = None
                    output.append(node.val)
                    node = node.right
        return output


if __name__ == '__main__':
    test_cases = [
        ([1, None, 2, 3], [1, 3, 2]),
        ([1, 2, 5, 3, 4, None, 6, None, None, None, None, 7, 8], [3, 2, 4, 1, 5, 7, 6, 8]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().inorderTraversal(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/binary-tree-inorder-traversal

Related:
  - lt_98
  - lt_144
  - lt_145
  - lt_173
  - lt_230
  - lt_272
  - lt_285

Complexity:
  - Time: O()
  - Space: O()
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
        path_list = []
        stack = []
        node = root
        while len(stack) > 0 or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                path_list.append(node.val)
                node = node.right
        return path_list
 
    def inorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder_recursive(node, path_list):
            if not node: return
            inorder_recursive(node.left, path_list)
            path_list.append(node.val)
            inorder_recursive(node.right, path_list)
        path_list = []
        inorder_recursive(root, path_list)
        return path_list

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


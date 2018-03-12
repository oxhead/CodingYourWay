"""
https://leetcode.com/problems/binary-tree-postorder-traversal

Related:
  - lt_94

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3

 

return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
"""

from base import TreeNode
from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
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
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        return output

    def postorderTraversal_iterative2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path_list = []
        stack = []
        last_node_visited = None
        node = root
        while len(stack) > 0 or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek_node = stack[-1]
                if peek_node.right and last_node_visited != peek_node.right:
                    node = peek_node.right
                else:
                    path_list.append(peek_node.val)
                    last_node_visited = stack.pop()
        return path_list
 
    def postorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def postorder_recursive(node, path_list):
            if not node: return
            postorder_recursive(node.left, path_list)
            postorder_recursive(node.right, path_list)
            path_list.append(node.val)
        path_list = []
        postorder_recursive(root, path_list)
        return path_list

    def postorderTraversal_morris(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-postorder-traversal.py
        def trace_back(node_from, node_to):
            result, current = [], node_from
            while current != node_to:
                result.append(current.val)
                current = current.right
            result.append(node_to.val)
            result.reverse()
            return result

        dummy = TreeNode(0)
        dummy.left = root
        output, current = [], dummy
        while current:
            if current.left is None:
                current = current.right
            else:
                node = current.left
                while node.right and node.right != current:
                    node = node.right
                if not node.right:
                    node.right = current
                    current = current.left
                else:
                    output += trace_back(current.left, node)
                    node.right = None
                    current = current.right
        return output
        

if __name__ == '__main__':
    test_cases = [
        ([1, None, 2, 3], [3, 2, 1]),
        ([1, 2, 5, 3, 4, None, 6, None, None, None, None, 7, 8], [3, 4, 2, 7, 8, 6, 5, 1]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().postorderTraversal_morris(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


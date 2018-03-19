"""
https://leetcode.com/problems/binary-tree-upside-down

Related:
  - lt_206_reverse-linked-list
"""

"""
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
For example:
Given a binary tree {1,2,3,4,5},

    1
   / \
  2   3
 / \
4   5

return the root of the binary tree [4,5,2,#,#,3,1].

   4
  / \
 5   2
    / \
   3   1  

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""

from utils import parse_tree, serialize_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Time: O(n)
        # Space: O(n), if consider the call stack
        # https://github.com/algorhythms/LeetCode/blob/master/156%20Binary%20Tree%20Upside%20Down.py
        if not root or not root.left: return root
        left, right = root.left, root.right
        new_root = self.upsideDownBinaryTree(left)
        left.left, left.right = right, root
        root.left, root.right = None, None
        return new_root

    def upsideDownBinaryTree_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Time: O(n)
        # Space: O(1)
        # https://www.tangjikai.com/algorithms/leetcode-156-binary-tree-upside-down
        p, parent, parent_right = root, None, None
        while p:
            left = p.left
            p.left = parent_right
            parent_right = p.right
            p.right = parent
            parent = p
            p = left
        return parent


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5], [4, 5, 2, None, None, 3, 1]), 
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().upsideDownBinaryTree(parse_tree(test_case[0]))
        output_list = serialize_tree(output)
        print('output:', output_list)
        assert output_list == test_case[1]


"""
https://leetcode.com/problems/invert-binary-tree

Related:
"""

"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

    Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
"""

from utils import parse_tree, tree_traversal_inorder

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Time: O(n)
        # Space: O(h)
        def swap_tree(node):
            if not node: return
            node.left, node.right = node.right, node.left
            swap_tree(node.left)
            swap_tree(node.right) 
        swap_tree(root)
        return root

if __name__ == '__main__':
    test_cases = [
        ([4, 2, 7, 1, 3, 6, 9], None),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        root = parse_tree(test_case[0])
        output = Solution().invertTree(root)
        output_list = tree_traversal_inorder(output)
        print('output:', output_list)
        assert output_list == list(reversed(tree_traversal_inorder(parse_tree(test_case[0]))))


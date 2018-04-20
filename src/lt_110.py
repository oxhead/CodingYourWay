"""
https://leetcode.com/problems/balanced-binary-tree

Related:
  - lt_104_maximum-depth-of-binary-tree
"""

"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7

Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

Return false.
"""

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(h)
        def get_height(node):
            if not node: return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        return get_height(root) >= 0

    def isBalanced_redundant(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def find_height(node):
            if not node: return 0
            height = 1 + max(find_height(node.left), find_height(node.right))
            return height
            #return 1 + max(find_height(node.left), find_height(node.right))
        if not root: return True
        return abs(find_height(root.left) - find_height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == '__main__':
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], True),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),
        ([1, 2, 2, 3, None, None, 3, 4, None, None, 4], False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isBalanced(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


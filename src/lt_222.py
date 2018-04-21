"""
https://leetcode.com/problems/count-complete-tree-nodes/description/

Related:
  - lt_270_closest-binary-search-tree-value
"""

"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(logn ^ 2)
        # Space: O(logn)
        # https://www.liuchuo.net/archives/3253
        if not root: return 0
        height_left, height_right = 0, 0
        left, right = root, root
        while left:
            left = left.left
            height_left += 1
        while right:
            right = right.right
            height_right += 1
        if height_left == height_right: return 2 ** height_left - 1
        else: return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes_v2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(logn ^ 2)
        # Space: O(logn)
        def get_level(node):
            return 1 + get_level(node.left) if node else -1
        h = get_level(root)
        if h < 0: return 0
        if get_level(root.right) == h - 1:
            return self.countNodes(root.right) + (1 << h)
        else:
            return self.countNodes(root.left) + (1 << h-1) 

    def countNodes_naive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(logn)
        return 0 if not root else 1 + self.countNodes(root.left) + self.countNodes(root.right)


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], 3),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().countNodes(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


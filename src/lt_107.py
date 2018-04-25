"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii

Related:
  - lt_102_binary-tree-level-order-traversal
  - lt_637_average-of-levels-in-binary-tree
"""

"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
"""

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Time: O(n)
        # Space: O(n)
        if not root: return []

        output = []
        queue = [root]
        while queue:
            output.insert(0, [n.val for n in queue])
            queue_level = []
            for node in queue:
                if node.left: queue_level.append(node.left)
                if node.right: queue_level.append(node.right)
            queue = queue_level
        return output


if __name__ == '__main__':
    test_cases = [
        ([], []),
        ([3, 9, 20, None, None, 15, 7], [[15, 7], [9, 20], [3]])
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().levelOrderBottom(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


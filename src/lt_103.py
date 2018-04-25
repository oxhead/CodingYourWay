"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

Related:
  - lt_102_binary-tree-level-order-traversal
"""

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Time: O(n)
        # Space: O(n)
        if not root: return []
        output = []
        queue = [root]
        level = 0
        while queue:
            level += 1
            if level % 2 == 1:
                output.append([n.val for n in queue])
            else:
                output.append([n.val for n in reversed(queue)])
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
        return output

    def zigzagLevelOrder_v2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Time: O(n)
        # Space: O(n)
        if not root: return []

        output = []
        queue_current = [root]
        queue_children = []
        level = 0
        while queue_current:
            level += 1
            for node in queue_current:
                if node.left:
                    queue_children.append(node.left)
                if node.right:
                    queue_children.append(node.right)
            if level % 2 == 1:
                output.append([n.val for n in queue_current])
            else:
                output.append([n.val for n in reversed(queue_current)])
            queue_current = queue_children
            queue_children = []

        return output

            
if __name__ == '__main__':
    test_cases = [
        ([], []),
        ([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]])
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().zigzagLevelOrder(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


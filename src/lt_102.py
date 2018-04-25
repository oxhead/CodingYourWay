"""
https://leetcode.com/problems/binary-tree-level-order-traversal

Related:
  - lt_103_binary-tree-zigzag-level-order-traversal
  - lt_107_binary-tree-level-order-traversal-ii
  - lt_111_minimum-depth-of-binary-tree
  - lt_314_binary-tree-vertical-order-traversal
  - lt_637_average-of-levels-in-binary-tree
"""

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
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
            output.append([n.val for n in queue])
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
        return output

    def levelOrder_v2(self, root):
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
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(level)
        return output

    def levelOrder_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        def traverse(node, level, output):
            if len(output) <= level:
                output.append([])
            output[level].append(node.val)
            if node.left:
                traverse(node.left, level + 1, output)
            if node.right:
                traverse(node.right, level + 1, output)
        output = []
        traverse(root, 0, output)
        return output


if __name__ == '__main__':
    test_cases = [
        ([], []),
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]])
    ]

    from utils import parse_tree

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().levelOrder(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


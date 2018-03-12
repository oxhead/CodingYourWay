"""
https://leetcode.com/problems/average-of-levels-in-binary-tree

Related:
  - lt_102_binary-tree-level-order-traversal
  - lt_107_binary-tree-level-order-traversal-ii
"""

"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:

Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note:

    The range of node's value is in the range of 32-bit signed integer.
"""

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # Time: O(n)
        # Space: O(n), in the worst case
        if not root: return []

        output = []
        queue = [root]
        while queue:
            output.append(sum([n.val for n in queue]) / len(queue))
            queue_children = []
            for node in queue:
                if node.left:
                    queue_children.append(node.left)
                if node.right:
                    queue_children.append(node.right)
            queue = queue_children

        return output
        

if __name__ == '__main__':
    test_cases = [
        ([], []),
        ([3, 9, 20, None, None, 15, 7], [3, 14.5, 11])
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().averageOfLevels(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]

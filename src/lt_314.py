"""
https://leetcode.com/problems/binary-tree-vertical-order-traversal

Related:
  - lt_102_binary-tree-level-order-traversal
"""

"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:

    Given binary tree [3,9,20,null,null,15,7],

       3
      /\
     /  \
     9  20
        /\
       /  \
      15   7

    return its vertical order traversal as:

    [
      [9],
      [3,15],
      [20],
      [7]
    ]

    Given binary tree [3,9,8,4,0,1,7],

         3
        /\
       /  \
       9   8
      /\  /\
     /  \/  \
     4  01   7

    return its vertical order traversal as:

    [
      [4],
      [9],
      [3,0,1],
      [8],
      [7]
    ]

    Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),

         3
        /\
       /  \
       9   8
      /\  /\
     /  \/  \
     4  01   7
        /\
       /  \
       5   2

    return its vertical order traversal as:

    [
      [4],
      [9,5],
      [3,0,1],
      [8,2],
      [7]
    ]
"""

from collections import defaultdict

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []

        queue = [(root, 0, 0)]
        records = defaultdict(list)
        output = []
        while queue:
            node, row, col = queue.pop(0)
            records[col].append(node.val)
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        for col in sorted(records.keys()): 
            output.append(records[col])
        
        return output

if __name__ == '__main__':
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], [[9], [3, 15], [20], [7]]),
        ([3, 9, 8, 4, 0, 1, 7], [[4], [9], [3, 0, 1], [8], [7]]),
        ([3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5], [[4], [9, 5], [3, 0, 1], [8, 2], [7]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().verticalOrder(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/same-tree/description/

Related:
"""

"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: return True
        elif (p and not q) or (not p and q): return False
        elif p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    test_cases = [
        (([1, 2, 3], [1, 2, 3]), True),
        (([1, 2], [1, None, 3]), False),
        (([1, 2, 1], [1, 1, 2]), False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isSameTree(parse_tree(test_case[0][0]), parse_tree(test_case[0][1]))
        print('output:', output)
        assert output == test_case[1]


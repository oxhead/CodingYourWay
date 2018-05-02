"""
https://leetcode.com/problems/trim-a-binary-search-tree

Related:
"""

"""
 Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:

Input: 
    1
   / \
  0   2

  L = 1
  R = 2

Output: 
    1
      \
       2

Example 2:

Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1
"""

from utils import parse_tree, serialize_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # Time: O(n)
        # Space: O(h)
        # Hints:
        # 1) Discard the subtrees that are not necessary
        # Approaches:
        # 1) Break the problems into subproblems and use recursion.
        if root is None:
            return root
        if root.val > R:
            return self.trimBST(root.left, L, R)
        elif root.val < L:
            return self.trimBST(root.right, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root
        

if __name__ == '__main__':
    test_cases = [
        (([1, 0, 2], 1, 2), [1, None, 2]),
        (([3, 0, 4, None, 2, None, None, 1], 1, 3), [3, 2, None, 1]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().trimBST(parse_tree(test_case[0][0]), test_case[0][1], test_case[0][2])
        print('output:', serialize_tree(output))
        assert serialize_tree(output) == test_case[1]


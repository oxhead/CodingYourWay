"""
https://leetcode.com/problems/path-sum

Related:
  - lt_113_path-sum-ii
  - lt_124_binary-tree-maximum-path-sum
  - lt_129_sum-root-to-leaf-numbers
  - lt_437_path-sum-iii
  - lt_666_path-sum-iv
"""

"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(h)
        # Hints:
        # 1) Make sure when it reaches the leaf node.
        if not root: return False
        if not root.left and not root.right: return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


if __name__ == '__main__':
    test_cases = [
        (([], 0), False),
        (([5, 4, 8, 11, 13, 4, 7, 2, None, None, None, 1], 22), True),
        (([5, 4, 8, 11, 13, 4, 7, 2, None, None, None, 1], 50), False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        root = parse_tree(test_case[0][0])
        output = Solution().hasPathSum(root, test_case[0][1])
        print('output:', output)
        assert output == test_case[1]


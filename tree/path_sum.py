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
        if not root:
            return False

        sum -= root.val
        if (not root.left) and (not root.right):
            return sum == 0

        if root.left and self.hasPathSum(root.left, sum): return True
        if root.right and self.hasPathSum(root.right, sum): return True
        return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
       	if not root:
            return []
        return [root.val] + self.inorderTraversal(root.left) + self.inorderTraversal(root.right)
        

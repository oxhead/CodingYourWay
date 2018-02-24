"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

Related:
  - lt_109

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""

from base import ListNode, TreeNode
from utils import print_tree, is_height_balanced_bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """ 
        if len(nums) < 1:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

if __name__ == '__main__':
    test_cases = [
        ([-10, -3, 0, 5, 9], None),
        ([], None),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        root = Solution().sortedArrayToBST(test_case[0])
        print('output:', is_height_balanced_bst(root))
        assert is_height_balanced_bst(root)


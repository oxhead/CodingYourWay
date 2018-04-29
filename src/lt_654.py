"""
https://leetcode.com/problems/maximum-binary-tree

Related:
"""

"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

    The root is the maximum number in the array.
    The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
    The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree.

Example 1:

Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1

Note:

    The size of the given array will be in the range [1,1000].
"""

from base import TreeNode
from utils import serialize_tree

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def build(left, right):
            if left > right: return None
            mid = nums.index(max(nums[left:right+1]))
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        return build(0, len(nums) - 1)

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # Time: O(n)
        # Space: O(n)
        # https://github.com/kamyu104/LeetCode/blob/master/Python/maximum-binary-tree.py
        stack = []
        for n in nums:
            node = TreeNode(n)
            while stack and node.val > stack[-1].val:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
        

if __name__ == '__main__':
    test_cases = [
        ([3, 2, 1, 6, 0, 5], [6, 3, 5, None, 2, 0, None, None, 1]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().constructMaximumBinaryTree(test_case[0])
        print('output:', serialize_tree(output))
        assert serialize_tree(output) == test_case[1]


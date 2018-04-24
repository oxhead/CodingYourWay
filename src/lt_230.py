"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst

Related:
  - lt_94_binary-tree-inorder-traversal
  - lt_671_second-minimum-node-in-a-binary-tree
"""

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        # https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleMedium/230.html
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            top = stack.pop()
            k -= 1
            if k == 0:
                node = top
                break
            else:
                node = top.right
        return node.val

    def kthSmallest_recursive(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # https://github.com/algorhythms/LeetCode/blob/master/230%20Kth%20Smallest%20Element%20in%20a%20BST.py
        def count(node):
            if not node:
                return 0
            return 1 + count(node.left) + count(node.right)
        left_count = count(root.left)
        if left_count + 1 == k:
            return root.val
        elif left_count + 1 < k:
            return self.kthSmallest(root.right, k - (left_count + 1))
        else:
            return self.kthSmallest(root.left, k)
        
    def kthSmallest_naive(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def traverse(node, nums):
            if not node: return
            nums.append(node.val)
            traverse(node.left, nums)
            traverse(node.right, nums)
        nums = []
        traverse(root, nums)
        return sorted(nums)[k-1]


if __name__ == '__main__':
    test_cases = [
        (([1], 1), 1),
        (([2, 1], 1), 1), 
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().kthSmallest(parse_tree(test_case[0][0]), test_case[0][1])
        print('output:', output)
        assert output == test_case[1]


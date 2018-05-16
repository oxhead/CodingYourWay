"""
https://leetcode.com/problems/binary-tree-maximum-path-sum

Related:
  - lt_112_path-sum
  - lt_129_sum-root-to-leaf-numbers
  - lt_666_path-sum-iv
  - lt_687_longest-univalue-path
"""

"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3

Return 6. 
"""

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(h)
        # https://www.jianshu.com/p/c3e81355831d
        # differentiate max_path_sum from single_path_sum
        def search(node):
            if not node: return float('-inf'), 0
            left = search(node.left)
            right = search(node.right)
            # !!! this zero is very important
            # the single_path_sum stores the max sum. three cases
            # 1) current + left child
            # 2) current + right child
            # 3) no nodes are considered (handled bt the max_path_sum
            single_path_sum = max(node.val + left[1], node.val + right[1], 0)
            # the max path sum is either form the left subtree, the right subtree or
            # both (including the current node) 
            global_path_sum = max(left[0], right[0], left[1] + node.val + right[1])
            return global_path_sum, single_path_sum
        global_path_sum, _ = search(root)
        return global_path_sum

    def maxPathSum_global(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(h)
        max_sum = float('-inf')
        def max_path_sum(node):
            nonlocal max_sum
            if not node: return float('-inf')
            left = max(0, max_path_sum(node.left))
            right = max(0, max_path_sum(node.right))
            max_sum = max(max_sum, node.val + left + right)
            return node.val + max(left, right)
        if not root: return 0
        max_path_sum(root)
        return max_sum


    def maxPathSum_failed():
        def max_path_sum(node, total):
            if not node: return float('-inf')
            if node.left and node.right:
                s1 = max_path_sum(node.left, total + node.left.val)
                s2 = max_path_sum(node.right, total + node.right.val)
                return max(total, s1, s2, s1 + s2 - total)
            elif node.left:
                return max(total, max_path_sum(node.left, total + node.left.val))
            elif node.right:
                return max(total,  max_path_sum(node.right, total + node.right.val))
            else:
                return total

        if not root: return float('-inf')
        return max(max_path_sum(root, root.val), self.maxPathSum(root.left), self.maxPathSum(root.right))

    def maxPathSum_failed(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node):
            if not node: return float('-inf'), float('-inf')
            if not node.left and not node.right: return node.val, float('-inf')
            left = traverse(node.left)
            right = traverse(node.right)
            return max(node.val, node.val + left[0] + right[0], node.val + left[0], node.val + right[0]), max(max(left), max(right))
            
        return max(traverse(root))


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
        ([1, -2, -3], 1),
        ([-2, -1], -1),
        ([1, -2, -3, 1, 3, -2, None, -1], 3),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 48),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().maxPathSum(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


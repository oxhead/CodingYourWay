"""
https://leetcode.com/problems/unique-binary-search-trees-ii

Related:
  - lt_96_unique-binary-search-trees
  - lt_241_different-ways-to-add-parentheses
"""

"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

import itertools

from base import TreeNode
from utils import serialize_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # Time: O(?)
        # Space: O(n)
        def build(nums):
            if not nums: return [None]
            output = []
            for i, n in enumerate(nums):
                left_subtrees = build(nums[:i])
                right_subtrees = build(nums[i+1:])
                for left, right in itertools.product(left_subtrees, right_subtrees):
                    root = TreeNode(n)
                    root.left = left
                    root.right = right
                    output.append(root)
            return output
                 
        if n < 1: return []
        nums = [n for n in range(1, n + 1)]
        return build(nums)


if __name__ == '__main__':
    test_cases = [
        (0, []), 
        (3, [[1, None, 3, 2], [3, 2, None, 1], [3, 1, None, None, 2], [2, 1, 3], [1, None, 2, None, 3]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().generateTrees(test_case[0])
        for o in output:
            print(serialize_tree(o))
        assert len(output) == len(test_case[1])
        assert sorted([tuple(serialize_tree(node)) for node in output]) == sorted([tuple(data) for data in test_case[1]])

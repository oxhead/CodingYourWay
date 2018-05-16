"""
https://leetcode.com/problems/sum-root-to-leaf-numbers

Related:
  - lt_112_path-sum
  - lt_124_binary-tree-maximum-path-sum
"""

"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(h)
        def traverse(node, num):
            if not node: return 0
            elif not node.left and not node.right: return int(num + str(node.val))
            return traverse(node.left, num + str(node.val)) + traverse(node.right, num + str(node.val))
        return traverse(root, "")
        


if __name__ == '__main__':
    test_cases = [
        ([0, 1], 1),
        ([1, 2, 3], 25),
        ([4, 9, 0, 5, 1], 1026),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().sumNumbers(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


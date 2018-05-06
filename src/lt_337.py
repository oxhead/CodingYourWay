"""
https://leetcode.com/problems/house-robber-iii

Related:
  - lt_198_house-robber
  - lt_213_house-robber-ii
"""

"""
 The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

     3
    / \
   2   3
    \   \ 
     3   1

Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

     3
    / \
   4   5
  / \   \ 
 1   3   1

Maximum amount of money the thief can rob = 4 + 5 = 9. 
"""

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(h)
        # Hints:
        # 1) Maintain two cases of maximum amount
        # 2) If the current node is included: node.val + left (no included) + right (no included)
        # 3) Else the current node is NOT included: max(left(either included or not)) + max(right(either included or not))
        def search(node):
            if not node: return (0, 0)
            left = search(node.left)
            right = search(node.right)
            return (node.val + left[1] + right[1], max(left) + max(right))
        return max(search(root))

    def rob_verbose(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def search(node, can_include):
            if not node: return 0
            if (node, can_include) in records: return records[(node, can_include)]
            amount = 0
            if can_include:
                amount = max(node.val + search(node.left, False) + search(node.right, False), search(node.left, True) + search(node.right, True), search(node.left, True) + search(node.right, False), search(node.left, False) + search(node.right, True))
            else:
                amount = search(node.left, True) + search(node.right, True)
            records[(node, can_include)] = amount
            return amount
        records = {}
        return search(root, True)
        

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], 5),
        ([3, 2, 3, None, 3, None, 1], 7),
        ([3, 4, 5, 1, 3, None, 1], 9),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().rob(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


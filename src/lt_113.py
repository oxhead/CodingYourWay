"""
https://leetcode.com/problems/path-sum-ii

Related:
  - lt_112_path-sum
  - lt_257_binary-tree-paths
  - lt_437_path-sum-iii
  - lt_666_path-sum-iv
"""

"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

return

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # Time: O(n)
        # Space: O(h)
        # Hints:
        # 1) Use backtracking to keep track the current visisted node.
        def search(node, total, current, output):
            if node and not node.left and not node.right and total == node.val:
                output.append(current + [node.val])
            elif node:
                current.append(node.val)
                search(node.left, total - node.val, current, output)
                search(node.right, total - node.val, current, output)
                current.pop()
            return output
        return search(root, sum, [], [])

    def pathSum_verbose(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # Time: O(n)
        # Space: O(h)
        if not root: return []
        if not root.left and not root.right and root.val == sum: return [[root.val]]
        
        output = []
        for sub in self.pathSum(root.left, sum - root.val):
            output.append([root.val] + sub)
        for sub in self.pathSum(root.right, sum - root.val):
            output.append([root.val] + sub)
        return output


if __name__ == '__main__':
    test_cases = [
        (([1, 2], 1), []),
        (([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22), [[5, 4, 11, 2], [5, 8, 4, 5]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().pathSum(parse_tree(test_case[0][0]), test_case[0][1])
        print('output:', output)
        assert sorted(output) == sorted(test_case[1])


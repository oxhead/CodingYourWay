"""
https://leetcode.com/problems/binary-tree-paths

Related:
  - lt_113_path-sum-ii
"""

"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5

All root-to-leaf paths are:

["1->2->5", "1->3"]
"""

from base import TreeNode
from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(node, path, path_list):
            if not node: return
            current_path = path + [node.val]
            if not node.left and not node.right:
                path_list.append(current_path)
            if node.left:
                dfs(node.left, current_path, path_list)
            if node.right:
                dfs(node.right, current_path, path_list)
        path_list = []
        dfs(root, [], path_list)
        return ['->'.join([str(p) for p in path]) for path in path_list]

    def binaryTreePaths2(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(node, prefix, path_list):
            if not node: return
            prefix = '{}->{}'.format(prefix, node.val) if prefix else str(node.val)
            if not node.left and not node.right:
                path_list.append(prefix)
            if node.left:
                dfs(node.left, prefix, path_list)
            if node.right:
                dfs(node.right, prefix, path_list)
        path_list = []
        dfs(root, "", path_list)
        return path_list

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, None, 5], ["1->2->5", "1->3"]),
        ([37, -34, -48, None, -100, -100, 48, None, None, None, None, -54, None, -71, -22, None, None, None, 8], ["37->-34->-100", "37->-48->-100", "37->-48->48->-54->-71", "37->-48->48->-54->-22->8"])
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().binaryTreePaths(parse_tree(test_case[0]))
        print('output:', sorted(output))
        assert sorted(output) == sorted(test_case[1])


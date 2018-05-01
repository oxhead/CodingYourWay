"""
https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii

Related:
  - lt_298_binary-tree-longest-consecutive-sequence
"""

"""
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].

Note: All the values of tree nodes are in the range of [-1e7, 1e7].
"""

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(h)
        # Hint:
        # 1) recursion
        # 2) maintain two path -- increasing and decresing path
        # 3) maintain a global max_length
        # 4) calculate the path length by path_length_inc + path_length_dec - 1 (duplicate paraent)
        # 5) a path is eather increasing or decreasing -- the above calculation is precise
        def dfs(node):
            if not node: return 0, 0
            count_left = dfs(node.left)
            count_right = dfs(node.right)
            count_inc, count_dec = 1, 1
            if node.left:
                if node.left.val == node.val + 1:
                    count_inc = max(count_inc, count_left[0] + 1)
                elif node.left.val == node.val - 1:
                    count_dec = max(count_dec, count_left[1] + 1)
            if node.right:
                if node.right.val == node.val + 1:
                    count_inc = max(count_inc, count_right[0] + 1)
                elif node.right.val == node.val - 1:
                    count_dec = max(count_dec, count_right[1] + 1)
            self.max_count = max(self.max_count, count_inc + count_dec - 1)
            return count_inc, count_dec
        self.max_count = 0
        dfs(root)
        return self.max_count 
        
    def longestConsecutive_TLE(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, previous, count, max_count, up=True):
            if not node:
                return max(max_count, count)
            if (up and node.val != previous + 1) or (not up and node.val != previous - 1):
                count_left_up = dfs(node.left, node.val, 1, max_count, True)
                count_left_down = dfs(node.left, node.val, 1, max_count, False)
                count_right_up = dfs(node.right, node.val, 1, max_count, True)
                count_right_down = dfs(node.right, node.val, 1, max_count, False)
                if node.left:
                    records[(node.left, True)] = count_left_up
                    records[(node.left, False)] = count_left_down
                if node.right:
                    records[(node.right, True)] = count_right_up
                    records[(node.right, False)] = count_right_down
                if node.left and node.right:
                    if node.left.val == node.val - 1 and node.right.val == node.val + 1:
                        return max(max_count, count_left_down + count_right_up - 1, count_left_up, count_right_down)
                    elif node.left.val == node.val + 1 and node.right.val == node.val - 1:
                        return max(max_count, count_left_up + count_right_down - 1, count_left_down, count_right_up)
                return max(max_count, count_left_up, count_left_down, count_right_up, count_right_down)
            else:
                count += 1
                max_count = max(max_count, count)
                return max(max_count, dfs(node.left, node.val, count, max_count, up), dfs(node.right, node.val, count, max_count, up))
        if not root: return 0
        records = {}
        return max(dfs(root, float('inf'), 0, 0, True), dfs(root, float('inf'), 0, 0, False))


if __name__ == '__main__':
    test_cases = [
        ([1, None, 3, 2, 4, None, None, None, 5], 4),
        ([2, None, 3, 2, None, 1], 3),
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, None, 3, None, 5, None, 6, None, 7, None, 8], 4),
        ([1, 2, 3], 2),
        ([2, 1, 3], 3),
        ([3, 1, 2], 2),
        ([2, 1, 4, 3, None, 5], 2),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().longestConsecutive(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


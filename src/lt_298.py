"""
https://leetcode.com/problems/binary-tree-longest-consecutive-sequence

Related:
  - lt_128_longest-consecutive-sequence
  - lt_549_binary-tree-longest-consecutive-sequence-ii
"""

"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,

   1
    \
     3
    / \
   2   4
        \
         5

Longest consecutive sequence path is 3-4-5, so return 3.

   2
    \
     3
    / 
   2    
  / 
 1

Longest consecutive sequence path is 2-3,not3-2-1, so return 2. 
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
        def dfs(node):
            if not node: return 0
            count = 1
            for child in (node.left, node.right):
                if not child: continue
                count_child = dfs(child)
                if child.val == node.val + 1:
                    count = max(count, count_child + 1)
            self.max_count = max(self.max_count, count)
            return count
        self.max_count = 0
        dfs(root)
        return self.max_count

    def longestConsecutive_verbose(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(h)
        def dfs(node, previous, count, max_count):
            if not node: return count
            if node.val == previous + 1:
                count += 1
                max_count = max(max_count, count)
                return max(max_count, dfs(node.left, node.val, count, max_count), dfs(node.right, node.val, count, max_count))
            else:
                return max(max_count, dfs(node.left, node.val, 1, max_count), dfs(node.right, node.val, 1, max_count))
            
        if not root: return 0
        return max(dfs(root.left, root.val, 1, 1), dfs(root.right, root.val, 1, 1))


if __name__ == '__main__':
    test_cases = [
        ([1, None, 3, 2, 4, None, None, None, 5], 3),
        ([2, None, 3, 2, None, 1], 2),
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, None, 3, None, 5, None, 6, None, 7, None, 8], 4),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().longestConsecutive(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/path-sum-iii

Related:
  - lt_112_path-sum
  - lt_113_path-sum-ii
  - lt_666_path-sum-iv
  - lt_687_longest-univalue-path
"""

"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
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
        :rtype: int
        """
        # Time: O(n)
        # Space: O(h)
        # http://rainykat.blogspot.com/2017/01/leetcode-437-path-sum-iii-2dfs.html
        def search(node, sum):
            if not node: return 0
            count = 0
            if node.val == sum: count += 1
            count += search(node.left, sum - node.val)
            count += search(node.right, sum - node.val)
            return count
        if not root: return 0
        return search(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)       
 
    def pathSum_failed(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root: return 0
        print('node={}, sum={}'.format(root.val, sum))
        count = 1 if root.val == sum else 0
        return count + self.pathSum(root.left, sum) + self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum) + self.pathSum(root.right, sum - root.val)

if __name__ == '__main__':
    test_cases = [
        (([], 1), 0),
        (([10, None, -3, None, 11], 8), 1),
        (([8, None, -3, None, 11], 8), 2),
        (([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8), 3),
        (([1, None, 2, None, 3, None, 4, None, 5], 3), 2),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().pathSum(parse_tree(test_case[0][0]), test_case[0][1])
        print('output:', output)
        assert output == test_case[1]


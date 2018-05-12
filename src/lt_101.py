"""
https://leetcode.com/problems/symmetric-tree

Related:
"""

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively. 
"""

from utils import parse_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(1)
        # Hints:
        # 1) Recursion check
        def is_matched(left, right):
            if not left and not right: return True
            if not left or not right: return False
            if left.val != right.val: return False
            return is_matched(left.left, right.right) and is_matched(left.right, right.left)
        if not root: return True
        return is_matched(root.left, root.right)

    def isSymmetric_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(h), h is the tree height
        if not root: return True
        q = [root, root]
        while q:
            n1, n2 = q.pop(), q.pop()
            if not n1 and not n2: continue
            if not n1 or not n2: return False
            if n1.val != n2.val: return False
            q.append(n1.left)
            q.append(n2.right)
            q.append(n1.right)
            q.append(n2.left)
        return True


if __name__ == '__main__':
    test_cases = [
        ([], True),
        ([1], True),
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False),
        ([3, 9, 20, None, None, 15, 7], False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isSymmetric(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


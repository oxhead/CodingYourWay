"""
https://leetcode.com/problems/two-sum-iv-input-is-a-bst

Related:
  - lt_1_two-sum
  - lt_167_two-sum-ii-input-array-is-sorted
  - lt_170_two-sum-iii-data-structure-design
"""

"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""
import collections

from utils import print_tree, parse_tree

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(h)
        # https://github.com/kamyu104/LeetCode/blob/master/Python/two-sum-iv-input-is-a-bst.py
        class BSTIterator:
            def __init__(self, root, forward):
                self.node = root
                self.forward = forward
                self.stack = collections.deque()
                self.val = None
                self.next()

            def value(self):
                return self.val

            def next(self):
                while self.node or self.stack:
                    if self.node:
                        self.stack.append(self.node)
                        self.node = self.node.left if self.forward else self.node.right
                    else:
                        self.node = self.stack.pop()
                        self.val = self.node.val
                        self.node = self.node.right if self.forward else self.node.left
                        break
        if not root: return False
        left, right = BSTIterator(root, True), BSTIterator(root, False)
        while left.value() < right.value():
            if left.value() + right.value() == k:
                return True
            elif left.value() + right.value() < k:
                left.next()
            else:
                right.next()
        return False

    def findTarget_set(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        def traverse(node):
            if not node: return False
            elif node.val in records: return True
            else:
                records.add(k - node.val)
                return traverse(node.left) or traverse(node.right)
        records = set()
        return traverse(root)
        

if __name__ == '__main__':
    test_cases = [
        (([5, 3, 6, 2, 4, None, 7], 9), True),
        (([5, 3, 6, 2, 4, None, 7], 28), False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findTarget(parse_tree(test_case[0][0]), test_case[0][1])
        print('output:', output)
        assert output == test_case[1]


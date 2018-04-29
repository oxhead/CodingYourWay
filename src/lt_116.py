"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node

Related:
  - lt_117_populating-next-right-pointers-in-each-node-ii
  - lt_199_binary-tree-right-side-view
"""

"""
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

    You may only use constant extra space.
    Recursive approach is fine, implicit stack space does not count as extra space for this problem.
    You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7

After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
"""

from utils import parse_tree

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        if root.left: root.left.next = root.right
        if root.right and root.next: root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

    def connect_failed(self, root):
        def build(node, left, right, right_left):
            if not left and not right:
                if right_left:
                    node.next = right_left
            else:
                left.next = right
                build(left, left.left, left.right, right.left)
                build(right, right.left, right.right, right_left)
            
        if not root: return
        else:
            build(root, root.left, root.right, None)

    def connect(self, root)
        # Time: O(n)
        # Space: O(1)
        head = root
        while head:
            current = head
            while current and current.left:
                current.left.next = current.right
                if current.next:
                    current.right.next = current.next.left
                current = current.next
            head = head.left

if __name__ == '__main__':
    test_cases = [
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().connect(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


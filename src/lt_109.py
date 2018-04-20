"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

Related:
  - lt_108_convert-sorted-array-to-binary-search-tree
"""

"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""

from base import ListNode, TreeNode
from utils import to_linked_list, to_list
from utils import serialize_tree, print_tree, is_height_balanced_bst

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # Time: O(n * logn)
        # Space: O(1)
        def find_middle(node):
            previous = None
            if not node or not node.next: return node, previous
            slow, fast = node, node
            while fast and fast.next:
                previous = slow
                slow = slow.next
                fast = fast.next.next
            return slow, previous
        if not head: return None 
        middle, previous = find_middle(head) 
        if previous:
            previous.next = None
        new_root = TreeNode(middle.val)
        if previous:
           new_root.left = self.sortedListToBST(head) 
        new_root.right = self.sortedListToBST(middle.next)
        return new_root
        

if __name__ == '__main__':
    test_cases = [
        ([-10, -3, 0, 5, 9], None),
        ([], None),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        root = Solution().sortedListToBST(to_linked_list(test_case[0]))
        print('@@', serialize_tree(root))
        print('output:', is_height_balanced_bst(root))
        assert is_height_balanced_bst(root)


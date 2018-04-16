"""
https://leetcode.com/problems/reorder-list

Related:
"""

"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""

from base import ListNode
from utils import to_linked_list, to_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # Time: O(n)
        # Space: O(1)
        def reverse_list(node):
            previous = None
            while node:
                node.next, previous, node = previous, node, node.next
            return previous
        # split the list into half
        dummy = ListNode(None)
        dummy.next = head
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1, head2 = head, slow.next
        slow.next = None
        head2 = reverse_list(head2)
        # combine
        dummy = ListNode(None)
        node = dummy
        while head1 and head2:
            tmp = head1.next
            node.next, head1 = head1, head.next
            node.next.next, node, head2 = head2, head2, head2.next
            head1 = tmp
        node.next = head1 if head1 else head1
        

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4], [1, 4, 2, 3]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        head = to_linked_list(test_case[0])
        Solution().reorderList(head)
        print('output:', to_list(head))
        assert to_list(head) == test_case[1]

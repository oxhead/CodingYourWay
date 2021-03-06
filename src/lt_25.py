"""
https://leetcode.com/problems/reverse-nodes-in-k-group

Related:
  - lt_24_swap-nodes-in-pairs
"""

"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

from utils import to_linked_list, to_list
from base import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Time: O(n)
        # Space: O(1)
        def reverse(start, end):
            first = start.next
            current = first.next
            while current != end:
                first.next = current.next
                current.next = start.next
                start.next = current
                current = first.next

        dummy = ListNode(-1)
        dummy.next = head
        current, current_dummy = head, dummy
        count = 0
        while current:
            next_current = current.next
            count = (count + 1) % k
            if count == 0:
                next_dummy = current_dummy.next
                reverse(current_dummy, current.next)
                current_dummy = next_dummy
            current = next_current
        return dummy.next

    def reverseKGroup_failed(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(head, k):
            previous = None
            for _ in range(k):
                head.next, previous, head = previous, head, head.next
            return previous.next

        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        while current:
            current.next = reverse(current.next, k)
        return dummy.next

    def reverseKGroup_attempt2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        dummy = ListNode(None)
        previous = dummy
        node = head
        for i in range(count // k):
            for j in range(k):
                print(i, j)
                previous.next, node.next, node.next.next = node.next, node.next.next, node
                node = previous.next.next
                previous = node
        return dummy.next

    def reverseKGroup_v2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(start, end):
            previous = None
            node = start
            while node and node != end:
                node.next, previous, node = previous, node, node.next
            return previous
        dummy = ListNode(None)
        previous_group_end = None
        group_start = head
        node = head
        count = 0
        while node:
            node = node.next
            count = (count + 1) % k
            if count == 0:
                group_head = reverse(group_start, node)
                if dummy.next is None:
                    dummy.next = group_head
                if previous_group_end:
                    previous_group_end.next = group_head 
                group_start.next = node
                previous_group_end = group_start
                group_start = node
        return dummy.next if dummy.next else head
                
       

if __name__ == '__main__':
    test_cases = [
        (([1], 2), [1]),
        (([1, 2, 3, 4, 5], 2), [2, 1, 4, 3, 5]),
        (([1, 2, 3, 4, 5], 3), [3, 2, 1, 4, 5]),
        (([1, 2, 3, 4, 5], 4), [4, 3, 2, 1, 5]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().reverseKGroup(to_linked_list(test_case[0][0]), test_case[0][1])
        print('output:', to_list(output))
        assert to_list(output) == test_case[1]


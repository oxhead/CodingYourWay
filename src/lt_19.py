"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list

Related:
"""

"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
"""

from utils import to_linked_list, to_list
from base import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Time: O(n)
        # Space: O(1)
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        for i in range(n):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next

    def removeNthFromEnd_v2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        previous, slow, fast = None, head, head
        count = 0
        while fast:
            if count >= n:
                previous, slow = slow, slow.next
            fast = fast.next
            count += 1
        if not previous:
            head = head.next
        else:
            previous.next = slow.next
        return head

    def removeNthFromEnd_array(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Time: O(n)
        # Space: O(n)
        data = []
        node = head
        while node:
            data.append(node)
            node = node.next
        if n == 1:
            if len(data) == 1:
                return None
            else:
                data[-2].next = None
        elif n == len(data):
            head = head.next
        else:
            data[-(n + 1)].next = data[-n].next
        return head

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        previous, slow, fast = None, head, head
        count = 0
        while fast:
            if count >= n:
                previous, slow = slow, slow.next
            fast = fast.next
            count += 1
        if not previous:
            head = head.next
        else:
            previous.next = slow.next
        return head


if __name__ == '__main__':
    test_cases = [
        (([1, 2, 3, 4, 5], 2), [1, 2, 3, 5]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().removeNthFromEnd(to_linked_list(test_case[0][0]), test_case[0][1])
        print('output:', to_list(output))
        assert to_list(output) == test_case[1]


"""
https://leetcode.com/problems/swap-nodes-in-pairs

Related:
  - lt_25_reverse-nodes-in-k-group
"""

"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""

from utils import to_linked_list, to_list
from base import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            next_1, next_2, next_3 = current.next, current.next.next, current.next.next.next
            current.next = next_2
            next_2.next = next_1
            next_1.next = next_3
            current = next_1
        return dummy.next

    def swapPairs_illegal(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        count = 0
        previous = None
        node = head
        while node:
            count += 1
            if count % 2 != 0:
                previous = node
            else:
                previous.val, node.val = node.val, previous.val 
            node = node.next
        return head

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4], [2, 1, 4, 3]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().swapPairs(to_linked_list(test_case[0]))
        print('output:', to_list(output))
        assert to_list(output) == test_case[1]


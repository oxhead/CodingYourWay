"""
https://leetcode.com/problems/merge-k-sorted-lists

Related:
  - lt_21_merge-two-sorted-lists
  - lt_264_ugly-number-ii
"""

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity. 
"""

import heapq

from base import ListNode
from utils import to_list, to_linked_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Time: O(n*logn*logk), n is the length of a list, k is the number of sorted lists
        # Space: O(1)
        if not lists: return None
        if len(lists) == 0: return None
        elif len(lists) == 1: return lists[0]
        elif len(lists) == 2: return self.mergeTwoLists(lists[0], lists[1])
        return self.mergeTwoLists(self.mergeKLists(lists[:len(lists)//2]),
				  self.mergeKLists(lists[len(lists)//2:]))

    def mergeKLists_naive(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # exceeds time limit
        if not lists: return None
        if len(lists) == 0: return None
        elif len(lists) == 1: return lists[0]

        merged_list = lists[0]
        for l in lists[1:]:
            merged_list = self.mergeTwoLists(merged_list, l)
        return merged_list

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        dummy = ListNode(-1)
        node = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1: node.next = l1
        if l2: node.next = l2
        return dummy.next

    def mergeKLists_heap(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Time: O(n*k*logk), n is the length of a list, k is the number of sorted lists
        # Space: O(logk)
        # works only in Python 2.x
        # because heapq requires object comparaison
        # Python 2.x uses __cmp__(self, other)
        # Python 3.x uses __lt__(self, other)
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))

        current = ListNode(-1)
        head = current
        while heap:
            node = heapq.heappop(heap)[1]
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))

        return head.next


if __name__ == '__main__':
    test_cases = [
        ([], []),
        ([[1, 2, 4], [1, 3, 4]], [1, 1, 2, 3, 4, 4]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().mergeKLists([to_linked_list(l) for l in test_case[0]])
        print('output:', to_list(output))
        assert to_list(output) == test_case[1]


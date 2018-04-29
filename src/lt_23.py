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
        # Time: O(n*logk), n is the total number of items, k is the number of sorted lists
        # Space: O(1)
        def merge_two_lists(list1, list2):
            if not list1: return list2
            if not list2: return list1
            dummy = ListNode(None)
            node = dummy
            while list1 and list2:
                if list1.val <= list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next
            if list1: node.next = list1
            elif list2: node.next = list2
            return dummy.next
        if not lists: return None
        elif len(lists) == 1: return lists[0]
        return merge_two_lists(self.mergeKLists(lists[:len(lists)//2]), self.mergeKLists(lists[len(lists)//2:]))

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
        # Time: O(n*logk)
        # Space: O(logk)
        # Note:
        # the common implementation works only in Python 2.x
        # because heapq requires object comparaison
        # Python 2.x uses __cmp__(self, other)
        # Python 3.x uses __lt__(self, other)
        # a trick is used here to support Python 3.x
        heap = []
        for index, node in enumerate(lists):
            if node:
                # to support Python 3.x
                # it is fine here because no duplicate index exists
                heapq.heappush(heap, (node.val, index, node))
        dummy = ListNode(None)
        current = dummy
        while heap:
            index, node = heapq.heappop(heap)[1:]
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))
        return dummy.next


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


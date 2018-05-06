"""
https://leetcode.com/problems/merge-two-sorted-lists

Related:
  - lt_23_merge-k-sorted-lists
  - lt_88_merge-sorted-array
  - lt_148_sort-list
  - lt_244_shortest-word-distance-ii
"""

"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

from base import ListNode
from utils import to_list, to_linked_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Time: O(min(m, n))
        # Space: O(1)
        if not l1: return l2
        elif not l2: return l1
        dummy = ListNode(None)
        node = dummy
        while l1 or l2:
            n1 = l1.val if l1 else float('inf')
            n2 = l2.val if l2 else float('inf')
            node.next = l1 if n1 <= n2 else l2
            l1 = l1.next if n1 <= n2 else l1
            l2 = l2.next if n2 < n1 else l2
            node = node.next
        return dummy.next

    def mergeTwoLists_v2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Time: O(min(m, n))
        # Space: O(1)
        if not l1: return l2
        if not l2: return l1
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        current = head
        while l1 and l2:
            if l1.val <= l2.val:
                current.next, l1 = l1, l1.next
            else:
                current.next, l2 = l2, l2.next
            current = current.next    
        if l1: current.next = l1
        if l2: current.next = l2
        return head


if __name__ == '__main__':
    test_cases = [
        (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().mergeTwoLists(to_linked_list(test_case[0][0]), to_linked_list(test_case[0][1]))
        print('output:', to_list(output))
        assert to_list(output) == test_case[1]


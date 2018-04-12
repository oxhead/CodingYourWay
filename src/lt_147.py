"""
https://leetcode.com/problems/insertion-sort-list

Related:
  - lt_148_sort-list
"""

"""
Sort a linked list using insertion sort.
"""

from utils import to_linked_list, to_list
from base import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Time: O(n^2)
        # Space: O(1)
        if not head: return head
        dummy = ListNode(float('-inf'))
        dummy.next = head
        current = head.next
        sorted_tail = head
        while current:
            previous = dummy
            while previous.next.val < current.val:
                previous = previous.next
            if previous == sorted_tail:
                current, sorted_tail = current.next, current
            else:
                current.next, previous.next, sorted_tail.next = previous.next, current, current.next
                current = sorted_tail.next
        return dummy.next


if __name__ == '__main__':
    test_cases = [
        ([2, 1, 3, 5, 4], [1, 2, 3, 4, 5]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().insertionSortList(to_linked_list(test_case[0]))
        print('output:', to_list(output))
        assert to_list(output) == test_case[1]


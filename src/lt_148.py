"""
https://leetcode.com/problems/sort-list

Related:
  - lt_21_merge-two-sorted-lists
  - lt_75_sort-colors
  - lt_147_insertion-sort-list
"""

"""
Sort a linked list in O(n log n) time using constant space complexity.
"""

from utils import to_linked_list, to_list
from base import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # https://www.tangjikai.com/algorithms/leetcode-148-sort-list
        def merge(left, right):
            dummy = current = ListNode(-1)
            while left and right:
                if left.val <= right .val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                current = current.next
            current.next = left or right
            return dummy.next

        if not head or not head.next: return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = self.sortList(slow.next)
        slow.next = None
        left = self.sortList(head)
        return merge(left, right)


if __name__ == '__main__':
    test_cases = [
        ([2, 1, 3, 5, 4], [1, 2, 3, 4, 5]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().sortList(to_linked_list(test_case[0]))
        print('output:', to_list(output))
        assert to_list(output) == test_case[1]


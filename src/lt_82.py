"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

Related:
"""

"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3. 
"""

from base import ListNode
from utils import to_list, to_linked_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Time: O(n)
        # Space: O(1)
        if not head or not head.next: return head
        dummy = ListNode(None)
        previous, current = dummy, head
        while current:
            if current.next and current.next.val == current.val:
                val = current.val
                while current and current.val == val:
                    current = current.next
                previous.next = current
            else:
                previous.next = current
                previous = current
                current = current.next
        return dummy.next


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], [1, 2, 3]),
        ([1, 1, 2, 3], [2, 3]),
        ([1, 2, 2, 3], [1, 3]),
        ([1, 2, 3, 3], [1, 2]),
        ([1, 1, 2, 2, 3], [3]),
        ([1, 1, 2, 3, 3], [2]),
        ([1, 2, 2, 3, 3], [1]),
        ([1, 1, 2, 2, 3, 3], []),
        ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
        ([1, 1, 1, 2, 3], [2, 3]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().deleteDuplicates(to_linked_list(test_case[0]))
        print('output:', to_list(output))
        assert to_list(output) == test_case[1]


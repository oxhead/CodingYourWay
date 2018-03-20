"""
https://leetcode.com/problems/remove-linked-list-elements

Related:
  - lt_27_remove-element
  - lt_237_delete-node-in-a-linked-list
"""

"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5 
"""

from base import ListNode
from utils import to_linked_list, to_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # Time: O(n)
        # Space: O(1)
        if not head: return head
        dummy = ListNode(-1)
        dummy.next = head
        previous = dummy
        node = head 
        while node:
            if node.val == val:
                previous.next = node.next
            else:
                previous = node
            node = node.next
        return dummy.next

if __name__ == '__main__':
    test_cases = [
        (([1], 1), []),
        (([1, 1], 1), []),        
        (([1, 2, 6, 3, 4, 5, 6], 6), [1, 2, 3, 4, 5]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        root = Solution().removeElements(to_linked_list(test_case[0][0]), test_case[0][1])
        print('output:', to_list(root))
        assert to_list(root) == test_case[1]


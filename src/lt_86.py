"""
https://leetcode.com/problems/partition-list

Related:
"""

"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

from base import ListNode
from utils import to_linked_list, to_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # Time: O(n)
        # Space: O(1)
        left_head = left = ListNode(-1)
        right_head = right = ListNode(-1)
        node = head
        while node:
            if node.val < x:
                left.next = node
                left = left.next
            else:
                right.next = node
                right = right.next
            node = node.next
        left.next = right_head.next
        right.next = None
        return left_head.next


if __name__ == '__main__':
    test_cases = [
        (([1, 4, 3, 2, 5, 2], 3), [1, 2, 2, 4, 3, 5]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().partition(to_linked_list(test_case[0][0]), test_case[0][1])
        print('output:', to_list(output))
        assert to_list(output) == test_case[1]


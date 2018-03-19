"""
https://leetcode.com/problems/reverse-linked-list-ii

Related:
  - lt_206_reverse-linked-list
"""

"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. 
"""

from base import ListNode
from utils import to_linked_list, to_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # Time: O(n)
        # Space: O(1)
        def reverse(node, k):
            previous = None
            while k > 0:
                node.next, previous, node = previous, node, node.next
                k -= 1
            return previous, node

        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        for _ in range(m-1):
            node = node.next
        reverse_tail = node.next
        reverse_head, reverse_tail_next = reverse(node.next, n - m + 1)
        node.next = reverse_head
        reverse_tail.next = reverse_tail_next
        return dummy.next


if __name__ == '__main__':
    test_cases = [
        (([1, 2, 3, 4, 5], 2, 4), [1, 4, 3, 2, 5]),
        (([1, 2, 3, 4, 5], 1, 5), [5, 4, 3, 2, 1]),
        (([1, 2, 3, 4, 5], 1, 1), [1, 2, 3, 4, 5]),
        (([1, 2, 3, 4, 5], 5, 5), [1, 2, 3, 4, 5]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().reverseBetween(to_linked_list(test_case[0][0]), test_case[0][1], test_case[0][2])
        print('output:', to_list(output))
        assert to_list(output) == test_case[1]


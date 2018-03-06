"""
https://leetcode.com/problems/add-two-numbers

Related:
  - lt_43_multiply-strings
  - lt_67_add-binary
  - lt_371_sum-of-two-integers
  - lt_415_add-strings
  - lt_445_add-two-numbers-ii
"""

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

from utils import to_linked_list, to_list
from base import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Time: O(n), n is the maximum number of digits of the two integers
        # Space: O(1)
        dummy = ListNode(-1)
        node = dummy
        carry = 0
        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            n = n1 + n2  + carry
            carry = n // 10
            n = n % 10
            node.next = ListNode(n)
            node = node.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return dummy.next

if __name__ == '__main__':
    test_cases = [
        ((5, 5), 10),
        ((342, 465), 807),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        l1 = to_linked_list([int(x) for x in reversed(list(str(test_case[0][0])))])
        l2 = to_linked_list([int(x) for x in reversed(list(str(test_case[0][1])))])
        output = Solution().addTwoNumbers(l1, l2)
        print('output:', to_list(output))
        assert to_list(output) == [int(x) for x in reversed(list(str(test_case[1])))]


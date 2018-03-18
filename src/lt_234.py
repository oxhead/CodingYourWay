"""
https://leetcode.com/problems/palindrome-linked-list

Related:
  - lt_9_palindrome-number
  - lt_125_valid-palindrome
  - lt_206_reverse-linked-list
"""

"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""

from utils import to_linked_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def find_middle_node(node):
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        def reverse(node):
            previous = None
            while node:
                node.next, previous, node = previous, node, node.next
            return previous

        middle = find_middle_node(head)
        head2 = reverse(middle)
        while head2:
            if head.val != head2.val: return False
            head = head.next
            head2 = head2.next
        return True

    def isPalindrome_naive(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        tmp = head
        while tmp:
            stack.append(tmp.val)
            tmp = tmp.next
        while head:
            if len(stack) == 0: return False
            if stack.pop() != head.val: return False
            head = head.next
        return True


if __name__ == '__main__':
    test_cases = [
        ([], True),
        ([1], True),
        ([1, 2, 1], True),
        ([1, 1], True),
        ([1, 2], False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isPalindrome(to_linked_list(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


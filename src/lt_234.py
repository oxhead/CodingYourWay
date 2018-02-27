"""
https://leetcode.com/problems/palindrome-linked-list

Related:
  - lt_9
  - lt_125
  - lt_206

Complexity:
  - Time: O()
  - Space: O()
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

    def isPalindrome_advance(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_middle = self.find_middle_node(head)
        head2 = self.reverse_node(node_middle)
        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True

    def find_middle_node(self, node):
        fast = slow = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_node(self, node):
        if not node or not node.next: return node
        previous = None
        current = node
        while current:
            current.next, previous, current = previous, current, current.next
        return previous

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


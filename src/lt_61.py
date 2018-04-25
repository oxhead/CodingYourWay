"""
https://leetcode.com/problems/rotate-list

Related:
  - lt_189_rotate-array
  - lt_725_split-linked-list-in-parts
"""

"""
Given a list, rotate the list to the right by k places, where k is non-negative.

Example:

Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.
"""

from utils import to_linked_list, to_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0: return head

        tail = head
        count = 1
        while tail.next:
            count += 1
            tail = tail.next
        if count == k: return head
        node = head
        for _ in range(count - k % count - 1):
            node = node.next
        tail.next = head
        head = node.next
        node.next = None
        return head
        
    def rotateRight_cycle(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0: return head
        n = 0
        tail = head
        while tail.next:
            n += 1
            tail = tail.next
        n += 1

        remaining_steps = n - k % n
        if remaining_steps == n: return head

        tail.next = head
        for _ in range(remaining_steps):
            tail = tail.next
        head = tail.next
        tail.next = None
        return head

    def rotateRight_v2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head
        node = head
        count = 1
        while node.next:
            node = node.next
            count += 1
        node.next = head
        tail = node
        slow = fast = head
        for _ in range(k % count):
            fast = fast.next
        while fast != tail:
            slow = slow.next
            fast = fast.next
        head = slow.next
        slow.next = None
        return head

if __name__ == '__main__':
    test_cases = [
         (([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3]),
         (([1, 2, 3], 2000000000), [2, 3, 1]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        nums, k = test_case[0]
        root = Solution().rotateRight(to_linked_list(nums), k)
        print('output:', to_list(root))
        assert to_list(root) == test_case[1]


"""
https://leetcode.com/problems/reverse-linked-list

Related:
  - lt_92
  - lt_156
  - lt_234

Complexity:
  - Time: O(n)
  - Space: O(1)
"""

"""
Reverse a singly linked list.

click to show more hints.
Hint:

    A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

from utils import to_linked_list, to_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous = None
        while head:
            head.next, previous, head = previous, head, head.next
        return previous

    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        s = list()
        while head != None:
            s.append(head)
            head = head.next
        
        new_head = s[-1] if len(s) > 0 else None
        
        while len(s) > 0:
            n = s.pop()
            n.next = s[-1] if len(s) > 0 else None
            
        return new_head

if __name__ == '__main__':
    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [3, 2, 1])
    ]

    for test_case in test_cases:
        print('case:', test_case)
        root = to_linked_list(test_case[0])
        root_new = Solution().reverseList(root)
        print('output:', to_list(root_new))
        assert to_list(root_new) == test_case[1]


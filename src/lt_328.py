"""
https://leetcode.com/problems/odd-even-linked-list

Related:
  - lt_725

Complexity:
  - Time:
  - Space:
"""

"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ... 
"""

from base import ListNode
from utils import to_linked_list, to_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # http://rainykat.blogspot.com/2017/04/leetcode-328-odd-even-linked-list.html
        if not head: return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

    def oddEvenList_naive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        odd_start = head
        even_start = head.next
        odd = odd_start
        even = even_start
        count = 2
        node = head.next.next
        while node:
            count += 1
            if count % 2 == 1:
                odd.next = node
                odd = odd.next
            else:
                even.next = node
                even = even.next
            node = node.next
        # reset last node to odd, if it exists
        even.next = None
        odd.next = even_start
        return odd_start

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 5, 7, 2, 4, 6, 8]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().oddEvenList(to_linked_list(test_case[0]))
        print('output:', to_list(output))
        assert to_list(output) == test_case[1]


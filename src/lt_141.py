"""
https://leetcode.com/problems/linked-list-cycle

Related:
  - lt_142

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space? 
"""

from utils import to_linked_list_by_pairs

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        head1 = head
        head2 = head.next
        while head1 and head2:
            if head1 == head2: return True
            head1 = head1.next
            head2 = head2.next
            if head2: head2 = head2.next
        return False
        
if __name__ == '__main__':
    test_cases = [
        ([(1, 2)], False),
        ([(1, 2), (2, 3)], False),
        ([(1, 2), (2, 3), (3, 2)], True),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().hasCycle(to_linked_list_by_pairs(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


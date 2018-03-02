"""
https://leetcode.com/problems/linked-list-cycle

Related:
  - lt_141
  - lt_287

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

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
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return None

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None
        
if __name__ == '__main__':
    test_cases = [
        ([(1, None)], None),
        ([(1, 2)], None),
        ([(1, 2), (2, 3)], None),
        ([(1, 2), (2, 3), (3, 2)], 2),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().detectCycle(to_linked_list_by_pairs(test_case[0]))
        print('output:', output.val if output else None)
        if test_case[1]:
            if output:
                assert output.val == test_case[1]
            else:
                assert False
        else:
            assert output == None


"""
https://leetcode.com/problems/linked-list-cycle

Related:
  - lt_142_linked-list-cycle-ii
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
        # Time: O(n)
        # Space: O(1)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
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


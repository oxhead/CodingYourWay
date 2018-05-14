"""
https://leetcode.com/problems/linked-list-cycle

Related:
  - lt_141_linked-list-cycle
  - lt_287_find-the-duplicate-number
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
        # Time: O(n)
        # Space: O(1)
        # https://www.quora.com/How-does-Floyds-cycle-finding-algorithm-work-How-does-moving-the-tortoise-to-the-beginning-of-the-linked-list-while-keeping-the-hare-at-the-meeting-place-followed-by-moving-both-one-step-at-a-time-make-them-meet-at-starting-point-of-the-cycle
        # x: distance from head to where the cycle begins
        # y: distance from where the cycle begins to the meeting point
        # z: distance from the meeting point to where the cycle begins
        # the slow pointer travels x + y
        # the fast pointer travels x + y + z + y = x + 2y + z
        # since the faster pointer travels at 2x speed of the slow pointer
        # 2 * (x + y) = x + 2y + z
        # x = z
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

    def detectCycle_v2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head.next
        while fast and fast.next and fast != slow:
            fast = fast.next.next
            slow = slow.next
        if not fast: return None
        if not fast == slow: return None
        fast = head.next
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast


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


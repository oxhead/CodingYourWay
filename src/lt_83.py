"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list

Related:
"""

"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3. 
"""

from utils import to_list, to_linked_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Time: O(n)
        # Space: O(1)
        if not head or not head.next: return head
        previous = head
        node = previous.next
        while node:
            if node.val == previous.val:
                previous.next = node.next
            else:
                previous = node
            node = node.next   
        return head


if __name__ == '__main__':
    test_cases = [
        ([1, 1, 2], [1, 2]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
        ([1, 2, 3, 3, 3, 4], [1, 2, 3, 4]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().deleteDuplicates(to_linked_list(test_case[0]))
        print('output:', to_list(output))
        assert to_list(output) == test_case[1]


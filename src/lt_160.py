"""
https://leetcode.com/problems/intersection-of-two-linked-lists

Related:

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3

begin to intersect at node c1.

Notes:

    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.
"""

from utils import to_intersected_linked_list_by_pairs

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        stepsA = self.get_path_length(headA)
        stepsB = self.get_path_length(headB)
        nodeA = headA
        nodeB = headB
        if stepsA > stepsB:
            for _ in range(stepsA - stepsB):
                nodeA = nodeA.next
        if stepsB > stepsA:
            for _ in range(stepsB - stepsA):
                nodeB = nodeB.next
        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        return None

    def get_path_length(self, head):
        tmp = head
        count = 0
        while tmp:
            count += 1
            tmp = tmp.next
        return count

if __name__ == '__main__':
    test_cases = [
        (([('a1', 'a2'), ('a2', 'c1'), ('b1', 'b2'), ('b2', 'b3'), ('b3', 'c1'), ('c1', 'c2'), ('c2', 'c3')], 'a1', 'b1'), 'c1'),
        (([('a1', 'a2'), ('b1', 'b2'), ('b2', 'b3')], 'a1', 'b1'), None),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        headA, headB, headIntersect = to_intersected_linked_list_by_pairs(test_case[0][0], test_case[0][1], test_case[0][2], test_case[1])
        output = Solution().getIntersectionNode(headA, headB)
        print('output:', output.val if output else None)
        if test_case[1]:
             if headIntersect: assert headIntersect.val == test_case[1]
             else: assert headIntersect != None
        else:
             assert headIntersect == None

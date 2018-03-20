"""
https://leetcode.com/problems/delete-node-in-a-linked-list

Related:
  - lt_203_remove-linked-list-elements
"""

"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function. 
"""

from utils import to_linked_list, to_list, find_node_by_index


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Time: O(1)
        # Space: O(1)
        if node and node.next:
            node.val = node.next.val
            node.next = node.next.next


if __name__ == '__main__':
    test_cases = [
        # (linked list, element id), output
        (([1, 2, 3, 4], 2), [1, 2, 4]),
        # does not need to consider removing the tail node
        # (([1, 2, 3, 4], 3), [1, 2, 3]),
        (([1, 2, 3, 4], 0), [2, 3, 4]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        root = to_linked_list(test_case[0][0])
        node = find_node_by_index(root, test_case[0][1])
        output = Solution().deleteNode(node)
        print('output:', to_list(root))
        assert to_list(root) == test_case[1]


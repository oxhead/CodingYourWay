"""
https://leetcode.com/problems/copy-list-with-random-pointer

Related:
  - lt_133_clone-graph
"""

"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list. 
"""

from base import RandomListNode
from utils import to_random_list, to_random_linked_list

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # Time: O(n)
        # Space: O(1)
        # https://blog.csdn.net/tmylzq187/article/details/50913211
        if not head: return head

        # duplicate nodes and attach duplicates to themself
        node = head
        while node:
            node_copied = RandomListNode(node.label)
            node_copied.next = node.next
            node.next = node_copied
            node = node.next.next

        # copy the random pointer
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next

        # detach duplicates
        node = head
        new_head = node.next
        while node:
            node.next.next, node.next = node.next.next.next if node.next.next else None, node.next.next
            node = node.next
        return new_head
        
    def copyRandomList_hashtable(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        records = {}
        node = head
        dummy = RandomListNode(0)
        node_new = dummy
        while node:
            node_clone = RandomListNode(node.label)
            node_new.next = node_clone
            node_new = node_clone
            records[node] = node_clone
            node = node.next
            
        node = head
        while node:
            records[node].random = records[node.random] if node.random else None 
            node = node.next
        return dummy.next


if __name__ == '__main__':
    test_cases = [
        (([], []), ([], [])),
        (([-1, -1], [None, None]), ([-1, -1], [None, None])),
        (([1, 2, 3], [None, None]), ([1, 2, 3], [None, None, None])),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().copyRandomList(to_random_linked_list(*test_case[0]))
        print('output:', to_random_list(output))
        assert to_random_list(output) == test_case[1]


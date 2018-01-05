from base import ListNode
from utils import to_linked_list, to_list

class Solution:
    def reverseList1(self, head):
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

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current_node = head
        previous_node = None
        while current_node != None:
            tmp = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = tmp
        return previous_node

if __name__ == '__main__':
    test_cases = [
        [],
        [1],
        [1, 2, 3]
    ]

    for test_case in test_cases:
        print('case:', test_case)
        node = Solution().reverseList(to_linked_list(test_case))
        print('output:', to_list(node))
        assert to_list(node) == list(reversed(test_case))


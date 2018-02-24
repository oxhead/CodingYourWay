from linked_list import ListNode

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        s = list()
        while head != None:
            s.append(head)
            head = head.next
        
        new_head = s[-1] if len(s) > 1 else None
        
        while len(s) > 0:
            n = s.pop()
            n.next = s[-1] if len(s) > 0 else None
            
        return new_head

def to_linked_list(numbers):
    head = ListNode('#') 
    ptr = head
    for n in numbers:
        ptr.next = ListNode(n)
        ptr = ptr.next

    return head.next

def to_list(node):
    l = list()
    while node != None:
        l.append(node.value)
        node = node.next
    return l

if __name__ == '__main__':
    d1 = []
    l1 = to_linked_list(d1)
    assert to_list(l1) == d1

    d2 = [1]
    l2 = to_linked_list(d2)
    assert to_list(l2) == d2

    d3 = [1, 2, 3]
    l3 = to_linked_list(d3)
    assert to_list(l3) == d3

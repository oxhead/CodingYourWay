from base import ListNode

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

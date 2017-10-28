import unittest

from ds.linked_list import ListNode

class LinkedListTestCase(unittest.TestCase):
    def test_node(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        assert node1.value == 1
        assert node1.next == node2


if __name__ == '__main__':
    unittest.main()

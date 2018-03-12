"""
https://leetcode.com/problems/lru-cache

Related:
  - lt_460_lfu-cache
  - lt_588_design-in-memory-file-system
  - lt_604_design-compressed-string-iterator
"""

"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

from collections import OrderedDict

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.previous = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        node.next, node.previous = None, None
        if not self.head:
            self.head = node
        else:
            self.tail.next, node.previous = node, self.tail
        self.tail = node

    def delete(self, node):
        if node.previous:
            node.previous.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.previous = node.previous
        else:
            self.tail = node.previous
        node.next, node.previous = None, None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.store = {}
        self.access_list = DoubleLinkedList()

    def _add_item(self, key, val):
        item = ListNode(key, val)
        self.access_list.insert(item)
        self.store[key] = item

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # Time: O(1)
        # Space: O(1)
        if key not in self.store: return -1
        item = self.store[key]
        self.access_list.delete(item)
        self._add_item(key, item.val)
        return item.val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # Time: O(1)
        # Space: O(k)
        if key in self.store:
            self.access_list.delete(self.store[key])
        elif len(self.store) == self.capacity:
            del self.store[self.access_list.head.key]
            self.access_list.delete(self.access_list.head)
        self._add_item(key, value)


class LRUCache_OrderedDict:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.store = OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.store:
            return -1
        val = self.store[key]
        del self.store[key]
        self.store[key] = val
        return val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.store:
            del self.store[key]
        elif len(self.store) == self.capacity:
            self.store.popitem(last=False)
        self.store[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    test_cases = [
         (([('put', (1, 1)), ('put', (1, 1)), ('get', 1), ('put', (3, 3)), ('get', 2), ('put', (4, 4)), ('get', 1), ('get', 3), ('get', 4)], 2), [None, None, 1, None, -1, None, -1, 3, 4]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        obj = LRUCache(test_case[0][1])
        # obj = LRUCache_OrderedDict(test_case[0][1])
        for op_pair, output in zip(test_case[0][0], test_case[1]):
            op, params = op_pair
            if op == 'put':
                obj.put(*params)
            elif op == 'get':
                assert obj.get(params) == output


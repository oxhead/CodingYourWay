"""
https://leetcode.com/problems/implement-queue-using-stacks

Related:
  - lt_225_implement-stack-using-queues
"""

"""
Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

Notes:

    You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
    You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""

import collections

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = collections.deque()
        self.s2 = collections.deque()
        
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        # Time: O(1)
        # Space: O(1)
        self.s1.append(x)
        
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # Time: O(1), amortized
        # Space: O(n)
        self.peek()
        return self.s2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        # Time: O(1), amortized
        # Space: O(n)
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        # Time: O(1)
        # Space: O(1)
        return not self.s1 and not self.s2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__ == '__main__':
    test_cases = [
        ([('push', 1), ('peek', None), ('empty', None), ('pop', None)], [None, 1, False, 1]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        obj = MyQueue()
        for op_pair, expected_output in zip(*test_case):
            op, val = op_pair
            if op == 'push':
                obj.push(val)
            elif op == 'peek':
                assert obj.peek() == expected_output
            elif op == 'empty':
                assert obj.empty() == expected_output
            elif op == 'pop':
                assert obj.pop() == expected_output

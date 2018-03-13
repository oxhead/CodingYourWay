"""
https://leetcode.com/problems/max-stack

Related:
  - lt_155_min-stack
"""

"""
Design a max stack that supports push, pop, top, peekMax and popMax.

    push(x) -- Push element x onto stack.
    pop() -- Remove the element on top of the stack and return it.
    top() -- Get the element on the top.
    peekMax() -- Retrieve the maximum element in the stack.
    popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

Example 1:

MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5

Note:

    -1e7 <= x <= 1e7
    Number of operations won't exceed 10000.
    The last four operations won't be called when stack is empty.
"""

from collections import defaultdict

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMax = self.peekMax()
        if curMax == None or x > curMax:
            curMax = x
        self.q.append([x, curMax])

    def pop(self):
        """
        :rtype: int
        """
        return self.q.pop()[0]


    def top(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        return self.q[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        return self.q[-1][1]

    def popMax(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        maxN = self.q[-1][1]
        for i in range(len(self.q) - 1, -1, -1):
            if self.q[i][0] == maxN: 
                self.q.pop(i)
                for j in range(i, len(self.q)):
                    self.q[j][1] = max(self.q[j-1][1], self.q[j][0]) if j >= 1 else self.q[j][0]
                break
        
        return maxN

class MaxStack_failed:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_stack = []
        

    def _print(self):
        print('s1:', self.stack)
        print('s2:', self.max_stack)


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.max_stack or x > self.max_stack[-1]:
            self.max_stack.append(x)
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.max_stack and self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        x = self.stack.pop()
        return x

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def peekMax(self):
        """
        :rtype: int
        """
        return self.max_stack[-1]
        

    def popMax(self):
        """
        :rtype: int
        """
        print('before-------------')
        self._print()
        max_value = self.max_stack[-1]
        tmp_stack = []
        while self.stack[-1] != self.max_stack[-1]:
            tmp_stack.append(self.stack.pop())
        self.stack.pop()
        self.max_stack.pop()
        tmp_max = float('-inf')
        while tmp_stack:
            tmp_max = max(tmp_max, tmp_stack[-1])
            self.stack.append(tmp_stack.pop())
        if not self.max_stack or tmp_max >= self.max_stack[-1]:
            if self.stack:
                self.max_stack.append(tmp_max)
        print('after=============')
        self._print()
        return max_value

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

if __name__ == '__main__':
    test_cases = [
        ([('push', 5), ('push', 1), ('push', 5), ('top',), ('popMax',), ('top',), ('peekMak',), ('pop',), ('top',)], [None, None, None, 5, 5, 1, 5, 1, 5]),
        ([('push', 5), ('push', 1), ('push', -5), ('popMax',), ('popMax',), ('top',)], [None, None, None, 5, 1, -5]),
        ([('push', -23), ('peekMax',), ('push', -74), ('popMax',), ('push', -4), ('push', 20), ('push', 68), ('top',), ('push', 83), ('peekMax',), ('push', 73), ('popMax',), ('peekMax',)], [None, -23, None, -23, None, None, None, 68, None, 83, None, 83, 73]),
        ([('push', 79), ('pop',), ('push', 14), ('push', 67), ('push', 19), ('push', -92), ('popMax',), ('push', 77), ('pop',), ('push', 54), ('push', 5), ('peekMax',), ('popMax',), ('push', 12)], [None, 79, None, None, None, None, 67, None, 77, None, None, 54, 54, None]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        stack = MaxStack()
        for op_pair, expected_result in zip(test_case[0], test_case[1]):
            print(op_pair, expected_result)
            op = op_pair[0]
            if op == 'push':
                stack.push(op_pair[1])
            elif op == 'pop':
                assert stack.pop() == expected_result
            elif op == 'top':
                assert stack.top() == expected_result
            elif op == 'peekMax':
                assert stack.peekMax() == expected_result
            elif op == 'popMax':
                assert stack.popMax() == expected_result

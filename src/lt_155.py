"""
https://leetcode.com/problems/min-stack

Related:
  - lt_239
  - lt_716

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_value = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(self.min_value)
        self.stack.append(x)
        if self.min_value  == None or x < self.min_value: self.min_value = x
        
    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) < 1:
            raise IndexError('pop from empty stack')
        n = self.stack.pop()
        n_min = self.stack.pop()
        self.min_value = n_min
        return n

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) < 1:
            raise IndexError('top from empty stack')
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) < 1:
            raise IndexError('getMin from empty stack')
        return self.min_value
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    test_cases = [
        ([('push', 1), ('top',), ('min',), ('pop',)], [None, 1, 1, 1]),
        ([('push', 2), ('min',), ('push', 3), ('min',), ('push', 1)], [None, 2, None, 2, None, 1]),
        ([('push', 0), ('push', 1), ('push', 0), ('min',), ('pop',), ('min',)], [None, None, None, 0, 0, 0]),
        ([('push', 2), ('push', 0), ('push', 3), ('push', 0), ('min',), ('pop',), ('min',), ('pop',), ('min',), ('pop',), ('min',)], [None, None, None, None, 0, 0, 0, 3, 0, 0, 2]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        stack = MinStack()
        for op_pair, expected_result in zip(test_case[0], test_case[1]):
            print(op_pair, expected_result)
            print('#', stack.stack, stack.min_value)
            op = op_pair[0]
            if op == 'push':
                stack.push(op_pair[1])
            elif op == 'pop':
                assert stack.pop() == expected_result
            elif op == 'top':
                assert stack.top() == expected_result
            elif op == 'min':
                assert stack.getMin() == expected_result

"""
https://leetcode.com/problems/flatten-nested-list-iterator
Related:
  - lt_251
  - lt_281
  - lt_385
  - lt_565

Complexity:
  - Time:
  - Space:
"""

"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
"""

from utils import to_nested_list

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = list(reversed(nestedList))

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger(): return True
            top = self.stack.pop()
            for n in reversed(top.getList()):
                self.stack.append(n)
        return False

class NestedIterator_flatten(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def flatten(n):
            if n.isInteger():
                self.data.append(n.getInteger())
            else:
                for ni in n.getList():
                    flatten(ni) 
        self.data = []
        self.index = 0
        for n in nestedList:
            flatten(n)

    def next(self):
        """
        :rtype: int
        """
        n = self.data[self.index]
        self.index += 1
        return n
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.data)
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

if __name__ == '__main__':
    test_cases = [
        ([[]], []),
        ([[[[[[]]]]]], []),
        ([[1, 1], 2, [1, 1]], [1, 1, 2, 1, 1]),
        ([1, [4, [6]]], [1, 4, 6]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        nestedList = to_nested_list(test_case[0])
        i, v = NestedIterator(nestedList), []
        while i.hasNext(): v.append(i.next())
        print('output:', v)
        assert v == test_case[1]


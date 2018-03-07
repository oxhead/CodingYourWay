"""
https://leetcode.com/problems/peeking-iterator

Related:
  - lt_173_binary-search-tree-iterator
  - lt_251_flatten-2d-vector
  - lt_281_zigzag-iterator
"""

"""
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

Call next() gets you 1, the first element in the list.

Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.

Follow up: How would you extend your design to be generic and work with all types, not just integer?
"""

# Below is the interface for Iterator, which is already defined for you.
#
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.index = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        if self.nums: return self.index < len(self.nums)
        return False

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        n = self.nums[self.index]
        self.index += 1
        return n

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.top = None
        self.poped = False
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.poped:
            self.top = self.iterator.next()
            self.poped = True
        return self.top

    def next(self):
        """
        :rtype: int
        """
        if self.poped:
            self.poped = False
            return self.top
        return self.iterator.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.poped else self.iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ]


    for test_case in test_cases:
        print('case:', test_case)
        iter = PeekingIterator(Iterator(test_case[0]))
        output = []
        while iter.hasNext():
            val = iter.peek()
            assert val == iter.next()
            output.append(val)
        print('output:', output)
        assert output == test_case[1]


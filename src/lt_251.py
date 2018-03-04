"""
https://leetcode.com/problems/flatten-2d-vector

Related:
  - lt_173
  - lt_281
  - lt_284
  - lt_341

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

Follow up:
As an added challenge, try to code it using only iterators in C++ or iterators in Java. 
"""

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        def generator():
            for vec in vec2d:
                for n in vec:
                    yield n
        self.data = generator()
        self.n = sum([len(vec) for vec in vec2d])

    def next(self):
        """
        :rtype: int
        """
        self.n -= 1
        return next(self.data)


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.n > 0



class Vector2D_queue(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.queue = []

    def next(self):
        """
        :rtype: int
        """
        return self.queue.pop(0)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.queue or self.vec2d:
            if self.queue:
                return True
            elif self.vec2d:
                self.queue.extend(self.vec2d.pop(0))
            else:
                return False

class Vector2D_deque(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        from collections import deque
        self.data = deque()
        for vec in vec2d:
            self.data.extend(vec)

    def next(self):
        """
        :rtype: int
        """
        return self.data.popleft()


    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.data) > 0
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

if __name__ == '__main__':
    test_cases = [
        ([[1, 2], [3], [4, 5, 6]], [1, 2, 3, 4, 5, 6]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        i, v = Vector2D(test_case[0]), []
        while i.hasNext(): v.append(i.next())
        print('output:', v)
        assert v == test_case[1]


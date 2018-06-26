"""
https://leetcode.com/problems/nested-list-weight-sum

Related:
  - lt_364_nested-list-weight-sum-ii
  - lt_565_array-nesting
  - lt_690_employee-importance
"""

"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

Example 2:
Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27) 
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        self.value = value
        self.data = [] if self.value is None else None

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return self.value is not None

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        self.data.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.value = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self.value

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self.data if self.value is None else None


class Solution:
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def count_sum(nestedList, depth):
            total = 0
            for sub_list in nestedList:
                if sub_list.isInteger(): total += sub_list.getInteger() * depth
                else: total += count_sum(sub_list.getList(), depth + 1)
            return total
        return count_sum(nestedList, 1)
        

if __name__ == '__main__':
    test_cases = [
        ([[1,1],2,[1,1]], 10),
        ([1,[4,[6]]], 27),
    ]

    def create_list(n):
        if type(n) is list:
            integer_list = NestedInteger()
            for x in n: integer_list.add(create_list(x))
            return integer_list
        else:
            return NestedInteger(value=n)

    for test_case in test_cases:
        print('case:', test_case)
        nestedList = [create_list(n) for n in test_case[0]]
        output = Solution().depthSum(nestedList)
        print('output:', output)
        assert output == test_case[1]


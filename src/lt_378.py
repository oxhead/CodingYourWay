"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

Related:
  - lt_668 (kth-smallest-number-in-multiplication-table)
  - lt_407 (find-k-th-smallest-pair-distance)
  - lt_379 (find-k-pairs-with-smallest-sums)

Complexity:
  - Time:
  - Space:
"""

"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""

import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def search_counts(matrix, n, target):
            i, j = n - 1, 0
            count = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= target:
                    j += 1
                    count += i + 1
                else:
                    i -= 1
            return count
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) >> 1
            count = search_counts(matrix, n, mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left
            
        
    def kthSmallest_binarysearch_1(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # https://www.hrwhisper.me/leetcode-kth-smallest-element-sorted-matrix/
        def binary_search(row, n, target):
            left, right = 0, n
            while left < right:
                mid = (left + right) >> 1
                if row[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) >> 1
            count = sum([binary_search(row , n, mid) for row in matrix])
            if count < k: left = mid + 1
            else: right = mid
        return left

    def kthSmallest_heap(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # https://github.com/algorhythms/LeetCode/blob/master/378%20Kth%20Smallest%20Element%20in%20a%20Sorted%20Matrix.py
        class Node:
            def __init__(self, i, j):
                self.i = i
                self.j = j
            def __lt__(self, other):
                return matrix[self.i][self.j] < matrix[other.i][other.j]
            def hasnext(self):
                return self.j + 1 < len(matrix)
            def next(self):
                return Node(self.i, self.j + 1)
        heap = []
        for i in range(len(matrix)):
            heapq.heappush(heap, Node(i, 0))
        target = None
        for _ in range(k):
            target = heapq.heappop(heap)
            if target.hasnext():
                heapq.heappush(heap, target.next())
        return matrix[target.i][target.j]

if __name__ == '__main__':
    test_cases = [
        (([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8), 13),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().kthSmallest(*test_case[0])
        #output = Solution().kthSmallest_binarysearch_1(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


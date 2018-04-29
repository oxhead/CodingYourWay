"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

Related:
  - lt_379_find-k-pairs-with-smallest-sums
  - lt_407_find-k-th-smallest-pair-distance
  - lt_668_kth-smallest-number-in-multiplication-table
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

    def kthSmallest_heap_slow(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        count = 0
        for row in matrix:
            for n in row:
                heapq.heappush(heap, n)
        while count < k - 1:
            val = heapq.heappop(heap)
            count += 1
        return heap[0]

    def kthSmallest_heap_clean(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in range(len(matrix)):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        for _ in range(k):
            n, i, j = heapq.heappop(heap)
            if j < len(matrix[i]) - 1:
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return n

    def kthSmallest_binarysearch_v2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        left, right = matrix[0][0], matrix[m-1][n-1]
        while left < right:
            mid = left + (right - left) // 2
            count = 0
            j = n - 1
            for i in range(m):
                while j >= 0 and matrix[i][j] > mid: j -= 1
                count += (j + 1) 
            if count < k: left = mid + 1
            else: right = mid
        return left

    def kthSmallest_sort(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        nums = []
        for row in matrix:
            nums.extend(row)
        nums.sort()
        return nums[k-1]
 

if __name__ == '__main__':
    test_cases = [
        (([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8), 13),
        (([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5), 5),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().kthSmallest(*test_case[0])
        #output = Solution().kthSmallest_binarysearch_1(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/kth-largest-element-in-an-array

Related:
  - lt_324_wiggle-sort-ii
  - lt_347_top-k-frequent-elements
  - lt_414_third-maximum-number
"""

"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest_quickselect(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # https://aaronice.gitbooks.io/lintcode/content/data_structure/kth_largest_element.html

        def select(left, right, k):
            if left == right: return nums[left]
            pivot_index = partition(left, right)
            if pivot_index == k: return nums[pivot_index]
            elif pivot_index < k: return select(pivot_index + 1, right, k)
            else: return select(left, pivot_index - 1, k)

        def partition(left, right):
            pivot = nums[left]
            while left < right:
                while left < right and nums[right] >= pivot: right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= pivot: left += 1
                nums[right] = nums[left]
            nums[left] = pivot
            return left

        if not nums or len(nums) == 0 or k <= 0 or k > len(nums): return -1
        return select(0, len(nums) - 1, len(nums) - k)

    def findKthLargest_naive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # time limit exceeded
        for i in range(len(nums)-1, 0, -1):
            for j in range(i):
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j] 
        return nums[len(nums) - k]

    def findKthLargest_heap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for n in nums:
            if len(heap) < (len(nums) - k + 1): heapq.heappush(heap, -n)
            else:
                if n < -heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, -n) 
        return -heap[0]


if __name__ == '__main__':
    test_cases = [
        (([3, 2, 1, 5, 6, 4], 2), 5),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findKthLargest(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


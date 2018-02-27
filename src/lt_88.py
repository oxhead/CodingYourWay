"""
https://leetcode.com/problems/merge-sorted-array

Related:
  - lt_21

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index_m = m - 1
        index_n = n - 1
        while index_m >= 0 and index_n >= 0:
            if nums1[index_m] >= nums2[index_n]:
                nums1[index_m + index_n + 1] = nums1[index_m]
                index_m -= 1
            else:
                nums1[index_m + index_n + 1] = nums2[index_n]
                index_n -= 1
        while index_n >= 0:
            nums1[index_m + index_n + 1] = nums2[index_n]
            index_n -= 1


if __name__ == '__main__':
    test_cases = [
        (([], 0, [], 0), []),
        (([1], 1, [2], 1), [1, 2]),
        (([1, 2], 2, [3, 4], 2), [1, 2, 3, 4]),
        (([3, 4], 2, [1, 2], 2), [1, 2, 3, 4]),
        (([1, 3], 2, [2, 4], 2), [1, 2, 3, 4]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        input1 = [d for d in test_case[0][0]]
        input1 = input1 + [None] * test_case[0][1]
        input2 = [d for d in test_case[0][2]]
        input2 = input2 + [None] * test_case[0][3]
        Solution().merge(input1, test_case[0][1], input2, test_case[0][3])
        print('output:', input1)
        assert input1 == test_case[1]


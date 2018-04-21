"""
https://leetcode.com/problems/intersection-of-two-arrays

Related:
  - lt_350_intersection-of-two-arrays-ii
"""

"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:

    Each element in the result must be unique.
    The result can be in any order.

"""

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = set()
        for n in nums1:
            if n in nums2:
                output.add(n)
        return list(output)


if __name__ == '__main__':
    test_cases = [
        (([1, 2, 2, 1], [2, 2]), [2]),
        (([1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2]), []),
        (([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), [1]),
        (([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().intersection(*test_case[0])
        print('output:', output)
        assert sorted(output) == test_case[1]


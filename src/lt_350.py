"""
https://leetcode.com/problems/intersection-of-two-arrays-ii

Related:
  - lt_349

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:

    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:

    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        output = []
        for i, n1 in enumerate(nums1):
            for j, n2 in enumerate(nums2):
                if n2 == n1:
                    nums2[j] = None
                    output.append(n2)
                    break
        return output

        

if __name__ == '__main__':
    test_cases = [
        (([1, 2, 2, 1], [2, 2]), [2, 2]),
        (([1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2]), []),
        (([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), [1, 1, 1, 1, 1]),
        (([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().intersect(*test_case[0])
        print('output:', output)
        assert sorted(output) == test_case[1]


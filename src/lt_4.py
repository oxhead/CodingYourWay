"""
https://leetcode.com/problems/median-of-two-sorted-arrays

Related:
"""

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

import heapq

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Time: O(log(m+n))
        # Space: O(1)
        # https://github.com/algorhythms/LeetCode/blob/master/002%20Median%20of%20Two%20Sorted%20Arrays.py
        # http://fisherlei.blogspot.com/2012/12/leetcode-median-of-two-sorted-arrays.html
        # http://hankerzheng.com/blog/LeetCode-Median-of-Two-Sorted-Arrays
        # A: A0, A1, ..., Am/2, Am/2+1, ..., Am-2, Am-1
        # B: B0, B1, ..., Bn/2, Bn/2+1, ...m Bn-2, Bn-2 
        # Simplified:
        # A: A1 A2
        # B: B1 B2
        def find_kth(nums1, nums2, k):
            if not nums1: return nums2[k]
            if not nums2: return nums1[k]
            if k == 0: return min(nums1[0], nums2[0])
            m, n = len(nums1), len(nums2)
            if nums1[m//2] >= nums2[n//2]:
                print('A)', nums1)
                print('B)', nums2)
                print('k:', k)
                # need to discard unnecessary elements
                if k > m//2 + n//2:
                    # discard B1 
                    print('discard B1:', nums2, nums2[n//2+1:], k, k-n//2-1)
                    return find_kth(nums1, nums2[n//2+1:], k-n//2-1)
                else:
                    # discard A2
                    print('discard A2:', nums1, nums1[:m//2])
                    return find_kth(nums1[:m//2], nums2, k)
            else:
                # make sure Am/2 always > Bn/2
                print('switch)')
                return find_kth(nums2, nums1, k)
              
        m, n = len(nums1), len(nums2)
        if (m + n) & 1:
            print('case 1')
            return find_kth(nums1, nums2, (m + n) >> 1)
        else:
            print('case 2')
            return (find_kth(nums1, nums2, (m + n - 1) >> 1) + find_kth(nums1, nums2, (m + n) >> 1)) / 2 

    def findMedianSortedArrays_naive(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Time: O(m + n)
        # Space: O(1)
        m, n = len(nums1), len(nums2)
        k = (m + n) // 2 + 1 if (m + n) % 2 != 0 else ((m + n) // 2, (m + n) // 2 + 1)
        heap = []
        i1 = i2 = 0
        count = 0
        previous = None
        while i1 < len(nums1) or i2 < len(nums2):
            if i1 < len(nums1) and i2 < len(nums2):
                if nums1[i1] <= nums2[i2]:
                    heapq.heappush(heap, nums1[i1])
                    i1 += 1
                else:
                    heapq.heappush(heap, nums2[i2])
                    i2 += 1
            else:
                if i1 < len(nums1):
                    heapq.heappush(heap, nums1[i1])
                    i1 += 1
                else:
                    heapq.heappush(heap, nums2[i2])
                    i2 += 1
            current = heapq.heappop(heap)
            count += 1
            if type(k) is int and count == k: return current
            elif type(k) is tuple and count == k[-1]:
                return (previous + current) / 2 
            previous = current

if __name__ == '__main__':
    test_cases = [
        # (([1], []), 1),
        # (([1, 3], [2]), 2.0),
        # (([1, 2], [3, 4]), 2.5),
        (([1, 2, 3], [4, 5, 6]), 3.5),
        #(([1, 3, 5, 7, 9], [2, 4, 6, 8]), 5),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findMedianSortedArrays(*test_case[0])
        print('output:', output)
        assert abs(output - test_case[1]) < 0.0000001


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
        # Time: O(log(min(m, n)))
        # Space: O(1)
        # https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2496/Concise-JAVA-solution-based-on-Binary-Search
        def get_kth(num1, start1, nums2, start2, k):
            if start1 >= len(nums1): return nums2[start2 + k - 1]
            if start2 >= len(nums2): return nums1[start1 + k - 1]
            if k == 1: return min(nums1[start1], nums2[start2])
            mid1, mid2 = float('inf'), float('inf')
            if start1 + k // 2 - 1 < len(nums1): mid1 = nums1[start1 + k // 2 - 1]
            if start2 + k // 2 - 1 < len(nums2): mid2 = nums2[start2 + k // 2 - 1]
            if mid1 < mid2:
                return get_kth(nums1, start1 + k//2, nums2, start2, k - k//2)
            else:
                return get_kth(nums1, start1, nums2, start2 + k//2, k - k//2)
        m, n = len(nums1), len(nums2)
        k1 = (m + n + 1) // 2
        k2 = (m + n + 2) // 2
        if k1 == k2:
            return get_kth(nums1, 0, nums2, 0, k1)
        else:
            return (get_kth(nums1, 0, nums2, 0, k1) + get_kth(nums1, 0, nums2, 0, k2)) / 2

    def findMedianSortedArrays_v2(self, nums1, nums2):
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

    def findMedianSortedArrays_heap(self, nums1, nums2):
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

    def findMedianSortedArrays_failed(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        k = (len(nums1) + len(nums2) + 1) // 2 - 1
        count = 0
        left1, right1, left2, right2 = 0, len(nums1) - 1, 0, len(nums2) - 1
        print('k={}'.format(k))
        while count < k and left1 <= right1 and left2 <= right2:
            mid1 = left1 + (right1 - left1) // 2
            mid2 = left2 + (right2 - left2) // 2
            if nums1[mid1] <= nums2[mid2]:
                count += right2 - mid2
                right2 = mid2
            else:
                count += right1 - mid1
                right1 = mid1
        if right1 == -1:
            return 
        print(right1, right2)
        return (nums1[right1] + nums2[right2]) / 2 


if __name__ == '__main__':
    test_cases = [
        (([1], []), 1),
        (([1, 3], [2]), 2.0),
        (([1, 2], [3, 4]), 2.5),
        (([1, 2, 3], [4, 5, 6]), 3.5),
        (([1, 3, 5, 7, 9], [2, 4, 6, 8]), 5),
        (([1], [2, 3, 4, 5, 6]), 3.5),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findMedianSortedArrays(*test_case[0])
        print('output:', output)
        assert abs(output - test_case[1]) < 0.0000001


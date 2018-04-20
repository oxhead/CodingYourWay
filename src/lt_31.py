"""
https://leetcode.com/problems/next-permutation

Related:
  - lt_46_permutations
  - lt_47_permutations-ii
  - lt_60_permutation-sequence
  - lt_267_palindrome-permutation-ii
"""

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Time: O(n)
        # Space: O(1)
        # http://fisherlei.blogspot.sg/2012/12/leetcode-next-permutation.html
        # Example: [6, 8, 7, 4, 3, 2]
        # 0 1 2 3 4 5 (index)
        # 6 8 7 4 3 2 (nums)
        # 0           (m)
        #     2       (n)
        # 7 8 6 4 3 2 (swap nums[m] and nums[n])
        # 7 2 3 4 6 8 (reverse slice)
        m = n = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                m = i
                break
        if m == -1:
            nums.reverse()
            return
        for i in range(len(nums)-1, m, -1):
            if nums[i] > nums[m]:
                n = i
                break
        nums[m], nums[n] = nums[n], nums[m]
        # reverse the slice
        nums[m+1:] = nums[:m:-1]

    def nextPermutation_verbose(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Time: O(n)
        # Space: O(1)
        # http://fisherlei.blogspot.sg/2012/12/leetcode-next-permutation.html
        index_partition = index_change = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                index_partition = i - 1
                break
        for i in range(len(nums) - 1, index_partition, -1):
            if nums[i] > nums[index_partition]:
                index_change = i
                break
        if index_partition < 0:
            nums.sort()
            return
        nums[index_partition], nums[index_change] = nums[index_change], nums[index_partition]
        if index_partition < 0: return
        left = index_partition + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], [1, 3, 2]),
        ([1, 3, 2], [2, 1, 3]),
        ([2, 1, 3], [2, 3, 1]),
        ([2, 3, 1], [3, 1, 2]),
        ([3, 1, 2], [3, 2, 1]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([6, 8, 7, 4, 3, 2], [7, 2, 3, 4, 6, 8]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        nums = test_case[0]
        Solution().nextPermutation(nums)
        print('output:', nums)
        assert nums == test_case[1]


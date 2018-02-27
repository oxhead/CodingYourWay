"""
https://leetcode.com/problems/rotate-array

Related:
  - lt_61
  - lt_186

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II
"""

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # https://shenjie1993.gitbooks.io/leetcode-python/189%20Rotate%20Array.html

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        if not nums: return
        n = len(nums)
        k %= n
        reverse(nums, 0, n-k-1)
        reverse(nums, n-k, n-1)
        reverse(nums, 0, n-1)

    def rotate_naive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # space: O(1)
        # time: O(kn)
        if not nums: return
        for _ in range(k % len(nums)):
            n = nums[-1]
            for i in range(len(nums)-2, -1, -1):
                nums[i+1] = nums[i]
            nums[0] = n
                
    def rotate_extra_space(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # space: O(n)
        # time: O(n)
        if not nums: return
        k = k % len(nums)
        tmp = nums[-k:] + nums[:len(nums)-k+1] 
        for i in range(len(nums)):
            nums[i] = tmp[i]
        

if __name__ == '__main__':
    test_cases = [
        (([], 0), []),
        (([1], 0), [1]),
        (([1], 1), [1]),
        (([1, 2], 3), [2, 1]),
        (([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        nums, k = test_case[0]
        Solution().rotate(nums, k)
        print('output:', nums)
        assert nums == test_case[1]


"""
https://leetcode.com/problems/find-all-duplicates-in-an-array

Related:
  - lt_448_find-all-numbers-disappeared-in-an-array
"""

"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Time: O(n)
        # Space: O(1)
        output = []
        for n in nums:
            if nums[abs(n) - 1] < 0:
                output.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1
        return output
        
    def findDuplicates_failed(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] *= -1
        print(nums)
        return []

if __name__ == '__main__':
    test_cases = [
        ([4,3,2,7,8,2,3,1], [2, 3]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findDuplicates(test_case[0])
        print('output:', output)
        assert output == test_case[1]


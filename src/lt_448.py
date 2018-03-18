"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

Related:
  - lt_41_first-missing-positive
  - lt_442_find-all-duplicates-in-an-array
"""

"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Time: O(n)
        # Space: O(1)
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

if __name__ == '__main__':
    test_cases = [
        ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findDisappearedNumbers(test_case[0])
        print('output:', output)
        assert output == test_case[1]


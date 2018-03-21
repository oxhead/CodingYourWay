"""
https://leetcode.com/problems/patching-array

Related:
  - epi_
"""

"""
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.
"""

class Solution:
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        # Time: O(?)
        # Space: O(1)
        current_max = 1
        i = 0
        count = 0
        while current_max <= n:
            if i < len(nums) and nums[i] <= current_max:
                current_max += nums[i]
                i += 1
            else:
                current_max += current_max
                count += 1
        return count
        

if __name__ == '__main__':
    test_cases = [
        (([1, 3], 6), 1),
        (([1, 5, 10], 20), 2),
        (([1, 2, 2], 5), 0),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().minPatches(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


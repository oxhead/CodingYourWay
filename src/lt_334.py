"""
https://leetcode.com/problems/increasing-triplet-subsequence

Related:
  - lt_300

Complexity:
  - Time:
  - Space:
"""

"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false. 

Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
"""

class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min1 = min2 = 0x7FFFFFF
        for n in nums:
            if n < min1:
                min1 = n
            elif min1 < n < min2:
                min2 = n
            elif n > min2:
                return True
        return False

    def increasingTriplet_range(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # http://www.cnblogs.com/grandyang/p/5194599.html
        if not nums or len(nums) < 3: return False
        n = len(nums)
        forwards = [float('inf')] * n
        backwards = [float('-inf')] * n
        for i in range(1, n):
            forwards[i] = min(forwards[i-1], nums[i])
        for i in range(n-2, -1, -1):
            backwards[i] = max(backwards[i+1], nums[i])
        for i in range(n):
            if forwards[i] < nums[i] < backwards[i]:
                return True
        return False

if __name__ == '__main__':
    test_cases = [
       ([1, 2, 3, 4, 5], True),
       ([5, 4, 3, 2, 1], False),
       ([3, 2, 4, 2, 1, 7, 1], True),
       ([6, 5, 7, 1, 2, 8, 0], True,),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().increasingTriplet(test_case[0])
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/3sum-closest

Related:
  - lt_15_3sum
  - lt_259_3sum-smaller
"""

"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(1)
        nums.sort()
        best_val = float('inf')
        output = None
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                diff = total - target
                if abs(diff) < best_val:
                    best_val = abs(diff)
                    output = total

                if diff < 0:
                    left += 1
                elif diff > 0:
                    right -= 1
                else:
                    return target
        return output


if __name__ == '__main__':
    test_cases = [
        (([0,1,2], 3), 3),
        (([-1, 2, 1, -4], 1), 2),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().threeSumClosest(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


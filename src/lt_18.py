"""
https://leetcode.com/problems/4sum

Related:
  - lt_1_two-sum
  - lt_15_3sum
  - lt_454_4sum-ii
"""

"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Time: O(n^3)
        # Space: O(1)
        # https://www.tangjikai.com/algorithms/leetcode-18-4sum
        def k_sum(nums, target, k):
            if k == 2:
                left, right = 0, len(nums) - 1
                while left < right:
                    if left > 0 and nums[left] == nums[left - 1]:
                        left += 1
                        continue
                    if right < len(nums) - 1 and nums[right] == nums[right + 1]:
                        right -= 1
                        continue
                    if nums[left] + nums[right] == target:
                        yield (nums[left], nums[right])
                        left += 1
                    elif nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
            else:
                for left in range(len(nums) - k + 1):
                    # skip the same elements with previous
                    if left > 0 and nums[left] == nums[left - 1]:
                        continue
                    for sub in k_sum(nums[left+1:], target - nums[left], k - 1):
                        yield (nums[left],) + sub
        if not nums: return []
        nums.sort()
        return list(list(x) for x in k_sum(nums, target, 4))

    def fourSum_nestedloop(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                total = target - nums[i] - nums[j]
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == total:
                        output.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                    elif nums[left] + nums[right] < total:
                        left += 1
                    else:
                        right -= 1
        return output

    def fourSum_noyield(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def k_sum(left, right, target, k):
            if k == 2:
                output = []
                while left < right:
                    if nums[left] + nums[right] == target:
                        output.append([nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
                return output
            else:
                output = []
                for i in range(left, right - k + 1):
                    if i > left and nums[i] == nums[i-1]:
                        continue
                    for sub in k_sum(i + 1, right, target - nums[i], k - 1):
                        output.append([nums[i]] + sub)
                return output

        if not nums: return []
        nums.sort()
        return k_sum(0, len(nums) - 1, target, 4)
        
            
        

if __name__ == '__main__':
    test_cases = [
        (([1, 0, -1, 0, -2, 2], 0), [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().fourSum(*test_case[0])
        print('output:', output)
        assert sorted([sorted(x) for x in output]) == sorted([sorted(x) for x in test_case[1]])


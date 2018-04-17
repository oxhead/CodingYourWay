"""
https://leetcode.com/problems/3sum

Related:
  - lt_1_two-sum
  - lt_16_3sum-closest
  - lt_18_4sum
  - lt_259_3sum-smaller
"""

"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

import collections

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time: O(n^2)
        # Space: O(1)
        # https://blog.csdn.net/lisonglisonglisong/article/details/45848209
        def two_sum(left, right, target):
            while left < right:
                if nums[left] + nums[right] + target == 0:
                    output.append([target, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + target < 0:
                    left += 1
                else:
                    right -= 1
            
        output = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            two_sum(i + 1, len(nums) - 1, nums[i])
        return output
        
    def threeSum_failed(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        records = collections.defaultdict(set)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                records[-nums[i] - nums[j]].add(tuple(sorted([nums[i], nums[j]]))) 
        for k in range(len(nums)):
            if k in records:
                for s in records[k]:
                    output.append(list(s) + [nums[k]])
        return output

    def threeSum_failed2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3: return []
        nums.sort()
        output = []
        left, right = 0, len(nums) - 1
        while left < right:
            #import time
            #time.sleep(1)
            print('left={}, right={}'.format(left, right))
            i, j = left, right
            k = i + 1
            while i < k < j:
                print('i={}, k={}, j={}'.format(i, k, j))
                if nums[i] + nums[k] + nums[j] == 0:
                    output.append([nums[i], nums[k], nums[j]])
                    print('* found')
                    break
                elif nums[i] + nums[k] + nums[j] < 0:
                    k += 1
                else:
                    j -= 1
            left += 1
            #while left > 0 and nums[left] == nums[left - 1]:
            #    left += 1
            #while right < len(nums) - 1 and nums[right] == nums[right + 1]:
            #    right -= 1
        return output


if __name__ == '__main__':
    test_cases = [
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]]),
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().threeSum(test_case[0])
        print('output:', output)
        assert sorted(output) == sorted(test_case[1])


"""
https://leetcode.com/problems/delete-and-earn

Related:
  - lt_198_house-robber
"""

"""
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:

Input: nums = [3, 4, 2]
Output: 6
Explanation: 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.

Example 2:

Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation: 
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.

Note:
The length of nums is at most 20000.
Each element nums[i] is an integer in the range [1, 10000].
"""

class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n), where n = max(nums)
        # Space: O(n)
        # Hints:
        # 1) Reduce to the house rob problem
        if not nums: return 0
        max_n = max(nums)
        rewards = [0] * (max_n + 1)
        for n in nums:
            rewards[n] += n
        previous, current = 0, 0
        for i in range(1, len(rewards)):
            previous, current = current, max(previous + rewards[i], current) 
        return current


if __name__ == '__main__':
    test_cases = [
        ([], 0),
        ([1], 1),
        ([3, 4, 2], 6),
        ([2, 2, 3, 3, 3, 4], 9),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().deleteAndEarn(test_case[0])
        print('output:', output)
        assert output == test_case[1]


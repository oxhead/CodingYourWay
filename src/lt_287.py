"""
https://leetcode.com/problems/find-the-duplicate-number

Related:
  - lt_41_first-missing-positive
  - lt_136_single-number
  - lt_142_linked-list-cycle-ii
  - lt_268_missing-number
  - lt_645_set-mismatch
"""

"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:

    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n^2).
    There is only one duplicate number in the array, but it could be repeated more than once.
"""

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        # https://en.wikipedia.org/wiki/Cycle_detection
        # https://github.com/algorhythms/LeetCode/blob/master/287%20Find%20the%20Duplicate%20Number.py
        # N = n + 1
        # x    = {0, 1, 2, 3, ..., n-1, n}
        # f(x) = {1, 2, 3, 4, ..., n, 1}
        # similar to detecting cycled linked list
        # linked list = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 1 -> 2
        # slow: 0 -> 1 -> 2 -> ...
        # fast: 0 -> 2 -> 4 -> ...
        
        # This is important. Moves first to avoid check in the loop.
        fast = nums[nums[0]]
        slow = nums[0]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        # This is important. Moves back to where both fast and slow starts.
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        # Return the value, but not nums[fast]
        return fast

    def findDuplicate_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        while (slow == fast == 0) or slow != fast:
             slow = nums[slow]
             fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
             slow = nums[slow]
             fast = nums[fast]
        return fast

    def findDuplicate_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        previous = nums[0]
        for n in nums[1:]:
            if n == previous: return n
            previous = n
        return -1

    def findDuplicate_set(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for n in nums:
            if n in s: return n
            else: s.add(n)
        return -1

    def findDuplicate_binarysearch(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            count = sum([n <= mid for n in nums])
            if count > mid: right = mid - 1
            else: left = mid + 1
        return left


if __name__ == '__main__':
    test_cases = [
        ([1, 1], 1),
        ([1, 2, 1], 1),
        ([1, 1, 1], 1),
        ([1, 2, 2, 3, 4, 5], 2),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findDuplicate(test_case[0])
        print('output:', output)
        assert output == test_case[1]


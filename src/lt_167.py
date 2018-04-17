"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

Related:
  - lt_1_two-sum
  - lt_653_two-sum-iv-input-is-a-bst
"""

"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2 
"""

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left + 1, right + 1]

    def twoSum_slow(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search(start, end, n):
            if start > end: return -1
            mid = (start + end) // 2
            records[target - numbers[mid]] = mid
            if numbers[mid] == n: return mid
            elif numbers[mid] > n: return binary_search(start, mid - 1, n)
            else: return binary_search(mid + 1, end, n)
        records = {}
        for i, n in enumerate(numbers):
            if n in records:
                return [i + 1, records[n] + 1]
            j = binary_search(i + 1, len(numbers) - 1, target - n)
            if j != -1:
                return [i + 1, j + 1]
        return []


if __name__ == '__main__':
    test_cases = [
        (([2, 7, 11, 15], 9), [1, 2]),
        (([5, 25, 75], 100), [2, 3]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().twoSum(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


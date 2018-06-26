"""
https://leetcode.com/contest/weekly-contest-87/problems/longest-mountain-in-array/
"""

"""
845. Longest Mountain in Array

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Medium

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

    B.length >= 3
    There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

 

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.

"""

class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = [0] * len(A)
        right = [0] * len(A)
        for i in range(len(A)):
            if i > 0 and A[i] > A[i-1]: left[i] = left[i-1] + 1
        for j in range(len(A) - 1, -1, -1):
            if j < len(A) - 1 and A[j] > A[j+1]: right[j] = right[j+1] + 1
        longest = 0
        for i in range(len(A)):
            if left[i] > 0 and right[i] > 0: longest = max(longest, left[i] + right[i] + 1)
        return longest


if __name__ == '__main__':
    test_cases = [
        ([2,1,4,7,3,2,5], 5),
        ([2,2,2], 0),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().longestMountain(test_case[0])
        print('output:', output)
        assert output == test_case[1]

"""
https://leetcode.com/problems/4sum-ii

Related:
  - lt_18

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""

class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = 0
        records = {}
        for i in A:
            for j in B:
                k = i + j
                if k not in records:
                    records[k] = 0
                records[k] += 1
        for i in C:
            for j in D:
                k = i + j
                if -k in records:
                    count += records[-k]
        return count

if __name__ == '__main__':
    test_cases = [
        (([1, 2], [-2, -1], [-1, 2], [0, 2]), 2),
        (([-1, -1], [-1, 1], [-1, 1], [1, -1]), 6),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().fourSumCount(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


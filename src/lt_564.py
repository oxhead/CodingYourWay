"""
https://leetcode.com/problems/find-the-closest-palindrome

Related:
"""

"""
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:

Input: "123"
Output: "121"

Note:

    The input n is a positive integer represented by string, whose length will not exceed 18.
    If there is a tie, return the smaller one as answer.
"""

class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        # Time: O(l)
        # Space: O(l)
        # https://leetcode.com/problems/find-the-closest-palindrome/discuss/102391/Python-Simple-with-Explanation
        # Hints:
        # 1) l = len(n)
        # 2) Worst cases: 10 ** l + 1 or 10 ** (l-1) - 1 
        # 3) Three possible cases: prefix = "12345"[:3] = "123"
        #    A. 122xx
        #    B. 123xx
        #    C. 123xx
        # Examples:
        # 1)
        # n   candidates
        # 123 ([1001, 99])
        # 2)
        # prefix = 12
        # 3)
        # possible prefix = [11, 12, 13]
        # possible palindrome = [111, 121, 131]
        # 4) compare all the distances [99, 111, 121, 131, 1001]
        l = len(n)
        candidates = set((str(10 ** l + 1), str(10 ** (l-1) - 1)))
        prefix = int(n[:(l+1)//2])
        for i in map(str, (prefix - 1, prefix, prefix + 1)):
            # l % 2 == 0 (even length): prefix + prefix[::-1]
            # l % 2 == 0 (odd length) : prefix + prefix[:-1][::-1]
            candidates.add(i + [i, i[:-1]][l%2][::-1])
        candidates.discard(n)
        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))

if __name__ == '__main__':
    test_cases = [
        ("123", "121"),
        ("100", "99"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().nearestPalindromic(test_case[0])
        print('output:', output)
        assert output == test_case[1]


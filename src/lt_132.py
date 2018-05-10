"""
https://leetcode.com/problems/palindrome-partitioning-ii

Related:
  - lt_131_palindrome-partitioning
"""

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(n)
        # https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42198/My-solution-does-not-need-a-table-for-palindrome-is-it-right-It-uses-only-O(n)-space.
        # Hints:
        # 1) cuts[i]: minimum cuts for s[:i+1]
        # 2) two center points for the odd and even substrings
        # Examples:
        # a a b
        # 0 1 2 (init)
        # 0 1 2 (i=0,0)
        # 0 0 2 (i=0,1) -> s[0:2] = aa needs zero cut
        # 0 0 2 (i=1,1)
        # 0 0 2 (i=1,2)
        # 0 0 1 (i=2,2) -> s[2:3] = b needs one cut (aab -> aa, b)
        # 0 0 1 (i=2,3)
        # e f e
        # 0 1 2 (init)
        # 0 1 2 (i=0,0)
        # 0 1 2 (i=0,1)
        # 0 1 0 (i=1,1) -> s[1:2] = f needs one cut (ef -> e, f), s[0:3] = efe needs zero cut
        # 0 1 0 (i=1,2)
        # 0 1 0 (i=2,2)
        # 0 1 0 (i=2,3)
        def search(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if left == 0: cuts[right] = 0
                else: cuts[right] = min(cuts[right], cuts[left - 1] + 1)
                left -= 1
                right += 1
        cuts = [x for x in range(len(s))]
        for i in range(len(s)):
            search(i, i)
            search(i, i + 1)
        return cuts[-1]

    def minCut_v2(self, s):
        """
        :type s: str
        :rtype: int
        """
        # https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42198/My-solution-does-not-need-a-table-for-palindrome-is-it-right-It-uses-only-O(n)-space.
        cut = [x for x in range(-1, len(s))]
        for i in range(1, len(s)):
            for left, right in [(i, i), (i-1, i)]:
                while left >=0 and right < len(s) and s[left] == s[right]:
                    cut[right + 1] = min(cut[right + 1], cut[left] + 1)
                    left -= 1
                    right += 1
        return cut[-1]

    def minCut_TLE(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time: O(n^3)
        # Space: O(n^2)
        dp = [[0] * len(s) for _ in range(len(s))]
        for size in range(len(s)):
            for i in range(len(s)):
                j = i + size 
                if j >= len(s): break
                elif i == j: continue
                elif j - i == 1:
                    if s[i] == s[j]: dp[i][j] = 0
                    else: dp[i][j] = 1
                else:
                    if s[i] == s[j] and dp[i+1][j-1] == 0: dp[i][j] = 0
                    else:
                        min_cut = float('inf')
                        for k in range(i, j):
                            min_cut = min(min_cut, 1 + dp[i][k] + dp[k+1][j])
                        dp[i][j] = min_cut
        return dp[0][-1]
                

if __name__ == '__main__':
    test_cases = [
        ("aab", 1),
        ("efe", 0),
        ("leet", 2),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().minCut(test_case[0])
        print('output:', output)
        assert output == test_case[1]


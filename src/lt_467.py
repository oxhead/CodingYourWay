"""
https://leetcode.com/problems/unique-substrings-in-wraparound-string

Related:
"""

"""
Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:

Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.

Example 2:

Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.

Example 3:

Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
"""

class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        # http://blog.jerkybible.com/2017/01/10/LeetCode-467-Unique-Substrings-in-Wraparound-String/
        max_length = 0
        count = 0
        dp = [0] * 26
        for i in range(len(p)):
            if i > 0 and ((ord(p[i]) - ord(p[i-1]) == 1) or (ord(p[i-1]) - ord(p[i]) == 25)): 
                max_length += 1
            else:
                max_length = 1
            dp[ord(p[i]) - ord('a')] = max(dp[ord(p[i]) - ord('a')], max_length)
        return sum(dp)


if __name__ == '__main__':
    test_cases = [
        ("a", 1),
        ("cac", 2),
        ("zab", 6),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findSubstringInWraproundString(test_case[0])
        print('output:', output)
        assert output == test_case[1]


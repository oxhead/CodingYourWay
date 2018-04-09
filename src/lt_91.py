"""
https://leetcode.com/problems/decode-ways

Related:
  - lt_639_decode-ways-ii
"""

"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        if not s or s[0] == "0": return 0
        dp1, dp2 = 0, 1
        for i in range(len(s)):
            current = 0
            if s[i] != '0':
                current = dp2
            if i > 0 and (10 <= int(s[i-1:i+1]) <= 26):
                current += dp1
            dp1, dp2 = dp2, current
        return dp2

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        # http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-91-decode-ways/
        def dp(index):
            if index in records: return records[index]
            if index >= len(s): return 1
            if s[index] == '0': return 0
            count = dp(index + 1)
            if index < len(s) - 1 and 10 <= int(s[index:index+2]) <= 26:
                count += dp(index + 2)
            records[index] = count
            return count
        if not s: return 0
        records = {}
        return dp(0)


if __name__ == '__main__':
    test_cases = [
        ("", 0),
        ("0", 0),
        ("01", 0),
        ("10", 1),
        ("12", 2),
        ("27", 1),
        ("101", 1),
        ("122", 3),
        ("1222", 5),
        ("1223", 5),
        ("138", 2),
        ("230", 0),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().numDecodings(test_case[0])
        print('output:', output)
        assert output == test_case[1]


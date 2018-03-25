"""
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters

Related:
  - lt_3_longest-substring-without-repeating-characters
  - lt_239_sliding-window-maximum
  - lt_340_longest-substring-with-at-most-k-distinct-characters
"""

"""
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3. 
"""

import collections

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        records = collections.OrderedDict()
        max_length = 0
        left = 0
        for i in range(len(s)):
            if len(records) <= 1 and s[i] not in records:
                records[s[i]] = 0
            if s[i] in records:
                records[s[i]] += 1
                max_length = max(max_length, sum(records.values()))
            else:
                records = {s[i-1]: i - left, s[i]: 1}
            if i > 0 and s[i] != s[i-1]:
                left = i
        return max_length

if __name__ == '__main__':
    test_cases = [
        ("c", 1),
        ("abcabcbb", 4),
        ("bbbbb", 5),
        ("pwwkew", 3),
        ("tmmzuxt", 3),
        ("eceba", 3),
        ("ccaabbb", 5),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().lengthOfLongestSubstringTwoDistinct(test_case[0])
        print('output:', output)
        assert output == test_case[1]


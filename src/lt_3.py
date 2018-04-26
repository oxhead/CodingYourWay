"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

Related:
  - lt_159_longest-substring-with-at-most-two-distinct-characters
"""

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        records = {}
        left, max_length = 0, 0
        for i, c in enumerate(s):
            # left represents the boundary of non-repeative characters
            # if left > records[s[i]], then records[s[i]] should not be
            # considered as a valid character
            # because the max length is controlled by (i - left + 1 )
            if c in records and left <= records[c]:
                left = records[c] + 1
            else:
                max_length = max(max_length, i - left + 1)
            records[c] = i
        return max_length

    def lengthOfLongestSubstring_naive(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(1)
        if not s: return 0
        max_length = 1
        for i in range(1, len(s)):
            j = i
            records = set()
            while j >= 0:
                if s[j] in records: break
                records.add(s[j])
                j -= 1
            max_length = max(max_length, i - j)
        return max_length


if __name__ == '__main__':
    test_cases = [
        ("c", 1),
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("tmmzuxt", 5),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().lengthOfLongestSubstring(test_case[0])
        print('output:', output)
        assert output == test_case[1]


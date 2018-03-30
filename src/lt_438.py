"""
https://leetcode.com/problems/find-all-anagrams-in-a-string

Related:
  - lt_242_valid-anagram
  - lt_567_permutation-in-string
"""

"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

import collections

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Time: O(n)
        # Space: O(1)
        if not s or not p or len(p) > len(s): return []
        counter_s = collections.Counter(s[:len(p)-1])
        counter_p = collections.Counter(p)
        output = []
        for i in range(len(s) - len(p) + 1):
            counter_s[s[i+len(p)-1]] += 1
            if counter_s == counter_p:
                output.append(i)
            counter_s[s[i]] -= 1
            if counter_s[s[i]] == 0: counter_s.pop(s[i])
        return output


if __name__ == '__main__':
    test_cases = [
        (("cbaebabacd", "abc"), [0, 6]),
        (("abab", "ab"), [0, 1, 2]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findAnagrams(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


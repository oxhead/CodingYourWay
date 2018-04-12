"""
https://leetcode.com/problems/isomorphic-strings

Related:
  - lt_290_word-pattern
"""

"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Time: O(n)
        # Spac: O(n)
        # https://github.com/kamyu104/LeetCode/blob/master/Python/isomorphic-strings.py
        s2t, t2s = {}, {}
        for c1, c2 in zip(s, t):
            if c2 not in s2t and c1 not in t2s:
                s2t[c2] = c1
                t2s[c1] = c2
            elif c2 not in s2t or s2t[c2] != c1:
                return False
        return True

    def isIsomorphic_oneliner(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s, t))) == len(set(s)) and len(set(zip(s, t))) == len(set(t))


if __name__ == '__main__':
    test_cases = [
        (("ab", "aa"), False),
        (("egg", "add"), True),
        (("foo", "bar"), False),
        (("paper", "title"), True),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isIsomorphic(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/valid-anagram

Related:
  - lt_49
  - lt_266
  - lt_438

Complexity:
  - Time: O(n)
  - Space: O(n)
"""

"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
    You may assume the string contains only lowercase alphabets.

    Follow up:
        What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

from collections import defaultdict

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        for c in t:
            counter[c] -= 1
        for c, count in counter.items():
            if count != 0: return False
        return True

    def isAnagram2(self, s, t):
        return all([s.count(c) == t.count(c) for c in [chr(c) for c in range(ord('a'), ord('z')+1)]])

if __name__ == '__main__':
    test_cases = [
        (("anagram", "nagaram"), True),
        (("rat", "car"), False),
        (("anagram", "anagra"), False)
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isAnagram(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


"""
https://leetcode.com/problems/first-unique-character-in-a-string

Related:
  - lt_451

Complexity:
  - Time: O(n)
  - Space: O(n)
"""

"""
 Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

 Examples:

     s = "leetcode"
     return 0.

 s = "loveleetcode",
 return 2.
"""

import collections

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1


if __name__ == '__main__':
    test_cases = [
        ("leetcode", 0),
        ("loveleetcode", 2)
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().firstUniqChar(test_case[0])
        print('output:', output)
        assert output == test_case[1]


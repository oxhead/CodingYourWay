"""
https://leetcode.com/problems/palindrome-permutation
https://leetcode.com/problems/palindrome-permutation-ii

Related:
  - lt_5_longest-palindromic-substring
  - lt_242_valid-anagram
  - lt_267_palindrome-permutation-ii
  - lt_409_longest-palindrome
"""

"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True. 
"""

import collections

class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        counter = collections.Counter(s)
        odd = 0
        for k, v in counter.items():
            if v % 2 != 0: odd += 1
        return odd <= 1

if __name__ == '__main__':
    test_cases = [
        ("aabb", True),
        ("abc", False),
        ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", True)
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().canPermutePalindrome(test_case[0])
        print('output:', output)
        assert output == test_case[1]


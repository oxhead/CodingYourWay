"""
https://leetcode.com/problems/longest-palindrome

Related:
  - lt_266_palindrome-permutation
"""

"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

import collections

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        # Hint: even number of characters with ONLY one odd number of character (can be duplicate)
        # Approaches:
        #  1) Hash Table (Counter)
        counter = collections.Counter(s)
        count = 0
        odd_count = False
        for k, v in counter.items():
            if v % 2 == 0:
                count += v
            else:
                count += v - 1
                odd_count = True
        return count + int(odd_count)


if __name__ == '__main__':
    test_cases = [
       ("abccccdd", 7), 
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().longestPalindrome(test_case[0])
        print('output:', output)
        assert output == test_case[1]


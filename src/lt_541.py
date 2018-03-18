"""
https://leetcode.com/problems/reverse-string-ii

Related:
  - lt_344_reverse-string
  - lt_345_reverse-vowels-of-a-string
"""

"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:

    The string consists of lower English letters only.
    Length of the given string and k will in the range [1, 10000]
"""

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)

    def reverseStr_verbose(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Time: O(n)
        # Space: O(1)
        def reverse(data, i, j):
            while i < j:
                data[i], data[j] = data[j], data[i]
                i += 1
                j -= 1
        data = list(s)
        start, end = 0, -1
        rounds = 0
        while start < len(s) - 1:
            start = rounds * k
            end = start + k - 1
            if end >= len(s):
                end = len(s) - 1
            reverse(data, start, end)
            rounds += 2
        return "".join(data)

if __name__ == '__main__':
    test_cases = [
        (("a", 1), "a"),
        (("ab", 1), "ab"),
        (("ab", 2), "ba"),
        (("abcde", 2), "bacde"),
        (("abcdefg", 2), "bacdfeg"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().reverseStr(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


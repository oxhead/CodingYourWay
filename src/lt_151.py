"""
https://leetcode.com/problems/reverse-words-in-a-string

Related:
  - lt_186_reverse-words-in-a-string-ii

"""

"""
 Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.
Clarification:

    What constitutes a word?
    A sequence of non-space characters constitutes a word.
    Could the input string contain leading or trailing spaces?
    Yes. However, your reversed string should not contain leading or trailing spaces.
    How about multiple spaces between two words?
    Reduce them to a single space in the reversed string.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(reversed(s.split()))

if __name__ == '__main__':
    test_cases = [
        ("the sky is blue", "blue is sky the"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().reverseWords(test_case[0])
        print('output:', output)
        assert output == test_case[1]

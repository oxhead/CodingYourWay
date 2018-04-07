"""
https://leetcode.com/problems/length-of-last-word

Related:
"""

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        output = s.split()
        return len(output[-1]) if len(output) > 0 else 0

    def lengthOfLastWord_verbose(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ': return count
            count += 1
        return count

if __name__ == '__main__':
    test_cases = [
        ("Hello World", 5),
        ("a ", 1),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().lengthOfLastWord(test_case[0])
        print('output:', output)
        assert output == test_case[1]


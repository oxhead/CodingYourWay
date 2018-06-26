"""
https://leetcode.com/contest/weekly-contest-87/problems/backspace-string-compare/
"""

"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

 

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

 

Note:

    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.
"""

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def process(s):
            stack = []
            for i in range(len(s)):
                if s[i] == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(s[i])
            return stack
        S = process(S)
        T = process(T)
        return S == T


if __name__ == '__main__':
    test_cases = [
        (("ab#c", "ad#c"), True),
        (("ab##", "c#d#"), True),
        (("a##c", "#a#c"), True),
        (("a#c", "b"), False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().backspaceCompare(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

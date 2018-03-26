"""
https://leetcode.com/problems/valid-number

Related:
  - lt_8_string-to-integer-atoi
"""

"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. 
"""


class InputType:
    INVALID    = 0
    SPACE      = 1
    SIGN       = 2
    DIGIT      = 3
    DOT        = 4
    EXPONENT   = 5

class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(1)
        # https://github.com/kamyu104/LeetCode/blob/master/Python/valid-number.py
        transition_table = [[-1,  0,  3,  1,  2, -1],     # next states for state 0
                            [-1,  8, -1,  1,  4,  5],     # next states for state 1
                            [-1, -1, -1,  4, -1, -1],     # next states for state 2
                            [-1, -1, -1,  1,  2, -1],     # next states for state 3
                            [-1,  8, -1,  4, -1,  5],     # next states for state 4
                            [-1, -1,  6,  7, -1, -1],     # next states for state 5
                            [-1, -1, -1,  7, -1, -1],     # next states for state 6
                            [-1,  8, -1,  7, -1, -1],     # next states for state 7
                            [-1,  8, -1, -1, -1, -1]]     # next states for state 8
        
        state = 0
        for char in s:
            inputType = InputType.INVALID
            if char.isspace():
                inputType = InputType.SPACE;
            elif char == '+' or char == '-':
                inputType = InputType.SIGN
            elif char.isdigit():
                inputType = InputType.DIGIT
            elif char == '.':
                inputType = InputType.DOT
            elif char == 'e' or char == 'E':
                inputType = InputType.EXPONENT;
                
            state = transition_table[state][inputType];
            
            if state == -1:
                return False;
        
        return state == 1 or state == 4 or state == 7 or state == 8 

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # https://github.com/kamyu104/LeetCode/blob/master/Python/valid-number.py
        import re
        return bool(re.match("^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$", s))


if __name__ == '__main__':
    test_cases = [
        ("0", True),
        ("0.1", True),
        ("abc", False),
        ("1 a", False),
        ("2e10", True),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isNumber(test_case[0])
        print('output:', output)
        assert output == test_case[1]


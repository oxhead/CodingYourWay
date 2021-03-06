"""
https://leetcode.com/problems/evaluate-reverse-polish-notation

Related:
  - lt_224_basic-calculator
  - lt_282_expression-add-operators
"""

"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

    Division between two integers should truncate toward zero.
    The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        stack = []
        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack.append(int(token))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if token == '+':
                    stack.append(n1 + n2)
                elif token == '-':
                    stack.append(n1 - n2)
                elif token == '*':
                    stack.append(n1 * n2)
                elif token == '/':
                    stack.append(int(n1 / n2))
        return stack[0]


if __name__ == '__main__':
    test_cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().evalRPN(test_case[0])
        print('output:', output)
        assert output == test_case[1]

"""
https://leetcode.com/problems/generate-parentheses

Related:
  - lt_17
  - lt_20

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(left, right, current, output):
            if left == 0 and right == 0:
                output.append(current)
                return
            if left > 0:
                generate(left - 1, right, current + "(", output)
            if right > left:
                generate(left, right - 1, current + ")", output)
        output = []
        generate(n, n, "", output)
        return output
            

if __name__ == '__main__':
    test_cases = [
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (4, ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().generateParenthesis(test_case[0])
        print('output:', sorted(output))
        print('expected:', sorted(test_case[1]))
        assert sorted(output) == sorted(test_case[1])


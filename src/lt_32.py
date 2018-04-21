"""
https://leetcode.com/problems/longest-valid-parentheses

Related:
  - lt_20_valid-parentheses
"""

"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4. 
"""

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        # https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleHard/32.html
        max_count = 0
        invalid_index = -1
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    start_index = stack[-1] if stack else invalid_index
                    max_count = max(max_count, i - start_index)
                else:
                    invalid_index = i
        return max_count
    
    def longestValidParentheses_failed(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0: return 0
        stack = []
        count = 0
        records = []
        for p in s:
            if p == '(':
                stack.append(p)
            else:
                if stack:
                    stack.pop()
                    count += 2
                    recor
                else:
                    stack = []
                    records.append(count)
                    count = 0
                    print('*', records)
        records.append(count)
        return max(records)


if __name__ == '__main__':
    test_cases = [
        ("(()", 2),
        (")()())", 4),
        ("()(()", 2),
        ("(()()", 4),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().longestValidParentheses(test_case[0])
        print('output:', output)
        assert output == test_case[1]


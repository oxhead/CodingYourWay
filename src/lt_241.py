"""
https://leetcode.com/problems/different-ways-to-add-parentheses

Related:
  - lt_95_unique-binary-search-trees-ii
  - lt_224_basic-calculator
  - lt_282_expression-add-operators
"""

"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1

Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2

Output: [0, 2]

Example 2

Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

Output: [-34, -14, -10, -10, 10]
"""

import re
import operator
from collections import defaultdict

class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # Time: O(?)
        # Space: O(?)
        def compute(i, j):
            if i == j: return [nums[i]]
            elif dp[i][j]: return dp[i][j]

            for k in range(i, j):
                for left in compute(i, k):
                    for right in compute(k+1, j):
                        dp[i][j].append(ops[k](left, right))
            return dp[i][j]
        
        tokens = re.split('(\D)', input)
        nums = list(map(int, tokens[::2]))
        ops = list(map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2]))
        dp = [[[] for _ in range(len(nums))] for _ in range(len(nums))]
        output = compute(0, len(nums) - 1)
        return output

    def diffWaysToCompute_failed(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def compute(i, j):
            if i >= j: return []
            elif dp[i][j]: return dp[i][j]
            
            if j - i == 1:
                dp[i][j] = [ops[i](nums[i], nums[j])]
                return dp[i][j]
            else:
                dp[i][j] = []
                for right in compute(i+1, j):
                    dp[i][j].append(ops[i](nums[i], right))
                for left in compute(i, j-1):
                    dp[i][j].append(ops[j-1](left, nums[j]))
                return dp[i][j]
                
        records = {}
        nums = []
        ops = []
        left = 0
        for index in range(len(input)):
            if input[index] in ('+', '-', '*'):
                nums.append(int(input[left:index]))
                if input[index] == '+': ops.append(operator.add)
                elif input[index] == '-': ops.append(operator.sub)
                elif input[index] == '*': ops.append(operator.mul)
                left = index + 1
            elif index == len(input) - 1:
                nums.append(int(input[left:index+1]))
        for i in range(len(nums) - 1):
            records[(i, i+1)] = ops[i]
        dp = [[set() for _ in range(len(nums))] for _ in range(len(nums))] 
        return compute(0, len(nums) - 1)

if __name__ == '__main__':
    test_cases = [
        #("2-1-1", [0, 2]),
        ("2*3-4*5", [-34, -14, -10, -10, 10]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().diffWaysToCompute(test_case[0])
        print('output:', output)
        assert sorted(output) == sorted(test_case[1])

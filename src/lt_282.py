"""
https://leetcode.com/problems/expression-add-operators

Related:
  - lt_150_evaluate-reverse-polish-notation
  - lt_224_basic-calculator
  - lt_227_basic-calculator-ii
  - lt_241_different-ways-to-add-parentheses
  - lt_494_arget-sum
"""

"""
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples:

"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""

class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # Time: O(?)
        # Space: O(?)
        # http://zxi.mytechroad.com/blog/searching/leetcode-282-expression-add-operators/
        # https://github.com/algorhythms/LeetCode/blob/master/282%20Expression%20Add%20Operators.py
        # Example:
        # 1234
        #         op next_val current_val previous_val current_val(new)
        # 1 + 2   +  3        3           2            6 (current_val + next_val)
        # 1 + 2   -  3        3           2            0 (current_val - next_val)
        # 1 + 2   *  3        3           2            7 (current_val - previous_val + previous * next_val)
        # 1 + 2   +  34       3           2            37
        # 1 + 2   -  34       3           2            -31
        # 1 + 2   *  34       3           2            69
        def dfs(index, current_str, current_val, previous):
            if index >= len(num):
                if current_val == target: output.append(current_str)
            else:
                for i in range(index, len(num)):
                    if i != index and num[index] == "0": continue
                    next_val = int(num[index:i+1])
                    if not current_str:
                        dfs(i+1, str(next_val), next_val, next_val)
                    else:
                        dfs(i+1, current_str + "+" + str(next_val), current_val + next_val, next_val)
                        dfs(i+1, current_str + "-" + str(next_val), current_val - next_val, -next_val)
                        dfs(i+1, current_str + "*" + str(next_val), current_val - previous + previous * next_val, previous * next_val)
        output = []
        dfs(0, "", 0, 0)
        return output


if __name__ == '__main__':
    test_cases = [
        (("123", 6), ["1+2+3", "1*2*3"]),
        (("232", 8), ["2*3+2", "2+3*2"]),
        (("105", 5), ["1*0+5","10-5"]),
        (("00", 0), ["0+0", "0-0", "0*0"]),
        (("3456237490", 9191), []),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().addOperators(*test_case[0])
        print('output:', output)
        assert sorted(output) == sorted(test_case[1])

"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number

Related:
  - lt_22_generate-parentheses
  - lt_39_combination-sum
  - lt_401_binary-watch
"""

"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
1:
2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz
0:

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want. 
"""

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Time: O(n * 4^n)
        # Space: O(n)
        if not digits or len(digits) == 0: return []
        MAPPING = {
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': [],
        }
        letters = [MAPPING[d] for d in digits]
        output = [[]]
        for letter_list in letters:
            output = [o + [letter] for o in output for letter in letter_list]  
        return [''.join(o) for o in output]

    def letterCombinations_dfs(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Time: O(n * 4^n)
        # Space: O(n)
        # https://shenjie1993.gitbooks.io/leetcode-python/017%20Letter%20Combinations%20of%20a%20Phone%20Number.html
        if not digits or len(digits) == 0: return []
        MAPPING = {
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': [],
        }
        def dfs(digits, current):
            if not digits:
                output.append(current)
                return
            for c in MAPPING[digits[0]]:
                dfs(digits[1:], current + c)
        output = []
        dfs(digits, "")
        return output


if __name__ == '__main__':
    test_cases = [
        ("", []),
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("234", ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']),
        ("222", ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().letterCombinations(test_case[0])
        print('output:', output)
        assert sorted(output) == sorted(test_case[1])


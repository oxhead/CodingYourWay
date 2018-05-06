"""
https://leetcode.com/problems/excel-sheet-column-title

Related:
  - lt_171_excel-sheet-column-number

Complexity:
"""

"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

Example 1:

Input: 1
Output: "A"

Example 2:

Input: 28
Output: "AB"

Example 3:

Input: 701
Output: "ZY"
"""

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Time: O(logn)
        # Space: O(1)
        output = []
        while n > 0:
            n -= 1
            c = n % 26
            output.append(chr(ord('A') + c))
            n = n // 26
        return "".join(reversed(output))

if __name__ == '__main__':
    test_cases = [
        (1, "A"),
        (28, "AB"),
        (701, "ZY"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().convertToTitle(test_case[0])
        print('output:', output)
        assert output == test_case[1]


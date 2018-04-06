"""
https://leetcode.com/problems/zigzag-conversion

Related:
"""

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 
"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s): return s
        output = [''] * numRows
        index, step = 0, 0
        for c in s:
            output[index] += c
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return "".join(output)

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        step = 2 * numRows - 2
        output = ""
        for i in range(numRows):
            for j in range(i, len(s), step):
                output += s[j]
                if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
                    output += s[j + step - 2 * i]
        return output
        

if __name__ == '__main__':
    test_cases = [
        (("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().convert(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


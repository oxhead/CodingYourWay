"""
https://leetcode.com/problems/count-and-say

Related:
  - lt_271
  - lt_443

Complexity:
  - Time: O()
  - Space: O()
"""

"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"
"""

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return '1'

        output = '1'
        for i in range(2, n+1):
            previous_output = output
            output = ''
            while previous_output:
                current_digit = previous_output[0]
                count = 0
                for c in previous_output:
                    if c == current_digit: count += 1
                    else: break
                output += '{}{}'.format(count, current_digit)
                previous_output = previous_output[count:]
        return output
        

if __name__ == '__main__':
    test_cases = [
        (1, '1'),
        (2, '11'),
        (3, '21'),
        (4, '1211'),
        (5, '111221'),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().countAndSay(test_case[0])
        print('output:', output)
        assert output == test_case[1]


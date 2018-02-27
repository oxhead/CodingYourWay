"""
https://leetcode.com/problems/plus-one

Related:
  - lt_43
  - lt_67
  - lt_369

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits: return [0]
        output = [d for d in digits]
        output[-1] += 1
        carry = 0
        for i in range(len(output)-1, -1, -1):
            output[i] += carry
            carry = output[i] // 10
            output[i] = output[i] % 10
        if carry: output.insert(0, 1)
        return output

if __name__ == '__main__':
    test_cases = [
        ([0], [1]),
        ([1], [2]),
        ([1, 9], [2, 0]),
        ([1, 1], [1, 2])
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().plusOne(test_case[0])
        print('output:', output)
        assert output == test_case[1]


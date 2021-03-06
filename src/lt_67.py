"""
https://leetcode.com/problems/add-binary

Related:
  - lt_2_add-two-numbers
  - lt_43_multiply-strings
  - lt_66_plus-one
"""

"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100". 
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        output = []
        i, j, carry = 0, 0, 0
        while i < len(a) or j < len(b) or carry:
            n1 = int(a[i]) if i < len(a) else 0
            n2 = int(b[j]) if j < len(b) else 0
            n = n1 + n2 + carry
            carry = n // 2
            n = n % 2
            output.append(str(n))
            i += 1
            j += 1
        return "".join(reversed(output))

    def addBinary_verbose(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(b) > len(a):
            a, b = b, a
        offset = len(a) - len(b)
        output = [int(d) for d in a]
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            if i - offset >= 0:
                output[i] += int(b[i - offset])
            output[i] += carry
            carry = output[i] // 2
            output[i] %= 2
        if carry:
            output.insert(0, carry)
        return ''.join([str(d) for d in output])


if __name__ == '__main__':
    test_cases = [
        (("11", "1"), "100"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().addBinary(*test_case[0])
        print('output:', output)
        assert output == test_case[1]


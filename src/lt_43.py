"""
https://leetcode.com/problems/multiply-strings

Related:
  - lt_2_add-two-numbers
  - lt_66_plus-one
  - lt_67_add-binary
  - lt_415_add-strings
"""

"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

    The length of both num1 and num2 is < 110.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        records = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                records[i + j] += int(num1[i]) * int(num2[j])
                records[i + j + 1] += records[i + j] // 10
                records[i + j] %= 10
        index = len(records) - 1
        while index > 0 and records[index] == 0:
            index -= 1
        return ''.join(map(str, records[index::-1]))

    def multiply_verbose(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def multiply(n1, n2):
            output = ""
            carry = 0
            assert len(n2) == 1
            if n1 == "0" or n2 == "0": return "0"
            for i, n in enumerate(n1[::-1]):
                val = int(n) * int(n2) + carry
                carry = val // 10
                val = val % 10
                output = str(val) + output
            if carry: output = str(carry) + output
            return output

        def plus(n1, n2):
            output = ""
            carry = 0
            i1, i2 = len(n1) - 1, len(n2) - 1
            while i1 >= 0 or i2 >= 0 or carry:
                val1 = int(n1[i1]) if i1 >= 0 else 0
                val2 = int(n2[i2]) if i2 >= 0 else 0
                n = val1 + val2 + carry
                carry = n // 10
                n = n % 10
                output = str(n) + output
                i1 -= 1
                i2 -= 1
            return output
        if not num1 or not num2: return None
        output = "0"
        for i, n in enumerate(num2[::-1]):
            m = multiply(num1, n)
            if m != '0': m = m + "0" * i
            output = plus(output, m)
        return output
        

if __name__ == '__main__':
    test_cases = [
        (("9", "9"), "81"),
        (("0", "52"), "0"),
        (("123", "45"), "5535"),
        (("9133", "0"), "0"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().multiply(*test_case[0])
        print('output:', output)
        assert output == test_case[1]
